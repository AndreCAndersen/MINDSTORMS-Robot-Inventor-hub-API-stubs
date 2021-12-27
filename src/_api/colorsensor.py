LPF2_FLIPPER_COLOR: int = None
PORTS: dict = None
_COLORLIST: list = None
_COMBI_MODE: tuple = None
_LIGHT_MODE: tuple = None
_AMBIENT_MODE: tuple = None

def sleep_ms(*args, **kwargs):
    pass


def get_sensor_value(*args, **kwargs):
    pass


def is_type(*args, **kwargs):
    pass


def clamp(*args, **kwargs):
    pass


def newSensorDisconnectedError(*args, **kwargs):
    pass


def _get_port_device(*args, **kwargs):
    pass


def _is_color_sensor(*args, **kwargs):
    pass

class ColorSensor:
    def __init__(self, *args, **kwargs):
        pass

    def _set_mode(self, *args, **kwargs):
        pass

    def _get_color(self, *args, **kwargs):
        pass

    def get_color(self, *args, **kwargs):
        pass

    def get_reflected_light(self, *args, **kwargs):
        pass

    def get_rgb_intensity(self, *args, **kwargs):
        pass

    def get_red(self, *args, **kwargs):
        pass

    def get_green(self, *args, **kwargs):
        pass

    def get_blue(self, *args, **kwargs):
        pass

    def get_ambient_light(self, *args, **kwargs):
        pass

    def wait_until_color(self, *args, **kwargs):
        pass

    def wait_for_new_color(self, *args, **kwargs):
        pass

    def light_up_all(self, *args, **kwargs):
        pass

    def light_up(self, *args, **kwargs):
        pass
