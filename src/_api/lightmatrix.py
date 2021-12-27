"""
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
>> list ORIENTATIONS
>> list FACES
>> function rotate_orientation
>> function get_current_orientation
>> function set_current_orientation
"""

class LightMatrix:

    _ALLOWED_EFFECTS: list = None

    def __init__(self, *args, **kwargs:
        pass

    def write(self, *args, **kwargs):
        pass

    def off(self, *args, **kwargs):
        pass

    def set_pixel(self, *args, **kwargs):
        pass

    def show(self, *args, **kwargs):
        pass

    def show_image(self, *args, **kwargs):
        pass

    def play_animation(self, *args, **kwargs):
        pass

    def start_animation(self, *args, **kwargs):
        pass

    def _perform_animation(self, *args, **kwargs):
        pass

    def get_orientation(self, *args, **kwargs):
        pass

    def set_orientation(self, *args, **kwargs):
        pass

    def rotate(self, *args, **kwargs):
        pass
