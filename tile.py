class Tile:
    pos_x = 0
    pos_y = 0
    nearby_mines = 0
    has_mine = False
    flag_type = 0
    is_revealed = False

    def __init__(self, x_value=0, y_value=0):
        self.pos_x = x_value
        self.pos_y = y_value

    def setPosX(self, x_value):
        self.pos_x = x_value

    def getPosX(self):
        return self.pos_x

    def setPosY(self, y_value):
        self.pos_y = y_value

    def getPosY(self):
        return self.pos_y

    def setNearbyMines(self, numMines):
        self.nearby_mines = numMines

    def getNearbyMines(self):
        return self.nearby_mines

    def addNearbyMine(self):
        self.nearby_mines += 1

    #alias for getFlagType()
    #will evaluate as False if 0 and True otherwise
    def isFlagged(self):
        return self.flag_type

    #behaves just like setFlagType(0)
    def removeFlag(self):
        self.flag_type = 0

    def getFlagType(self):
        return self.flag_type

    def setFlagType(self, typeInt):
        self.flag_type = int(typeInt)

    def hasMine(self):
        return self.has_mine

    def addMine(self):
        self.has_mine = True

    def removeMine(self):
        self.has_mine = False

    def isRevealed(self):
        return self.is_revealed

    def reveal(self):
        self.removeFlag()
        self.is_revealed = True

    def hide(self):
        self.is_revealed = False

    def adjacents(self):
        x, y = self.pos_x, self.pos_y

        adj = [
            (x, y - 1), (x, y + 1),
            (x - 1, y), (x - 1, y - 1), (x - 1, y + 1),
            (x + 1, y), (x + 1, y - 1), (x + 1, y + 1)
        ]

        return adj

    def explode():
        return 94

    def toTextTile(self):
        contents = " "

        if self.flag_type:
            if self.flag_type == 1:
                contents = "F"
            else:
                contents = "f"

        if self.is_revealed:
            if self.getNearbyMines:
                contents = "{0}".format(self.getNearbyMines())

            if self.has_mine:
                contents = "*"

        return "[{0}]".format(contents)

    def __str__(self):
        strPos = "Position: ({0},{1}). ".format(self.pos_x, self.pos_y)
        strNear = "{0} nearby mines. \n".format(self.nearby_mines)

        strTile = strPos + strNear
        baseLength = len(strTile)

        if self.has_mine:
            strTile += "Contains mine. "
        if self.flag_type:
            strTile += "Marked with flag #{0}. ".format(self.flag_type)
        if self.is_revealed:
            strTile += "Already revealed."

        if len(strTile) > baseLength:
            strTile += "\n"

        return strTile


