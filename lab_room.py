from decimal import Decimal

from device import Device
from device_status import DeviceStatus


class LabRoom:
    """Phòng thực hành kết tập nhiều đối tượng Device."""

    def __init__(self, room_id, name, capacity):
        if not room_id or not room_id.strip():
            raise ValueError("Mã phòng không được rỗng.")
        if not name or not name.strip():
            raise ValueError("Tên phòng không được rỗng.")
        if capacity <= 0:
            raise ValueError("Sức chứa phải lớn hơn 0.")

        self.room_id = room_id.strip()
        self.name = name.strip()
        self.capacity = capacity
        # Newbie thường dùng list bình thường, không dùng kiểu tuple view nâng cao
        self._devices = []

    @property
    def devices(self):
        # Trả về danh sách
        return self._devices

    def add_device(self, device):
        if device is None:
            raise ValueError("Không chấp nhận thiết bị None.")
        
        #Kiểm tra trùng mã 
        for d in self._devices:
            if d.device_id == device.device_id:
                raise ValueError(
                    f"Thiết bị có mã {device.device_id} đã tồn tại trong phòng {self.room_id}."
                )
        self._devices.append(device)

    def remove_device(self, device_id):
        # Tìm và xóa
        for d in self._devices:
            if d.device_id == device_id:
                self._devices.remove(d)
                return True
        return False

    def find_device(self, device_id):
        
        for d in self._devices:
            if d.device_id == device_id:
                return d
        return None

    def calculate_annual_maintenance_cost(self):
        # Hàm cộng dồn
        total = Decimal("0")
        for d in self._devices:
            total = total + d.calculate_annual_maintenance_cost()
        return total

    def get_devices_requiring_maintenance(self):
        
        result = []
        for d in self._devices:
            if d.status == DeviceStatus.UNDER_MAINTENANCE or d.years_in_use > 5:
                result.append(d)
        return result