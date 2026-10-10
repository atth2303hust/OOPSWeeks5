from datetime import date

class DeviceStatus:
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class PrinterType:
    INKJET = "INKJET"
    LASER = "LASER"


# Lớp cơ sở (Base Class)
class Device:

    def __init__(
        self,
        device_id,
        name,
        manufacture_year,
        purchase_cost,
        status=DeviceStatus.ACTIVE,
    ):
        # Kiểm tra năm sản xuất không được lớn hơn năm hiện tại 
        current_year = date.today().year
        if manufacture_year > current_year:
            raise ValueError("Năm sản xuất không được lớn hơn năm hiện tại")

        self.device_id = device_id
        self.name = name
        self.manufacture_year = manufacture_year
        self.purchase_cost = purchase_cost
        self.status = status

        # Các thuộc tính mạng 
        self.is_connected = False
        self.ip_address = None

    def calculate_annual_maintenance_cost(self):
        return 0

    def connect(self, ip):
        if self.is_connected == True:
            raise RuntimeError("Đã kết nối rồi!")
        self.is_connected = True
        self.ip_address = ip

    def disconnect(self):
        self.is_connected = False
        self.ip_address = None


# Lớp Computer
class Computer(Device):

    def __init__(
        self,
        device_id,
        name,
        manufacture_year,
        purchase_cost,
        ram,
        cpu,
        has_gpu,
        status=DeviceStatus.ACTIVE,
    ):
        super().__init__(
            device_id, name, manufacture_year, purchase_cost, status
        )
        self.ram = ram
        self.cpu = cpu
        self.has_gpu = has_gpu

    def calculate_annual_maintenance_cost(self):
       
        from decimal import Decimal

        return Decimal("2000000")


# Lớp Printer
class Printer(Device):

    def __init__(
        self,
        device_id,
        name,
        manufacture_year,
        purchase_cost,
        printer_type,
        page_count,
        is_color,
        status=DeviceStatus.ACTIVE,
    ):
        super().__init__(
            device_id, name, manufacture_year, purchase_cost, status
        )
        self.printer_type = printer_type
        self.page_count = page_count
        self.is_color = is_color

    def calculate_annual_maintenance_cost(self):
        from decimal import Decimal

        return Decimal("1120000")


# Lớp NetworkPrinter kế thừa từ Printer
class NetworkPrinter(Printer):

    def __init__(
        self,
        device_id,
        name,
        manufacture_year,
        purchase_cost,
        printer_type,
        page_count,
        is_color,
        status=DeviceStatus.ACTIVE,
    ):
        super().__init__(
            device_id,
            name,
            manufacture_year,
            purchase_cost,
            printer_type,
            page_count,
            is_color,
            status,
        )


# Lớp Projector
class Projector(Device):

    def __init__(
        self,
        device_id,
        name,
        manufacture_year,
        purchase_cost,
        resolution,
        lamp_hours,
        status=DeviceStatus.ACTIVE,
    ):
        super().__init__(
            device_id, name, manufacture_year, purchase_cost, status
        )
        self.resolution = resolution
        self.lamp_hours = lamp_hours

    def calculate_annual_maintenance_cost(self):
        from decimal import Decimal

        return Decimal("2100000")


# Lớp LabRoom quản lý thiết bị
class LabRoom:

    def __init__(self, room_id, name, capacity):
        self.room_id = room_id
        self.name = name
        self.capacity = capacity
        self.devices = []  # Dùng danh sách bình thường

    def add_device(self, device):
        
        for d in self.devices:
            if d.device_id == device.device_id:
                raise ValueError("Thiết bị bị trùng ID!")
        self.devices.append(device)

    def calculate_annual_maintenance_cost(self):
        from decimal import Decimal

        total = Decimal("0")
        for d in self.devices:
            total += d.calculate_annual_maintenance_cost()
        return total