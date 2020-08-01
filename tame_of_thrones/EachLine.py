class EachLine:
    def parse_line(self, line):
        kingdom, *message = line.split()
        message = (
            "".join(message) if isinstance(message, list) else message
        )
        return kingdom, message
