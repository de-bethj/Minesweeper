import re
from Error import NoSuchTileError

FORMAT = re.compile(r" *\d+ +\d+( F\d)? *")


class Move:
    raw = "0 0"
    pos_x = 0
    pos_y = 0
    flag = None

    def __init__(self, raw_str):
        self.raw = raw_str.upper()

    def posX(self):
        return self.pos_x

    def posY(self):
        return self.pos_y

    def getFlag(self):
        return self.flag

    def isValid(self):
        return FORMAT.fullmatch(self.raw.upper().strip())

    def parse(self, csInputs=False):

        def adjust(num, offset=1):
            num -= offset
            if num < 0:
                raise NoSuchTileError
            return num

        moveParts = self.raw.split(" ")
        x, y = moveParts[0], moveParts[1]
        self.pos_x, self.pos_y = int(x), int(y)

        if len(moveParts) > 2:
            f = moveParts[2].lstrip("Ff")
            self.flag = int(f)

        if not csInputs:
            self.pos_x = adjust(self.pos_x)
            self.pos_y = adjust(self.pos_y)

    def __str__(self):
        return self.raw
