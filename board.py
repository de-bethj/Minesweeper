import numpy as np
from tile import Tile


class Board:

    num_rows = 0
    num_columns = 0
    num_mines = 0
    #close enough. RTC correct method
    tile_grid = ""

    def __init__(self, rows=0, columns=0):
        self.num_rows = rows
        self.num_columns = columns
        self.num_mines = int((rows + columns) / 2)

        self.tile_grid = np.empty((rows, columns), object)

        for i in range(rows):
            for j in range(columns):
                self.tile_grid[i, j] = Tile(i, j)

    def size(self):
        return (self.num_rows, self.num_columns)

    def rows(self):
        return self.num_rows

    def cols(self):
        return self.num_columns

    def getTile(self, pos_x, pos_y, csInput=False):
        if not csInput:
            return self.tile_grid[pos_x - 1, pos_y - 1]
        return self.tile_grid[pos_x, pos_y]

    def updateSurroundingTiles(self, center_tile):
        for position in center_tile.adjacents():
            if -1 not in position:
                try:
                    self.tile_grid[position].addNearbyMine()
#                    print("added nearby mine to {0}".format(position))
                except IndexError:
                    pass
#                    print("index OB (probably caused by edges)")

    def placeMines(self):
        placed = 0
#        rng = np.random.default_rng(803)
        rng = np.random.default_rng()
        while placed < self.num_mines:
            i = rng.integers(low=0, high=self.num_columns, size=1)
            j = rng.integers(low=0, high=self.num_rows, size=1)
            candidate = self.tile_grid[i, j][0]
            if not(candidate.hasMine()):
                candidate.addMine()
                self.updateSurroundingTiles(candidate)
                placed += 1

    def display(self):
        for row in self.tile_grid:
            theRow = ""
            for tile in row:
                theRow += tile.toTextTile()
            print(theRow)

    def showSolution(self):
        for row in self.tile_grid:
            theRow = ""
            for tile in row:
                tile.reveal()
                theRow += tile.toTextTile()
            print(theRow)

    def hideAll(self):
        for row in self.tile_grid:
            theRow = ""
            for tile in row:
                tile.hide()
                theRow += tile.toTextTile()
            print(theRow)

    def explode(self, tile):
        if tile.hasMine():
            return 94
        return 0

    def __str__(self):

        strBoard = "{0} x {1} board containing {2} mines: \n".format(
            self.num_rows, self.num_columns, self.num_mines)

        strTiles = ""
        for row in self.tile_grid:
            for tile in row:
                strTiles += tile.toString()

        return strBoard + strTiles
