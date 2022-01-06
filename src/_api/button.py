class Button:
    """This is the buttons components part of the Hub. The functions below use the state of the left or right button,
    meaning whether they are pressed or not. You can use these functions to control the flow of your program. To select
    one button or the other you have to use the attribute `.left_button` or `.right_button`.
    """

    def wait_until_pressed(self):
        """Waits until the button is pressed.
        Example:

            from mindstorms import MSHub

            hub = MSHub()
            # Beep every time the Left Button is pressed.
            while True:
                hub.left_button.wait_until_pressed()
                hub.speaker.start_beep()
                hub.left_button.wait_until_released()
                hub.speaker.stop()
        """
        pass

    def wait_until_released(self):
        """Waits until the button is released.
        Example:

            from mindstorms import MSHub

            hub = MSHub()
            # Beep every time the Left Button is pressed.
            while True:
                hub.left_button.wait_until_pressed()
                hub.speaker.start_beep()
                hub.left_button.wait_until_released()
                hub.speaker.stop()
        """
        pass

    def was_pressed(self):
        """Checks if the button was pressed.
        Example:

            from mindstorms import MSHub
            from mindstorms.control import wait_for_seconds

            hub = MSHub()

            while True:
                wait_for_seconds(3)
                if hub.left_button.was_pressed():
                    # Put your own code here
                    hub.speaker.beep()
        """
        pass

    def is_pressed(self):
        """Checks if the button is pressed.
        Example:

            from mindstorms import MSHub

            hub = MSHub()

            if hub.left_button.is_pressed():
                # Do something.
                    hub.speaker.beep()
        """
        pass

    def is_released(self):
        """Checks if the button is released.
        Example:

            from mindstorms import MSHub

            hub = MSHub()

            if hub.left_button.is_released():
               # Beep if left button is released
               hub.speaker.beep()
        """
        pass
