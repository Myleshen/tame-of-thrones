class Message:
    def __init__(self, currentLine):
        """
        __init__ --> Initializes Kingdom and Message Sent.

        :param currentLine: Kingdom_Name Message_to_Kingdom
        :type currentLine: [type]
        """
        self.kingdom, *self.message = currentLine.split()
        self.message = (
            "".join(self.message)
            if isinstance(self.message, list)
            else self.message
        )

    def _return_contents_as_string(self):
        return "Kingdom: " + self.kingdom + " Message: " + self.message
