LPF2_FLIPPER_FORCE: int = None
PORTS: dict = None


def sleep_ms(*args, **kwargs):
    pass


def is_type(*args, **kwargs):
    pass


def newSensorDisconnectedError(*args, **kwargs):
    pass


def _is_force_sensor(*args, **kwargs):
    pass


def _get_port_device(*args, **kwargs):
    pass


class ForceSensor:
    def __init__(self, *args, **kwargs):
        pass

    def is_pressed(self, *args, **kwargs):
        pass

    def wait_until_pressed(self, *args, **kwargs):
        pass

    def wait_until_released(self, *args, **kwargs):
        pass

    def _is_pressed(self, *args, **kwargs):
        pass

    def get_force_newton(self, *args, **kwargs):
        pass

    def get_force_percentage(self, *args, **kwargs):
        pass
