from typing import Optional, Iterable

PORTS: dict = None
MOTOR_TYPES: tuple = None

def sleep_ms(*args, **kwargs):
    pass


def _is_motor(*args, **kwargs):
    pass


def is_type(*args, **kwargs):
    pass


def newSensorDisconnectedError(*args, **kwargs):
    pass


def wait_for_async(*args, **kwargs):
    pass


def clamp_speed(*args, **kwargs):
    pass


def clamp_power(*args, **kwargs):
    pass


class Motor:
    """This is the Single Motor Library, you can use the following functions to rotate your motors or move them to a
    specific position. To use the motors, you must first initialize them.
    """

    BRAKE: str = 'brake'
    HOLD: str = 'hold'
    COAST: str = 'coast'

    def __init__(self, port: str, unknown=None):
        self._port: str = port
        self._default_speed: int = 75
        self._last_event = None
        self._motor_wrapper = None

    def start(self, speed: int):
        """Starts running the motor at the specified speed. The motor will keep on running until you give it another
        motor command or your program ends.

        Example:

            from mindstorms import MSHub, Motor

            hub = MSHub()
            motor_a = Motor('A')

            motor_a.start(60)
            # Press on the hub's left button when you want to stop the motor
            hub.left_button.wait_until_pressed()
            motor_a.stop()

        :param speed: The desired motor's speed. If no value is specified, the speed is set by `set_default_speed()` is used.
        """
        assert -100 <= speed <= 100

    def stop(self):
        """Stops the motor. What the motor does after it stops depends on the action sets in `set_stop_action()`.

        Example:
            from mindstorms import MSHub, Motor

            hub = MSHub()
            motor = Motor('A')

            motor.start()
            # Press on the Hub's left button when you want the motor to stop.
            hub.left_button.wait_until_pressed()
            motor.stop()
        """
        pass

    def run_for_degrees(self, degrees: int, speed: Optional[int] = None):
        """ Runs the motor for a specified number of degrees.

        Example

            from mindstorms import Motor

            motor_a = Motor('A')

            # Run the motor 90 degrees clockwise at 30% speed.
            motor_a.run_for_degrees(90, 30)
            # Run the motor 90 degrees counterclockwise at maximum (100%) speed.
            motor_a.run_for_degrees(-90, 100)
            # Run the motor 360 degrees clockwise at default speed.
            motor_a.run_for_degrees(360)

        :param degrees: The number of degrees the motor should run. F.ex 360 degrees makes the motor run a full rotation.
        :param speed: The desired motor's speed. If no value is specified, the speed is set by `set_default_speed()` is used.
        """
        if speed is not None:
            assert 0 <= speed <= 100

    def run_to_position(self, degrees: int, direction: str = 'shortest path', speed: int = None):
        """Runs the motor to an absolute position.Runs the motor to an absolute position.

        Example:

            from mindstorms import Motor

            motor_a = Motor('A')

            # Run the motor to position 0 degrees, aligning the markers.

            motor_a.run_to_position(175, 'clockwise', 75)
            # Run the motor to position 0 degrees, aligning the markers.
            motor_a.run_to_position(0)

        :param degrees: The new desired position.
        :param direction: The direction the motor should run. You can choose to rotate the motor in one direction or
        the other, or let the motor decide which direction makes its rotation shorter by choosing 'shortest path'
        :param speed: The desired motor's speed. If no value is specified, the speed set by `set_default_speed()` is
        used.
        """
        assert 0 <= degrees <= 359
        assert direction in ['shortest path', 'clockwise', 'counterclockwise']
        assert 0 <= speed <= 100

    def get_position(self) -> int:
        """Returns the actual absolute position of the motor.

        Example:

            from mindstorms import MSHub, Motor

            hub = MSHub()
            motor_a = Motor('A')

            motor_a.run_for_seconds(1, 100)
            hub.light_matrix.write('Position =')
            hub.light_matrix.write(motor_a.get_position())
            motor_a.stop()

        :return: The current motor's position.
        """
        pass

    def get_speed(self) -> int:
        """Returns the actual speed of the motor.

        Example:

            from mindstorms import MSHub, Motor

            hub = MSHub()
            motor_a = Motor('A')

            motor_a.start()
            hub.light_matrix.write('Speed =')
            hub.light_matrix.write(motor_a.get_speed())
            motor_a.stop()

        :return: The motor's current speed.
        """
        pass

    def get_degrees_counted(self) -> int:
        """Returns the motor's relative position of degrees counted. You can set the degrees counted by using
        `set_degrees_counted()`.

        Example:

            from mindstorms import MSHub, Motor

            hub = MSHub()
            motor_a = Motor('A')

            motor_a.run_for_seconds(1, 100)
            hub.light_matrix.write('degrees counted =')
            hub.light_matrix.write(motor_a.get_degrees_counted())
            motor_a.stop()

        :return: The motor's degrees counted position.
        """
        pass

    def set_degrees_counted(self, degrees_counted: int):
        """Sets the degrees counted to the desired count.

        :param degrees_counted: The new degrees counted count.
        """
        pass

    def get_default_speed(self) -> int:
        """Returns the default motor speed.

        Example:

            from mindstorms import MSHub, Motor

            hub = MSHub()
            motor_a = Motor('A')

            motor_a.set_default_speed(50)
            motor_a.run_for_rotations(1, 100)
            hub.light_matrix.write('default speed =')
            hub.light_matrix.write(motor_a.get_default_speed())

        :return: The default motor's speed.
        """

    def set_default_speed(self, default_speed: int):
        """Sets the default motor speed. This is the default speed value used by the other motor functions when
        you do not specify a speed value. Setting the default speed does not affect the actual motor speed.
        This function should be used before another function that runs motors.

        Example:

            from mindstorms import Motor
            from mindstorms.control import wait_for_seconds

            motor_a = Motor('A')


            motor_a.set_default_speed(30)
            # The motor start running for 2 seconds at the default speed (30%)
            motor_a.run_for_seconds(2)
            # The motor start running at 85 speed
            motor_a.start(85)
            # The default speed is changed to 20%, not the actual motor speed
            motor_a.set_default_speed(20)
            wait_for_seconds(2)
            motor_a.stop()

        :param default_speed: The desired default speed.
        """
        assert -100 <= default_speed <= 100

    def set_stop_action(self, action: Optional[str] = COAST):
        """Sets the default stop action the motor performs when it stops running. Setting the default stop action does
        not affect the actual motor stop action. This function should be used before other functions that run or stop
        motors.

        Example:

            from mindstorms import Motor

            motor_a = Motor('A')

            # The motor is free after it completely stops.
            motor_a.set_stop_action('coast')
            motor_a.run_for_seconds(1, 100)
            # The motor keeps braking after it completely stops.
            motor_a.set_stop_action('brake')
            motor_a.run_for_seconds(1, 100)
            # The motor holds its position after it completely stops.
            motor_a.set_stop_action('hold')
            motor_a.run_for_seconds(1, 100)

        :param action: The desired stop action.
        """
        assert action in (self.COAST, self.BRAKE, self.HOLD)

    def set_stall_detection(self, stop_when_stalled: Optional[bool] = True):
        """Turns the stall detection on or off. Stall detection senses when a motor has been blocked and can't move.
        If stall detection has been enabled and a motor is blocked, the motor will be powered off after two seconds and
        the current motor command will be interrupted. If stall detection has been disabled, the motor will keep trying
        to run and prgorams will "get stuck" until the motor is no longer blocked. Stall detection is enabled by
        default.

        Example:

            from mindstorms import Motor

            motor = Motor('A')

            motor.set_stall_detection(False)
            motor.run_for_rotations(2)
            # The program will never proceed to here if the motor is stalled.

        :param stop_when_stalled: Choose "True" to enable stall detection or "False" to disable it.
        """
        pass

    def run_to_degrees_counted(self, degrees: int, speed: Optional[int] = None):
        """ Runst hte motor to a relative position of degrees counted. You can set the degrees counted by using `set_degrees_counted()`.

        Example

            from mindstorms import Motor
            from mindstorms.control import wait_for_seconds

            motor_a = Motor('A')

            # Run the motor to 400 degrees counted at 50% speed.
            motor_a.run_to_degrees_counted(400, 50)
            # Run the motor to -600 degrees counted at maximum (100%) speed.
            motor_a.run_to_degrees_counted(-600, 100)
            # Comment 3
            motor_a.run_to_degrees_counted(0)

        :param degrees: The number of degrees the motor should run. F.ex 360 degrees makes the motor run a full rotation.
        :param speed: The desired motor's speed. If no value is specified, the speed is set by `set_default_speed()` is used.
        """
        if speed is not None:
            assert 0 <= speed <= 100

    def run_for_rotations(self, rotations: float, speed: Optional[int] = None):
        """Runs the motor for a specified number of rotations.

        Example

            from mindstorms import Motor

            motor_a = Motor('A')
            # Run the motor 0.25 rotations clockwise (90 degrees).
            motor_a.run_for_rotations(0.25, 90)
            # Run the motor 0.25 rotations counterclockwise (-90 degrees).
            motor_a.run_for_rotations(-0.25, 10)

        :param rotations: The number of rotations the motor should run.
        :param speed: The desired motor's speed. If no value is specified, the speed is set by `set_default_speed()` is used.
        """
        assert -100 <= speed <= 100

    def run_for_seconds(self, seconds: float, speed: int):
        """Runs the motor for a specified number of seconds.

        Example

            from mindstorms import Motor

            motor_a = Motor('A')
            # Run the motor clockwise for half a second at 75% speed.
            motor_a.run_for_seconds(0.5, 75)
            # Run the motor counterclockwise for 3 seconds at 30% speed.
            motor_a.run_for_seconds(3, -30)

        :param seconds: The number of seconds the motor should run.
        :param speed: The desired motor's speed. If no value is specified, the speed is set by `set_default_speed()` is used.
        """
        assert -100 <= speed <= 100

    def start_at_power(self, power: int):
        """Starts running the motor at the specified power level. The motor will keep on running until you give it
        another motor command or your program ends.

        :param power: The desired motor's power.
        """
        assert -100 <= power <= 100

    def was_interrupted(self) -> bool:
        """Checks if the last motor command was interrupted.

        Example

            from mindstorms import Motor

            motor = Motor('A')

            motor.run_for_rotations(2)
            if motor.was_interrupted():
            # The motor did not complete two rotations.
            print('interrupted')
        :return: True if the last motor command was interrupted, otherwise false.
        """
        pass

    def was_stalled(self) -> bool:
        """Checks if the motor was stalled.

        Example
            from mindstorms import MSHub, Motor

            hub = MSHub()
            motor_a = Motor('A')

            motor_a.set_stall_detection(True)
            motor_a.run_for_rotations(2)
            if motor_a.was_stalled():
            # The motor did not complete two rotations.
            hub.light_matrix.write('stalled')

        :return: True if the motor has stalled during its last command, otherwise false.
        """
        pass
