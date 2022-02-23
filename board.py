import numpy as np
from tile import Tile


class Board:

    num_rows = 0
    num_columns = 0
    num_mines = 0
    tile_grid = None

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

    def getTile(self, move):
        print(move.posX(), move.posY())
        return self.tile_grid[move.posX(), move.posY()]

    def updateSurroundingTiles(self, center_tile):
        for position in center_tile.adjacents():
            if -1 not in position:
                try:
                    self.tile_grid[position].addNearbyMine()
                except IndexError:
                    # if adjacent tile is outside the board
                    # skip it and move on
                    pass

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
