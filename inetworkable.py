from abc import ABC, abstractmethod


class INetworkable(ABC):
    """Interface cho các thiết bị có khả năng kết nối mạng."""

    @property
    @abstractmethod
    def ip_address(self):
        pass

    @property
    @abstractmethod
    def is_connected(self):
        pass

    @abstractmethod
    def connect(self, ip_address):
        pass

    @abstractmethod
    def disconnect(self):
        pass