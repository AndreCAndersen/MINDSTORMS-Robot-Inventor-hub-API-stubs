
_SOUNDS_DIR: str = None


def wait_for_async(*args, **kwargs):
    pass


class Speaker:
    """This is the Speaker component part of the Hub, you can use the functions below to play beeps on the speaker and
    adjust the volume.
    """

    def __init__(self, *args, **kwargs):
        pass

    def beep(self, note: int = 60, seconds: float = 0.2, volume: int = None):  # note = 60 -> middle C note
        """Plays a beep on the Hub's speaker at the specified note. Your program will not continue until the specified
        number of seconds has elapsed.Plays a beep on the Hub's speaker at the specified note. Your program will not
        continue until the specified number of seconds has elapsed.

        Examples:

            from mindstorms import MSHub

            hub = MSHub()

            # beep beep beep!

            hub.speaker.beep(60, 0.5)
            hub.speaker.beep(44, 0.5, 50)
            hub.speaker.beep(123, 0.5, 100)

        :param note: The MIDI note number.
        :param seconds: The duration of the beep in seconds.
        :param volume: The volume at which the sound will be played. Type: integer or float (positive or negative
        number, including 0). Values: 0 to 100% or None. Default: None (indicating that current volume is used).
        """
        assert 44 <= note <= 123
        assert 0 <= volume <= 100

    def stop(self):
        """Stops any sound that is playing on the Hub's Speaker.
        Examples:

            from mindstorms import MSHub

            hub = MSHub()

            hub.speaker.start_beep()
            # Put your own code here
            hub.speaker.stop()
        """
        pass

    def get_volume(self):
        """Returns the value of the hub's Speaker volume.
        Examples:

            from mindstorms import MSHub

            hub = MSHub()
            # Increase the volume of the Hub speaker by 10%.
            hub.speaker.set_volume(hub.speaker.get_volume() + 10)
        """
        pass

    def set_volume(self, volume: int = 100):
        """Sets the Hub's Speaker volume. Not your device volumeSets the Hub's Speaker volume. Not your device volume

        Examples:

            from mindstorms import MSHub

            hub = MSHub()
            # Set the Hub speaker volume to 50%.
            hub.speaker.set_volume(50)

        :param volume: The new volume in percent. If the specified volume is out of range, the nearest volume (i.e., 0
        or 100) will be used instead.
        """
        assert 0 <= volume <= 100

    def start_beep(self, note: int = 60, volume: int = None):
        """Starts playing a beep on the Hub's Speaker at the specified note. The beep will play until stop() is called
        or another beep is played on the Speaker.Starts playing a beep on the Hub's Speaker at the specified note. The
        beep will play until stop() is called or another beep is played on the Speaker.

        Examples:

            from mindstorms import MSHub

            hub = MSHub()

            #Beep high-pitched for 3 seconds
            hub.speaker.start_beep(123, 100)
            wait_for_seconds(3)
            hub.speaker.stop()

        :param note: The MIDI note number.
        :param volume: The volume at which the sound will be played.
        """
        assert 44 <= note <= 123
        assert 0 <= volume <= 100

    def play_sound(self, name: str, volume: int):
        """Plays a sound from the hub speaker.
        The program will not continue until the sound has finished playing.Plays a sound from the hub speaker.
        The program will not continue until the sound has finished playing.

        Examples:

            from mindstorms import MSHub

            hub = MSHub()

            # Play the 'Damage' sound and wait for it to finish
            hub.speaker.play_sound('Damage')

        :param name: Name of the sound to play on Hub.
        :param volume: The volume at which the sound will be played.
        """
        assert name in ['1234', 'Activate', 'Affirmative', 'Bowling', 'Brick Eating', 'Celebrate', 'Chuckle',
                        'Countdown', 'Countdown Tick', 'Damage', 'Deactivate', 'Delivery', 'Dizzy', 'Error',
                        'Explosion', 'Exterminate', 'Fire', 'Goal', 'Goodbye', 'Grab', 'Hammer', 'Hello', 'Hi', 'Hi 5',
                        'Hit', 'Horn', 'Humming', 'Hydraulics Down', 'Hydraulics Up', 'Initialize', 'Kick', 'Laser',
                        'Laugh', 'Like', 'Mission Accomplished', 'No', 'Ouch', 'Ping', 'Play', 'Punch', 'Reverse',
                        'Revving', 'Sad', 'Scanning', 'Scared', 'Seek and Destroy', 'Shake', 'Shooting', 'Shut Down',
                        'Slam Dunk', 'Strike', 'Success Chime', 'Tadaa', 'Target Acquired', 'Target Destroyed', 'Whirl',
                        'Wow', 'Yes', 'Yipee', 'Yuck']
        assert 0 <= volume <= 100

    def start_sound(self, name: str, volume: int):
        """Starts playing a sound from the Hub speaker.

        The program will not wait for the sound to finish playing before proceeding to the next command.Starts playing
        a sound from the Hub speaker.

        The program will not wait for the sound to finish playing before proceeding to the next command.

        Examples:

            from mindstorms import MSHub

            hub = MSHub()

            # Play the 'Damage' sound and wait for it to finish
            hub.speaker.play_sound('Damage')

        :param name: Name of the sound to play on Hub.
        :param volume: The volume at which the sound will be played.
        """
        assert name in ['1234', 'Activate', 'Affirmative', 'Bowling', 'Brick Eating', 'Celebrate', 'Chuckle',
                        'Countdown', 'Countdown Tick', 'Damage', 'Deactivate', 'Delivery', 'Dizzy', 'Error',
                        'Explosion', 'Exterminate', 'Fire', 'Goal', 'Goodbye', 'Grab', 'Hammer', 'Hello', 'Hi', 'Hi 5',
                        'Hit', 'Horn', 'Humming', 'Hydraulics Down', 'Hydraulics Up', 'Initialize', 'Kick', 'Laser',
                        'Laugh', 'Like', 'Mission Accomplished', 'No', 'Ouch', 'Ping', 'Play', 'Punch', 'Reverse',
                        'Revving', 'Sad', 'Scanning', 'Scared', 'Seek and Destroy', 'Shake', 'Shooting', 'Shut Down',
                        'Slam Dunk', 'Strike', 'Success Chime', 'Tadaa', 'Target Acquired', 'Target Destroyed', 'Whirl',
                        'Wow', 'Yes', 'Yipee', 'Yuck']
        assert 0 <= volume <= 100


class SpeakerSoundProvider:

    def get_canonical_name(self, *args, **kwargs):
        pass

    def get_sound_files(self, *args, **kwargs):
        pass
