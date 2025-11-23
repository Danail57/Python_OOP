from abc import ABC, abstractmethod


class PowerConnectable(ABC):
    @abstractmethod
    def plug_in_power(self):
        pass


class HDMIConnectable(ABC):
    @abstractmethod
    def connect_via_hdmi(self, device):
        pass


class RCAConnectable(ABC):
    @abstractmethod
    def connect_via_rca(self, device):
        pass


class EthernetConnectable(ABC):
    @abstractmethod
    def connect_via_ethernet(self, device):
        pass


class Television(PowerConnectable, HDMIConnectable, RCAConnectable):
    def plug_in_power(self):
        print("TV connected to power")

    def connect_via_hdmi(self, device):
        print(f"TV connected to {device} via HDMI")

    def connect_via_rca(self, device):
        print(f"TV connected to {device} via RCA")


class DVDPlayer(PowerConnectable, HDMIConnectable):
    def plug_in_power(self):
        print("DVD player connected to power")

    def connect_via_hdmi(self, device):
        print(f"DVD connected to {device} via HDMI")


class GameConsole(PowerConnectable, HDMIConnectable, EthernetConnectable):
    def plug_in_power(self):
        print("Console connected to power")

    def connect_via_hdmi(self, device):
        print(f"Console connected to {device} via HDMI")

    def connect_via_ethernet(self, device):
        print(f"Console connected to {device} via Ethernet")


class Router(PowerConnectable, EthernetConnectable):
    def plug_in_power(self):
        print("Router connected to power")

    def connect_via_ethernet(self, device):
        print(f"Router connected to {device} via Ethernet")
