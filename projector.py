from decimal import Decimal
from device import Device
from device_status import DeviceStatus


class Projector(Device):

    def __init__(
        self,
        device_id,
        name,
        year_in_use,
        purchase_price,
        brightness_lumens,
        lamp_hours,
        status=DeviceStatus.ACTIVE,
    ):
        super().__init__(
            device_id, name, year_in_use, purchase_price, status
        )

        
        if brightness_lumens <= 0:
            raise ValueError("Độ sáng phải lớn hơn 0")
        if lamp_hours < 0:
            raise ValueError("Số giờ bóng đèn không được âm")

        self.brightness_lumens = brightness_lumens
        self.lamp_hours = lamp_hours

    def calculate_annual_maintenance_cost(self):
        
        cost = self.purchase_price * Decimal("0.03")
        if self.lamp_hours > 3000:
            cost = cost + Decimal("1500000")
        return cost

    def __str__(self):
        
        return (
            super().__str__()
            + ", brightness="
            + str(self.brightness_lumens)
            + "lm, "
            + "lamp_hours="
            + str(self.lamp_hours)
        )