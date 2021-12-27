"""
> module motorpair
>> type __class__
>>> type __class__
>>> str __name__
>>> tuple __bases__
>>> dict __dict__
>> str __name__
>> str __file__

>> System system
>> dict PORTS
>> function _is_motor
>> function wait_for_async
>> function clamp_speed
>> function clamp_power
>> function from_steering
>> RuntimeError _DISCONNECTED_ERROR
>> RuntimeError _MOTOR_PAIRING_ERROR
>> function clamp_steering
"""


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












