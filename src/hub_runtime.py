__version__: str = None

BACK: int = None
BOTTOM: int = None
BT_VCP: type = None
FRONT: int = None
Image: type = None
LEFT: int = None
RIGHT: int = None
TOP: int = None
USB_VCP: type = None

button: type = None
port: type = None
battery: Battery = None
bluetooth: bluetooth = None
config: dict = None
display: Display = None
motion: Motion = None
sound: Sound = None
supervision: supervision = None


def file_transfer(*args, **kwargs):
    pass


def info(*args, **kwargs):
    pass


def led(*args, **kwargs):
    pass


def power_off(*args, **kwargs):
    pass


def repl_restart(*args, **kwargs):
    pass


def reset(*args, **kwargs):
    pass


def status(*args, **kwargs):
    pass


def temperature(*args, **kwargs):
    pass

