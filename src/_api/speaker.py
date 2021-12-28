
_SOUNDS_DIR: str = None


def wait_for_async(*args, **kwargs):
    pass


class Speaker:

    def __init__(self, *args, **kwargs):
        pass

    def stop(self, *args, **kwargs):
        pass

    def beep(self, *args, **kwargs):
        pass

    def get_volume(self, *args, **kwargs):
        pass

    def set_volume(self, *args, **kwargs):
        pass

    def start_beep(self, *args, **kwargs):
        pass

    def play_sound(self, *args, **kwargs):
        pass

    def start_sound(self, *args, **kwargs):
        pass


class SpeakerSoundProvider:

    def get_canonical_name(self, *args, **kwargs):
        pass

    def get_sound_files(self, *args, **kwargs):
        pass
