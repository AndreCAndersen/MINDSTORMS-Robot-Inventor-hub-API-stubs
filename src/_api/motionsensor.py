def sleep_ms(*args, **kwargs):
    pass


class MotionSensor:
    BACK: str = 'back'
    DOWN: str = 'down'
    FALLING: str = 'falling'
    FRONT: str = 'front'
    TAPPED: str = 'tapped'
    UP: str = 'up'
    LEFT_SIDE: str = 'left_side'
    RIGHT_SIDE: str = 'right_side'
    SHAKEN: str = 'shaken'
    DOUBLE_TAPPED: str = 'double_tapped'

    def __init__(self, *args, **kwargs):
        pass

    def align_to_model(self, *args, **kwargs):
        pass

    def get_orientation(self, *args, **kwargs):
        pass

    def _orientation_from_string(self, *args, **kwargs):
        pass

    def get_pitch_angle(self, *args, **kwargs):
        pass

    def get_roll_angle(self, *args, **kwargs):
        pass

    def get_yaw_angle(self, *args, **kwargs):
        pass

    def reset_yaw_angle(self, *args, **kwargs):
        pass

    def wait_for_new_orientation(self, *args, **kwargs):
        pass

    def get_gesture(self, *args, **kwargs):
        pass

    def was_gesture(self, *args, **kwargs):
        pass

    def wait_for_new_gesture(self, *args, **kwargs):
        pass
