_COLORMAP: dict = None


class StatusLight:
    """This is the status light component part of the hub, the following functions let you change the color of the
    status light (central button light ring).
    """

    def on(self, color: str = 'white'):
        """Sets the color of the status light.Sets the color of the status light.

        Example:

            from mindstorms import MSHub

            hub = MSHub()

            hub.status_light.on('blue')

        :param color: Illuminates the Hub’s Status Light in the specified color.
        """
        assert color in ['azure', 'black', 'blue', 'cyan', 'green', 'orange', 'pink', 'red', 'violet', 'white',
                         'yellow']

    def off(self):
        """Turns off the light.
        Example:

            from mindstorms import MSHub

            hub = MSHub()

            hub.status_light.off()
        """
        pass
