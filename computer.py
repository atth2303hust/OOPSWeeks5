from decimal import Decimal

from device import Device
from device_status import DeviceStatus
from inetworkable import INetworkable


class Computer(Device, INetworkable):
    """Máy tính: một thiết bị và luôn có khả năng kết nối mạng."""

    def __init__(
        self,
        device_id,
        name,
        year_in_use,
        purchase_price,
        ram_gb,
        processor,
        has_dedicated_gpu,
        status=DeviceStatus.ACTIVE,
    ):
        super().__init__(device_id, name, year_in_use, purchase_price, status)

        if ram_gb <= 0:
            raise ValueError("Dung lượng RAM phải lớn hơn 0.")
        if not processor or not processor.strip():
            raise ValueError("Loại bộ xử lý không được rỗng.")

        self.ram_gb = ram_gb
        self.processor = processor.strip()
        self.has_dedicated_gpu = has_dedicated_gpu
        self._ip_address = None

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
        if self.is_connected == True:
            raise RuntimeError("Đang kết nối; không thể kết nối lại.")

        if ip_address == None or ip_address == "":
            raise ValueError("Địa chỉ IP không được rỗng.")

        self._ip_address = ip_address.strip()

    def disconnect(self):
        self._ip_address = None

    def calculate_annual_maintenance_cost(self):
        # 5% cơ bản; +2% nếu có GPU rời; +1% nếu đã dùng trên 5 năm.
        rate = Decimal("0.05")

        if self.has_dedicated_gpu == True:
            rate = rate + Decimal("0.02")

        if self.years_in_use > 5:
            rate = rate + Decimal("0.01")

        return self.purchase_price * rate

    def __str__(self):
        
        gpu_str = "No"
        if self.has_dedicated_gpu:
            gpu_str = "Yes"

        return (
            super().__str__()
            + ", RAM="
            + str(self.ram_gb)
            + "GB, CPU="
            + str(self.processor)
            + ", GPU="
            + gpu_str
        )