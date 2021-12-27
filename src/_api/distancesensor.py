"""
> module distancesensor
>> type __class__
>>> type __class__
>>> str __name__
>>> tuple __bases__
>>> dict __dict__
>> str __name__
>> str __file__
>> function sleep_ms
>> int LPF2_FLIPPER_DISTANCE
>> dict PORTS
>> function is_type
>> function clamp
>> function newSensorDisconnectedError
"""


class DistanceSensor:
    IN: str = 'in'
    CM: str = 'cm'
    PERCENT: str = 'percent'
    _LIGHT_MODE: int = None
    _LONG_RANGE_MODE: tuple = None
    _SHORT_RANGE_MODE: tuple = None

    def __init__(self, *args, **kwargs):
        pass

    def light_up_all(self, *args, **kwargs):
        pass

    def light_up(self, *args, **kwargs):
        pass

    def _set_range(self, *args, **kwargs):
        pass

    def _set_light(self, *args, **kwargs):
        pass

    def _is_distance_sensor(self, *args, **kwargs):
        pass

    def get_distance_cm(self, *args, **kwargs):
        pass

    def get_distance_inches(self, *args, **kwargs):
        pass

    def get_distance_percentage(self, *args, **kwargs):
        pass

    def wait_for_distance_farther_than(self, *args, **kwargs):
        pass

    def wait_for_distance_closer_than(self, *args, **kwargs):
        pass
