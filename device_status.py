"""
/****************/
Mã sinh viên: <MSSV>
Họ tên: <HỌ VÀ TÊN>
/****************/
"""

from enum import Enum


class DeviceStatus(Enum):
    """Trạng thái hoạt động của thiết bị."""

    ACTIVE = "Active"
    UNDER_MAINTENANCE = "UnderMaintenance"
    RETIRED = "Retired"
