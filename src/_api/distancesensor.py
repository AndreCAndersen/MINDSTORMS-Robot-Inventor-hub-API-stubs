LPF2_FLIPPER_DISTANCE: int = None
PORTS: dict = None


def sleep_ms(*args, **kwargs):
    pass


def is_type(*args, **kwargs):
    pass


def clamp(*args, **kwargs):
    pass


def newSensorDisconnectedError(*args, **kwargs):
    pass


class DistanceSensor:
    """This is the Distance Sensor Library, you can use the functions here to detect objects within the sensor range
    and measure distances. To use the Distance Sensor, you must first initialize it.

    Examples:
        from mindstorms import DistanceSensor
        # Initialize the Distance Sensor.
        distance = DistanceSensor('A')
    """
    IN: str = 'in'
    CM: str = 'cm'
    PERCENT: str = 'percent'
    _LIGHT_MODE: int = None
    _LONG_RANGE_MODE: tuple = None
    _SHORT_RANGE_MODE: tuple = None

    def __init__(self, *args, **kwargs):
        pass

    def get_distance_cm(self, short_range: bool = False):
        """Returns the measured distance in centimeters.Returns the measured distance in centimeters.

        Examples:

            from mindstorms import DistanceSensor

            # Initialize the Distance Sensor.
            wall_detector = DistanceSensor('F')

            # Measure the distance between the Distance Sensor and object in centimeters and inches.
            dist_cm = wall_detector.get_distance_cm()
            dist_inches = wall_detector.get_distance_inches()
            # Print both results on the console.
            print('cm:', dist_cm, 'inches:', dist_inches)

        :param short_range: Whether or not to use short range mode. Short range mode increases accuracy, but it can only detect nearby objects.
        """
        assert isinstance(short_range, bool)

    def get_distance_inches(self, short_range: bool = False):
        """Returns the measured distance in inches.Returns the measured distance in inches.

        Examples:

            from mindstorms import DistanceSensor

            # Initialize the Distance Sensor.
            wall_detector = DistanceSensor('F')

            # Measure the distance between the Distance Sensor and object in centimeters and inches.
            dist_cm = wall_detector.get_distance_cm()
            dist_inches = wall_detector.get_distance_inches()
            # Print both results on the console.
            print('cm:', dist_cm, 'inches:', dist_inches)

        :param short_range: Whether or not to use short range mode. Short range mode increases accuracy, but it can
        only detect nearby objects.
        """
        assert isinstance(short_range, bool)

    def get_distance_percentage(self, short_range: bool = False):
        """Returns the measured distance as a percentage of the Distance Sensor detection range.Returns the measured
        distance as a percentage of the Distance Sensor detection range.


        :param short_range: Whether or not to use short range mode. Short range mode increases accuracy, but it can
        only detect nearby objects.
        """
        assert isinstance(short_range, bool)

    def wait_for_distance_farther_than(self, distance: float, unit: str = 'cm', short_range: bool = False):
        """Waits until the measured distance is greater than the specified distance.Waits until the measured distance
        is greater than the specified distance.

        Examples:

            from mindstorms import MSHub, DistanceSensor

            hub = MSHub()
            distance_sensor = DistanceSensor('F')

            while True:
                distance_sensor.wait_for_distance_farther_than(20, 'cm')
                hub.light_matrix.write('>')
                distance_sensor.wait_for_distance_closer_than(20, 'cm')
                hub.light_matrix.write('<')

        :param distance: The target distance to be detected from the sensor to an object.
        :param unit: The unit in which the distance is measured.
        :param short_range: Whether or not to use short range mode. Short range mode increases accuracy, but it can
        only detect nearby objects.
        """
        assert unit in ['cm', 'in', '%']
        assert isinstance(short_range, bool)

    def wait_for_distance_closer_than(self, distance: float, unit: str = 'cm', short_range: bool = False):
        """Waits until the measured distance is less than the specified distance.Waits until the measured distance is less than the specified distance.

        Examples:

            from mindstorms import MSHub, DistanceSensor

            hub = MSHub()
            distance_sensor = DistanceSensor('F')

            while True:
                distance_sensor.wait_for_distance_farther_than(20, 'cm')
                hub.light_matrix.write('>')
                distance_sensor.wait_for_distance_closer_than(20, 'cm')
                hub.light_matrix.write('<')

        :param distance: The target distance to be detected from the sensor to an object.
        :param unit: The unit in which the distance is measured.
        :param short_range: Whether or not to use short range mode. Short range mode increases accuracy, but it can only detect nearby objects.
        """
        assert unit in ['cm', 'in', '%']
        assert isinstance(short_range, bool)

    def light_up_all(self, brightness: int = 100):
        """Lights up all of the lights on the Distance Sensor at the specified brightness.Lights up all of the lights
        on the Distance Sensor at the specified brightness.

        Examples:

            from mindstorms import DistanceSensor

            distance_sensor = DistanceSensor('F')

            # Turn on the lights at maximum brightness (100%).
            distance_sensor.light_up_all(100)
            # Turn off the lights.
            distance_sensor.light_up_all(0)

        :param brightness: The desired brightness in percent of all the distance sensor lights.
        """
        assert 0 <= brightness <= 100

    def light_up(self, right_top: int = 100, left_top: int = 100, right_bottom: int = 100, left_bottom: int = 100):
        """Light up each individual lights of the Distance Sensor at the specified brightness.Light up each individual
        lights of the Distance Sensor at the specified brightness.

        Examples:

            from mindstorms import DistanceSensor

            distance_sensor = DistanceSensor('A')
            # Switch on the top light of the Distance Sensor.
            distance_sensor.light_up(100, 20, 0, 0)

        :param right_top: The brightness in percent of the right top light of the Distance Sensor.
        :param left_top: The brightness in percent of the left top light of the Distance Sensor.
        :param right_bottom: The brightness in percent of the right bottom light of the Distance Sensor.
        :param left_bottom: The brightness in percent of the left bottom light of the Distance Sensor.
        """
        assert 0 <= right_top <= 100
        assert 0 <= left_top <= 100
        assert 0 <= right_bottom <= 100
        assert 0 <= left_bottom <= 100

    def _set_range(self, *args, **kwargs):
        pass

    def _set_light(self, *args, **kwargs):
        pass

    def _is_distance_sensor(self, *args, **kwargs):
        pass
