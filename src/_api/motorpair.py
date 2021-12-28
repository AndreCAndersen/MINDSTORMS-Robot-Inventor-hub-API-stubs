from typing import Optional

PORTS: dict = None
_DISCONNECTED_ERROR: RuntimeError = None
_MOTOR_PAIRING_ERROR: RuntimeError = None


def _is_motor(*args, **kwargs):
    pass


def wait_for_async(*args, **kwargs):
    pass


def clamp_speed(*args, **kwargs):
    pass


def clamp_power(*args, **kwargs):
    pass


def from_steering(*args, **kwargs):
    pass


def clamp_steering(*args, **kwargs):
    pass


class MotorPair:
    IN: str = 'in'
    BRAKE: str = 'brake'
    HOLD: str = 'hold'
    CM: str = 'cm'
    COAST: str = 'coast'
    ROTATIONS: str = 'rotations'
    DEGREES: str = 'degrees'
    SECONDS: str = 'seconds'

    def __init__(self, port1: str, port2: str):
        """This is the Motor Pair Library, you can use the functions here to control 2 motors simultaneously in
        opposite directions. To be able to use a Motor Pair, you must initialize both motors.

        :param port1:
        :param port2:
        """
        pass

    def start(self, steering: Optional[int] = 0, speed: Optional[int] = None):
        """Starts both motors simultaneously to move a Driving Base. The motor will keep moving at the specified
        speed until you give them another command or when your program ends.

        Example:

            from mindstorms import MSHub, MotorPair

            motor_pair = MotorPair('B', 'A')

            motor_pair.start(-100, 30)
            # Press on the Hub's right button when you want the motors to stop.
            hub.right_button.wait_until_pressed()
            motor_pair.stop()

        :param steering:
        :param speed:
        """
        assert -100 <= steering <= 100
        if speed is not None:
            assert -100 <= speed <= 100

    def stop(self):
        """Stops both motors simultaneously, which will stop a Driving Base. What the motors do after they stop
        depends on the action sets in `set_stop_action()`.

        Examples:

            from mindstorms import MSHub, MotorPair

            motor_pair = MotorPair('B', 'A')

            motor_pair.start(-100, 30)
            # Press on the Hub's right button when you want the motors to stop.
            hub.right_button.wait_until_pressed()
            motor_pair.stop()
        """
        pass

    def move(self, amount: float, unit: Optional[str] = CM, steering: Optional[int] = 0, speed: Optional[int] = None):
        """Runs both motors simultaneously to move a Driving Base.

        Example:

            from mindstorms import MotorPair

            motor_pair = MotorPair('B', 'A')

            motor_pair.move(4, 'cm', 0, 50)
            motor_pair.move(2, 'rotations', steering=100)
            motor_pair.move(3, 'seconds', steering=-100, 100)

        :param amount: The amount of movement in relation to the specified unit. Negative value move the Driving
        Base Backward instead of forward.
        :param unit: The unit of measurement. When unit is specified as 'cm' or 'in', the amount parameter represents
        horizontal distance the Driving Base must travel. The relationship between the motor rotations and distance
        traveled can be adjusted using the function `set_motor_rotation()`. When unit is specified as 'rotations' or
        'degrees', the amount parameter represents how many rotations or degrees the motor must rotate. When unit is
        specified as 'seconds', the amount parameter represents the duration the motors must run.
        :param steering: The direction the Driving Base is steering. The default value steers the Driving Base streight.
        Negative value steers the Driving Base to the left and positive values to the right. Minimum and maximum value
        makes the Driving Base spin on itself.
        :param speed: The desired motors speed. Negative value moves the Driving Base backward instead of forward.
        If no value is specified, the speed set by `set_default_speed()`is used.
        """
        if unit is not None:
            assert unit in (self.CM, self.IN, self.ROTATIONS, self.DEGREES, self.SECONDS)
        assert -100 <= steering <= 100
        if speed is not None:
            assert -100 <= speed <= 100

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

    def move_tank(self, amount: float, unit: Optional[str] = CM, left_speed: Optional[int] = None, right_speed: Optional[int] = None):
        """ Move the Driving Base using differential (tank) steering. The speed of each motor can be controlled independently.

        Example:

            from mindstorms import MotorPair

            motor_pair = MotorPair('B', 'A')
            motor_pair.move_tank(10, 'cm', 25, 75)

        :param amount: The amount of movement in relation to the specified unit. Negative value moves the Driving
        Base backward instead of forward.
        :param unit: The unit of measurement. When unit is specified as 'cm' or 'in', the amount parameter represents
        horizontal distance the Driving Base must travel. The relationship between the motor rotations and distance
        traveled can be adjusted using the function `set_motor_rotation()`. When unit is specified as 'rotations' or
        'degrees', the amount parameter represents how many rotations or degrees the motor must rotate. When unit is
        specified as 'seconds', the amount parameter represents the duration the motors must run.
        :param left_speed: The left motor's desired speed. Negative value makes the left motor run backward. If no
        value is specified, the default speed set by `set_default_speed()` is used.
        :param right_speed: The right motor's desired speed. Negative value makes the right motor run backward. If no
        value is specified, the default speed set by `set_default_speed()` is used.
        """
        if unit is not None:
            assert unit in (self.CM, self.IN, self.ROTATIONS, self.DEGREES, self.SECONDS)
        if left_speed is not None:
            assert -100 <= left_speed <= 100
        if right_speed is not None:
            assert -100 <= right_speed <= 100

    def start_tank(self, *args, **kwargs):
        pass

    def start_tank_at_power(self, *args, **kwargs):
        pass
