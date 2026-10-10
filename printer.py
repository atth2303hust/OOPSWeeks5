from decimal import Decimal

from device import Device
from device_status import DeviceStatus
from printer_type import PrinterType


class Printer(Device):
    """Máy in thông thường; mặc định không mang năng lực mạng."""

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
            device_id, name, year_in_use, purchase_price, status
        )

                if printed_pages < 0:
            raise ValueError("Số trang đã in không được âm.")

        self.printer_type = printer_type
        self.printed_pages = printed_pages
        self.is_color = is_color

    @property
    def supports_network(self):
        """Printer thường không hỗ trợ mạng trong mô hình đã chọn."""
        return False

    def calculate_annual_maintenance_cost(self):
        cost = self.purchase_price * Decimal("0.04")

        # Dùng phép tính tường minh
        if self.printed_pages > 100000:
            cost = cost + Decimal("500000")
        if self.is_color == True:
            cost = cost + Decimal("300000")

        return cost

    def __str__(self):
            color_str = "No"
        if self.is_color:
            color_str = "Yes"

        network_str = "No"
        if self.supports_network:
            network_str = "Yes"

        return (
            super().__str__()
            + ", type="
            + str(self.printer_type.value)
            + ", pages="
            + str(self.printed_pages)
            + ", color="
            + color_str
            + ", network="
            + network_str
        )