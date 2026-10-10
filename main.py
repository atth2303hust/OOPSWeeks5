from device_maintenance_lab import (
    Computer,
    Device,
    DeviceStatus,
    INetworkable,
    LabRoom,
    NetworkPrinter,
    Printer,
    PrinterType,
    Projector,
)


def format_vnd(value):
    """Định dạng số tiền theo VND"""
    
    return str(int(value)) + " VND"


def print_room(room):
    """In danh sách thiết bị và thông tin phòng """
    print("=== " + room.room_id + " - " + room.name + " ===")

    for device in room.devices:
        print(device)
        print("  -> Chi phí bảo trì:", format_vnd(device.calculate_annual_maintenance_cost()))

    print("Tổng chi phí bảo trì:", format_vnd(room.calculate_annual_maintenance_cost()))
    print("Thiết bị cần bảo trì:")

    devices = room.get_devices_requiring_maintenance()
    if len(devices) == 0:
        print("  (Không có)")
    else:
        for device in devices:
            print("  - " + device.device_id + ": " + device.name)
    print()


def test_duplicate_device(room, device):
    """Kiểm thử thêm trùng thiết bị."""
    print("[TEST] Thêm thiết bị trùng mã vào LAB-A:")
    try:
        room.add_device(device)
    except ValueError as exc:
        print("  Đã chặn đúng:", exc)
        print()


def test_network_polymorphism(dev1, dev2, dev3):
    """Kiểm thử kết nối mạng."""
    print("=== KIỂM THỬ INetworkable ===")
    
    dev1.connect("10.0.0.11")
    print("Computer1 -> Connected:", dev1.is_connected, "| IP:", dev1.ip_address)

    dev2.connect("10.0.0.12")
    print("Computer2 -> Connected:", dev2.is_connected, "| IP:", dev2.ip_address)

    dev3.connect("10.0.0.21")
    print("NetworkPrinter -> Connected:", dev3.is_connected, "| IP:", dev3.ip_address)

    print("\n[TEST] Không cho phép kết nối lại khi đang kết nối:")
    try:
        dev1.connect("10.0.0.99")
    except RuntimeError as exc:
        print("  Đã chặn đúng:", exc)

    print("\n[TEST] Ngắt kết nối thiết bị đầu tiên:")
    dev1.disconnect()
    print("  Connected:", dev1.is_connected, "| IP sau khi ngắt:", dev1.ip_address)


def main():
    """Hàm chạy chương trình chính"""
    print("=== HỆ THỐNG QUẢN LÝ THIẾT BỊ VÀ HỢP ĐỒNG BẢO TRÌ ===\n")

    computer1 = Computer(
        "C001", "Workstation AI", 2020, 25000000,
        32, "Intel Core i7", True,
    )
    computer2 = Computer(
        "C002", "Office PC", 2024, 18000000,
        16, "Intel Core i5", False,
    )

    printer1 = Printer(
        "P001", "Color Inkjet", 2023, 8000000,
        PrinterType.INKJET, 150000, True,
    )
    network_printer = NetworkPrinter(
        "P002", "Network Laser", 2022, 12000000,
        PrinterType.LASER, 50000, False,
    )

    projector = Projector(
        "PJ001", "Main Projector", 2021, 20000000,
        5000, 4000, DeviceStatus.UNDER_MAINTENANCE,
    )

    room_a = LabRoom("LAB-A", "Phòng thực hành A", 40)
    room_b = LabRoom("LAB-B", "Phòng thực hành B", 35)

    room_a.add_device(computer1)
    room_a.add_device(printer1)
    room_a.add_device(projector)

    room_b.add_device(computer2)
    room_b.add_device(network_printer)

    test_duplicate_device(room_a, computer1)
    print_room(room_a)
    print_room(room_b)

    print("=== KIỂM THỬ TÌM THIẾT BỊ ===")
    found = room_a.find_device("P001")
    if found != None:
        print("Tìm thấy P001:", found.name)
    else:
        print("Không tìm thấy P001.")
    print()

    test_network_polymorphism(computer1, computer2, network_printer)


if __name__ == "__main__":
    main()