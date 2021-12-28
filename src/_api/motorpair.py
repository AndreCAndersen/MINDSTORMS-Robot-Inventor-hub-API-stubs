PORTS: dict = None
_DISCONNECTED_ERROR: RuntimeError = None
_MOTOR_PAIRING_ERROR: RuntimeError = None


def _is_motor(*args, **kwargs):
    pass


def wait_for_async(*args, **kwargs):
    pass


def clamp_speed(*args, **kwargs):
    pass


def clamp_power(*args, **kwargs):
    pass


def from_steering(*args, **kwargs):
    pass


def clamp_steering(*args, **kwargs):
    pass


class MotorPair:
    IN: str = 'in'
    BRAKE: str = 'brake'
    HOLD: str = 'hold'
    CM: str = 'cm'
    COAST: str = 'coast'
    ROTATIONS: str = 'rotations'
    DEGREES: str = 'degrees'
    SECONDS: str = 'seconds'

    def __init__(self, *args, **kwargs):
        pass

    def start(self, *args, **kwargs):
        pass

    def stop(self, *args, **kwargs):
        pass

    def move(self, *args, **kwargs):
        pass

    def get_default_speed(self, *args, **kwargs):
        pass

    def set_default_speed(self, *args, **kwargs):
        pass

    def set_stop_action(self, *args, **kwargs):
        pass

    def start_at_power(self, *args, **kwargs):
        pass

    def was_interrupted(self, *args, **kwargs):
        pass

    def _move_with_speed(self, *args, **kwargs):
        pass

    def set_motor_rotation(self, *args, **kwargs):
        pass

    def move_tank(self, *args, **kwargs):
        pass

    def start_tank(self, *args, **kwargs):
        pass

    def start_tank_at_power(self, *args, **kwargs):
        pass












