from abc import abstractmethod, ABC


class Device(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class LoggerMixin:
    def log(self, l_message):
        print('[LOG]:', l_message)


class Phone(Device, LoggerMixin):
    def turn_on(self):
        self.log("Phone is turning on")

    def turn_off(self):
        self.log("Phone is turning off")


class Laptop(Device, LoggerMixin):
    def turn_on(self):
        self.log("Laptop is turning on")

    def turn_off(self):
        self.log("Laptop is turning off")

devices = [Phone(), Laptop()]

for device in devices:
    device.turn_on()
    device.turn_off()
