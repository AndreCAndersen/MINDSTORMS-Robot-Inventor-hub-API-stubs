PORTS: dict = None
MOTOR_TYPES: tuple = None

def sleep_ms(*args, **kwargs):
    pass


def _is_motor(*args, **kwargs):
    pass


def is_type(*args, **kwargs):
    pass


def newSensorDisconnectedError(*args, **kwargs):
    pass


def wait_for_async(*args, **kwargs):
    pass


def clamp_speed(*args, **kwargs):
    pass


def clamp_power(*args, **kwargs):
    pass


class Motor:

    BRAKE: str = 'brake'
    HOLD: str = 'hold'
    COAST: str = 'coast'

    def __init__(self, *args, **kwargs):
        pass

    def start(self, *args, **kwargs):
        pass

    def stop(self, *args, **kwargs):
        pass

    def run_for_degrees(self, *args, **kwargs):
        pass

    def run_to_position(self, *args, **kwargs):
        pass

    def get_position(self, *args, **kwargs):
        pass

    def get_speed(self, *args, **kwargs):
        pass

    def get_degrees_counted(self, *args, **kwargs):
        pass

    def set_degrees_counted(self, *args, **kwargs):
        pass

    def get_default_speed(self, *args, **kwargs):
        pass

    def set_default_speed(self, *args, **kwargs):
        pass

    def set_stop_action(self, *args, **kwargs):
        pass

    def set_stall_detection(self, *args, **kwargs):
        pass

    def run_to_degrees_counted(self, *args, **kwargs):
        pass

    def run_for_rotations(self, *args, **kwargs):
        pass

    def run_for_seconds(self, *args, **kwargs):
        pass

    def start_at_power(self, *args, **kwargs):
        pass

    def was_interrupted(self, *args, **kwargs):
        pass

    def was_stalled(self, *args, **kwargs):
        pass
