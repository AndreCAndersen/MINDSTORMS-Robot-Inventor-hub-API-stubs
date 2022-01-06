LPF2_FLIPPER_COLOR: int = None
PORTS: dict = None
_COLORLIST: list = None
_COMBI_MODE: tuple = None
_LIGHT_MODE: tuple = None
_AMBIENT_MODE: tuple = None

def sleep_ms(*args, **kwargs):
    pass


def get_sensor_value(*args, **kwargs):
    pass


def is_type(*args, **kwargs):
    pass


def clamp(*args, **kwargs):
    pass


def newSensorDisconnectedError(*args, **kwargs):
    pass


def _get_port_device(*args, **kwargs):
    pass


def _is_color_sensor(*args, **kwargs):
    pass

class ColorSensor:
    """This is the Color sensor Library, you can use the functions here to detect colors, ambient light and light
    reflection. To use the Color Sensor, you must first initialize it.
    """
    def __init__(self, *args, **kwargs):
        pass

    def get_color(self):
        """Returns the color the color sensor sees.
        Examples:

            from mindstorms import MSHub, ColorSensor
            from mindstorms.operator import not_equal_to


            hub = MSHub()
            paper_scanner = ColorSensor('E')

            color = paper_scanner.get_color()
            if not_equal_to(color, None):
                hub.status_light.on(color)
                hub.light_matrix.write('Color ' + color + ' detected')
            else :
                hub.light_matrix.write('No color detected')
        """
        pass

    def get_ambient_light(self):
        """Returns the intensity of the ambient light. The Color Sensor changes mode to detected the ambient light,
        this can affect your program in unexpected ways. For example, the Color Sensor can't read colors when it is in
        ambient light mode.
        """
        pass

    def get_reflected_light(self):
        """Returns the intensity of the reflected light.
        """
        pass

    def get_rgb_intensity(self):
        """Returns the intensity of the red, green and blue color and the overall color intensity.
        Examples:

            from mindstorms import MSHub, ColorSensor
            from mindstorms.control import wait_for_seconds

            # Display the red intensity, tuple [0].
            hub = MSHub()
            paper_scanner = ColorSensor('E')

            wait_for_seconds(1)
            rgb_intensity = paper_scanner.get_rgb_intensity()
            hub.light_matrix.write('red = ')
            # Display the red intensity, tuple [0].
            hub.light_matrix.write(rgb_intensity[0])
            wait_for_seconds(1)
            hub.light_matrix.write('overall = ')
            # Display the overall intensity, tuple [3].
            hub.light_matrix.write(rgb_intensity[3])
        """
        pass

    def get_red(self):
        """Returns the red color intensity detected by the Color Sensor.
        """
        pass

    def get_green(self):
        """Returns the green color intensity detected by the Color Sensor.
        """
        pass

    def get_blue(self):
        """Returns the blue color intensity detected by the Color Sensor.
        """
        pass

    def wait_until_color(self, color: str):
        """Waits until the Color Sensor detects the specified color.Waits until the Color Sensor detects the specified
        color.

        Examples:

            from mindstorms import ColorSensor

            color_sensor = ColorSensor('A')

            color_sensor.wait_until_color('blue')
            # Put your own code here

        :param color: The name of the color.
        """
        assert color in ['black', 'blue', 'cyan', 'green', 'red', 'violet', 'white', 'yellow' or None]

    def wait_for_new_color(self):
        """Waits until the Color Sensor detects a new color. The first time this method is called, it immediately
        returns the detected color. After that, it waits until the Color Sensor detects a color that’s different from
        the color that was detected the last time this method was used.
        Examples:

            from mindstorms import ColorSensor

            color_sensor = ColorSensor('A')

            while True:
                color = color_sensor.wait_for_new_color()
                if color == 'black':
                    # Put your own code here
                    print('black')
                elif color == 'white':
                    # Put your own code here
                    print('white')
        """
        pass

    def light_up_all(self, brightness: int = 100):
        """Lights up all of the lights on the Color Sensor at the specified brightness. The Color Sensor changes mode
        to light up, this can affect your program in unexpected ways. For example, the Color Sensor can't read colors
        when it's in light up mode.Lights up all of the lights on the Color Sensor at the specified brightness. The
        Color Sensor changes mode to light up, this can affect your program in unexpected ways. For example, the Color
        Sensor can't read colors when it's in light up mode.

        Examples:

            from mindstorms import ColorSensor

            color_sensor = ColorSensor('A')
            # Turns on the Color Sensor's lights at 100% (default) brightness.
            color_sensor.light_up_all()
            # Turns on the Color Sensor's lights at 10% brightness..
            color_sensor.light_up_all(10)

        :param brightness: The desired brightness in percent of the Color Sensor lights.
        """
        assert 0 <= brightness <= 100

    def light_up(self, light_1: int = 100, light_2: int = 100, light_3: int = 100):
        """Sets the brightness of each individual lights on the Color Sensor.
        The Color Sensor changes mode to light up, this can affect your program in unexpected ways. For example, the
        Color Sensor can't read colors when it's in light up mode.Sets the brightness of each individual lights on the
        Color Sensor. The Color Sensor changes mode to light up, this can affect your program in unexpected ways. For
        example, the Color Sensor can't read colors when it's in light up mode.

        Examples:

            from mindstorms import ColorSensor

            color_sensor = ColorSensor('A')
            # Turn on one light (light_2) on the Color Sensor at full brightness.
            color_sensor.light_up(0, 100, 0)

        :param light_1: The desired brightness of the first light in percent.
        :param light_2: The desired brightness of the second light in percent.
        :param light_3: The desired brightness of the third light in percent.
        """
        assert 0 <= light_1 <= 100
        assert 0 <= light_2 <= 100
        assert 0 <= light_3 <= 100
