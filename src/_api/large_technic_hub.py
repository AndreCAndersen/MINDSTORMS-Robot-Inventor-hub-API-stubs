from _api import LightMatrix, StatusLight, Button, MotionSensor, Speaker


class LargeTechnicHub:
    PORT_A: str = None
    PORT_B: str = None
    PORT_C: str = None
    PORT_D: str = None
    PORT_E: str = None
    PORT_F: str = None

    _light_matrix: LightMatrix = None
    _status_light: StatusLight = None
    _left_button: Button = None
    _right_button: Button = None
    _motion_sensor: MotionSensor = None
    _speaker: Speaker = None

    @property
    def speaker(self) -> Speaker:
        pass

    @property
    def light_matrix(self) -> LightMatrix:
        pass

    @property
    def status_light(self) -> StatusLight:
        pass

    @property
    def left_button(self) -> Button:
        pass

    @property
    def right_button(self) -> Button:
        pass

    @property
    def motion_sensor(self) -> MotionSensor:
        pass
