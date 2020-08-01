class LineParser:
    def parse_line(self, line):
        """
        parse_line --> Parses the input line into the kingdom part
        and message part

        Since there are some cases where the message can be split by
        spaces this is made into a new parser

        :param line: [description]
        :type line: [type]
        :return: [description]
        :rtype: [type]
        """
        if line == "" or line == []:
            return None, None
        kingdom, *message = line.split()
        message = (
            "".join(message) if isinstance(message, list) else message
        )
        return kingdom, message
