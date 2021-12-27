"""
> module motionsensor
>> type __class__
>>> type __class__
>>> str __name__
>>> tuple __bases__
>>> dict __dict__
>> str __name__
>> str __file__
>> module hub
>>> type __class__
>>> str __name__
>>> str __version__
>>> int BACK
>>> int BOTTOM
>>> type BT_VCP
>>> int FRONT
>>> type Image
>>> int LEFT
>>> int RIGHT
>>> int TOP
>>> type USB_VCP
>>> Battery battery
>>> bluetooth bluetooth
>>> type button
>>> dict config
>>> Display display
>>> function file_transfer
>>> function info
>>> function led
>>> Motion motion
>>> type port
>>> function power_off
>>> function repl_restart
>>> function reset
>>> Sound sound
>>> function status
>>> supervision supervision
>>> function temperature
>> function sleep_ms

"""

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
