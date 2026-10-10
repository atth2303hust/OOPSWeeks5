from decimal import Decimal

from device_status import DeviceStatus
from inetworkable import INetworkable
from printer import Printer
from printer_type import PrinterType


class NetworkPrinter(Printer, INetworkable):
    """Printer chuyên biệt có thêm khả năng kết nối mạng."""

    def __init__(
        self,
        device_id,
        name,
        year_in_use,
        purchase_price,
        printer_type,
        printed_pages,
        is_color,
        status=DeviceStatus.ACTIVE,
    ):
        super().__init__(
            device_id,
            name,
            year_in_use,
            purchase_price,
            printer_type,
            printed_pages,
            is_color,
            status,
        )
        self._ip_address = None

    @property
    def supports_network(self):
        return True

    @property
    def ip_address(self):
        return self._ip_address

    @property
    def is_connected(self):
        
        if self._ip_address != None:
            return True
        else:
            return False

    def connect(self, ip_address):
        # Kiểm tra trạng thái kết nối
        if self.is_connected == True:
            raise RuntimeError("Đang kết nối; không thể kết nối lại.")

        if ip_address == None or ip_address == "":
            raise ValueError("Địa chỉ IP không được rỗng.")

        self._ip_address = ip_address.strip()

    def disconnect(self):
        self._ip_address = None