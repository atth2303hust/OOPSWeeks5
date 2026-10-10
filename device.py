from abc import ABC, abstractmethod
from datetime import date
from decimal import Decimal

from device_status import DeviceStatus


class Device(ABC):
    """Lớp cơ sở trừu tượng cho mọi thiết bị trong hệ thống."""

    def __init__(
        self,
        device_id,
        name,
        year_in_use,
        purchase_price,
        status=DeviceStatus.ACTIVE,
    ):
        if not device_id or not device_id.strip():
            raise ValueError("Mã thiết bị không được rỗng.")

        self._device_id = device_id.strip()
        self.name = name
        self.year_in_use = year_in_use
        self.purchase_price = purchase_price
        self.status = status

    @property
    def device_id(self):
        return self._device_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Tên thiết bị không được rỗng.")
        self._name = value.strip()

    @property
    def year_in_use(self):
        return self._year_in_use

    @year_in_use.setter
    def year_in_use(self, value):
        current_year = date.today().year
        if value <= 0 or value > current_year:
            raise ValueError("Năm đưa vào sử dụng không hợp lệ.")
        self._year_in_use = value

    @property
    def purchase_price(self):
        return self._purchase_price

    @purchase_price.setter
    def purchase_price(self, value):
        price = Decimal(str(value))
        if price <= 0:
            raise ValueError("Giá mua phải lớn hơn 0.")
        self._purchase_price = price

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def years_in_use(self):
        current_year = date.today().year
        return current_year - self.year_in_use

    @abstractmethod
    def calculate_annual_maintenance_cost(self):
        pass

    def __str__(self):
        
        return (
            self.__class__.__name__
            + "(id="
            + str(self.device_id)
            + ", name="
            + str(self.name)
            + ", year="
            + str(self.year_in_use)
            + ", price="
            + str(self.purchase_price)
            + " VND, status="
            + str(self.status.value)
            + ")"
        )