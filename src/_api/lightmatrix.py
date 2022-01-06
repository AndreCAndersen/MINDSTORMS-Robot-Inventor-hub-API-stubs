ORIENTATIONS: list = None
FACES: list = None

def rotate_orientation(*args, **kwargs):
    pass


def get_current_orientation(*args, **kwargs):
    pass


def set_current_orientation(*args, **kwargs):
    pass

class LightMatrix:
    """This is the Light Matrix component part of the Hub, you can use the following functions to display pixels,
    images, numbers or text on the Light Matrix.
    """

    _ALLOWED_EFFECTS: list = None

    def set_pixel(self, x: int, y: int, brightness: int = 100):
        """Sets the brightness of one pixel (one of the 25 LEDs) on the Light Matrix.Sets the brightness of one pixel
        (one of the 25 LEDs) on the Light Matrix.

        Examples:

            from mindstorms import MSHub

            hub = MSHub()

            hub.light_matrix.set_pixel(1, 4, 90)

        :param x: Pixel position of the Light Matrix 5 columns, counting from the left.
        :param y: Pixel position of the Light Matrix 5 rows, counting from the top.
        :param brightness: Brightness of the specified pixel in percent
        """
        assert 0 <= x <= 4
        assert 0 <= y <= 4
        assert 0 <= brightness <= 100

    def show_image(self, image: str, brightness: int = 100):
        """Shows an image on the Light Matrix.Shows an image on the Light Matrix.

        Examples:

            from mindstorms import MSHub
            from mindstorms.control import wait_for_seconds

            hub = MSHub()

            hub.light_matrix.show_image('HAPPY')
            wait_for_seconds(5)
            hub.light_matrix.show_image('ASLEEP')

        :param image: Name of the image.
        :param brightness: Brightness of the image in percent
        """
        assert image in ['ANGRY', 'ARROW_E', 'ARROW_N', 'ARROW_NE', 'ARROW_NW', 'ARROW_S', 'ARROW_SE', 'ARROW_SW',
                         'ARROW_W', 'ASLEEP', 'BUTTERFLY', 'CHESSBOARD', 'CLOCK1', 'CLOCK10', 'CLOCK11', 'CLOCK12',
                         'CLOCK2', 'CLOCK3', 'CLOCK4', 'CLOCK5', 'CLOCK6', 'CLOCK7', 'CLOCK8', 'CLOCK9', 'CONFUSED',
                         'COW', 'DIAMOND', 'DIAMOND_SMALL', 'DUCK', 'FABULOUS', 'GHOST', 'GIRAFFE', 'GO_RIGHT',
                         'GO_LEFT', 'GO_UP', 'GO_DOWN', 'HAPPY', 'HEART', 'HEART_SMALL', 'HOUSE', 'MEH',
                         'MUSIC_CROTCHET', 'MUSIC_QUAVER', 'MUSIC_QUAVERS', 'NO', 'PACMAN', 'PITCHFORK', 'RABBIT',
                         'ROLLERSKATE', 'SAD', 'SILLY', 'SKULL', 'SMILE', 'SNAKE', 'SQUARE', 'SQUARE_SMALL',
                         'STICKFIGURE', 'SURPRISED', 'SWORD', 'TARGET', 'TORTOISE', 'TRIANGLE', 'TRIANGLE_LEFT',
                         'TSHIRT', 'UMBRELLA', 'XMAS', 'YES']
        assert 0 <= brightness <= 100

    def write(self, text: str):
        """Displays text on the Light Matrix, one letter at a time, scrolling from right to left. The program will not
        continue until all of the specified text have been displayed.Displays text on the Light Matrix, one letter at a
        time, scrolling from right to left. The program will not continue until all of the specified text have been
        displayed.

        Examples:

            from mindstorms import MSHub

            hub = MSHub()

            hub.light_matrix.write('Hello!')
            # Show the number "1" on the Light Matrix.
            hub.light_matrix.write('1')

        :param text: Text to display. If a character is unknown, ? will be displayed instead.
        """
        pass

    def off(self):
        """Turns off all the pixels (LEDs) of the Light Matrix.
        Examples:

            from mindstorms import MSHub
            from mindstorms.control import wait_for_seconds

            hub = MSHub()

            hub.light_matrix.show_image('TARGET')
            wait_for_seconds(3)
            hub.light_matrix.off()
        """
        pass

    def show(self, pixels: int):
        """Show an array of pixels on the light matrix.Show an array of pixels on the light matrix.

        Examples:

            from mindstorms import MSHub

            hub = MSHub()

            pixels = '99999:77777:55555:33333:11111'
            hub.light_matrix.show(pixels)

        :param pixels: Array of pixels to display on the light matrix.
        """
        assert 0 <= pixels <= 9

    def play_animation(self, animation: str, fps: int = 2.5, effect: str = 'direct', clear: bool = False):
        """Plays an animation on the light matrix.

        The program will not continue until the animation has finished playing.Plays an animation on the light matrix.

        The program will not continue until the animation has finished playing.

        Examples:

            from mindstorms import MSHub

            hub = MSHub()

            anim_countdown = [
               '09990:09000:09990:00090:09990',
               '09090:09090:09990:00090:00090',
               '09990:00090:09990:00090:09990',
               '09990:00090:09990:09000:09990',
               '00900:09900:00900:00900:09990',
               '99999:99999:99999:99999:99999'
            ]
            hub.light_matrix.play_animation(anim_countdown, 10, 'fade out', True)

        :param animation: The animation to be played. Animation should be composed of multiple strings separated by
        commas. Each string consists of 5 groups of 5 numbers from 0 to 9 separated by ':'. Each group of 5 numbers
        represents a line of pixels of the light matrix with the first number of the first group representing the
        first left pixel of the first top line and the value representing the brightness 0 being off and 9 being 100%
        brightness.
        :param fps: The speed at which the animation is played, i.e. animation frames displayed per second.
        :param effect: The effect that is applied to the animation.
        :param clear: Whether or not the animation should clear the display upon completion.
        """
        assert 1 <= fps <= 20
        assert effect in ['direct', 'overlay', 'slide right', 'slide left', 'fade in', 'fade out']
        assert isinstance(clear, bool)

    def start_animation(self, animation: str, fps: int = 2.5, loop: bool = False, effect: str = 'direct',
                        clear: bool = False):
        """Starts an animation on the light matrix.

        The program will not wait for the animation to finish playing before proceeding to the next command.Starts an
        animation on the light matrix.

        The program will not wait for the animation to finish playing before proceeding to the next command.

        Examples:

            from mindstorms import MSHub

            hub = MSHub()

            anim_countdown = [
               '09990:09000:09990:00090:09990',
               '09090:09090:09990:00090:00090',
               '09990:00090:09990:00090:09990',
               '09990:00090:09990:09000:09990',
               '00900:09900:00900:00900:09990',
               '99999:99999:99999:99999:99999'
            ]
            hub.light_matrix.start_animation(anim_countdown, 10, False, 'fade out', True)

        :param animation: The animation to be played. Animation should be composed of multiple strings separated by
        commas. Each string consists of 5 groups of 5 numbers from 0 to 9 separated by ':'. Each group of 5 numbers
        represents a line of pixels of the light matrix with the first number of the first group representing the first
        left pixel of the first top line and the value representing the brightness 0 being off and 9 being 100%
        brightness.
        :param fps: The speed at which the animation is played, i.e. animation frames displayed per second.
        :param loop: Whether or not the animation should loop.
        :param effect: The effect that is applied to the animation.
        :param clear: Whether or not the animation should clear the display upon completion.
        """
        assert 1 <= fps <= 20
        assert isinstance(loop, bool)
        assert effect in ['direct', 'overlay', 'slide right', 'slide left', 'fade in', 'fade out']
        assert isinstance(clear, bool)

    def _perform_animation(self, *args, **kwargs):
        pass

    def set_orientation(self, orientation: str = 'upright'):
        """Sets the orientation of the light matrix.Sets the orientation of the light matrix.

        Examples:

            from mindstorms import MSHub

            hub = MSHub()

            hub.light_matrix.write('LEGO')
            hub.light_matrix.set_orientation('upside down')
            hub.light_matrix.write('MINDSTORMS')

        :param orientation: The orientation the light matrix will be oriented towards.
        """
        assert orientation in ['upright', 'left', 'upside down', 'right']

    def rotate(self, direction: str = 'clockwise'):
        """Rotates the light matrix to the select directionRotates the light matrix to the select direction

        Examples:

            from mindstorms import MSHub

            hub = MSHub()

            hub.light_matrix.write('LEGO')
            hub.light_matrix.rotate('counterclockwise')
            hub.light_matrix.write('MINDSTORMS')

        :param direction: The direction set light matrix will be rotated. Rotating four times will put the light matrix
        in the same orientation it was before the rotations.
        """
        assert direction in ['clockwise', 'counterclockwise']

    def get_orientation(self):
        """Gets the orientation of the light matrix.
        Examples:

            from mindstorms import MSHub

            hub = MSHub()

            hub.light_matrix.set_orientation("right")
            orientation = hub.light_matrix.get_orientation()
            print(orientation)
        """
        pass
