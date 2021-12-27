"""

> module motor
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
>> System system
>> dict PORTS
>> function _is_motor
>> function is_type
>> tuple MOTOR_TYPES
>> function newSensorDisconnectedError
>> function wait_for_async
>> function clamp_speed
>> function clamp_power
"""


class Motor:
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


"""
>> type Motor
>>> type __class__
>>> function __init__
>>> str __module__
>>> str __name__
>>> str __qualname__
>>> tuple __bases__
>>> dict __dict__
>>> str BRAKE
>>> str HOLD
>>> str COAST
"""
