import numpy as np
from parts.tile import Tile


class Board:

    num_rows = 0
    num_columns = 0
    num_mines = 0
    tile_grid = None
    safe_tiles = 0

    def __init__(self, rows=0, columns=0):
        self.num_rows = rows
        self.num_columns = columns
        self.num_mines = int((rows + columns) / 2)

        self.tile_grid = np.empty((rows, columns), object)

        for y in range(rows):
            for x in range(columns):
                self.tile_grid[x, y] = Tile(x, y)

        self.safe_tiles = self.tile_grid.size - self.num_mines

    def shape(self):
        return (self.num_rows, self.num_columns)

    def size(self):
        return self.tile_grid.size

    def tiles(self):
        return self.tile_grid

    def tileList(self):
        tiles = []
        for row in self.tile_grid:
            for tile in row:
                tiles.append(tile)
        return tiles

    def rows(self):
        return self.num_rows

    def cols(self):
        return self.num_columns

    def tilesLeft(self):
        return self.safe_tiles

    def setTilesLeft(self, numTiles):
        self.safe_tiles = numTiles

    def getTile(self, move):
        #print("x", move.posX(),"y", move.posY(), flush=True)
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

    def revealSurroundingTiles(self, center_tile):
        for position in center_tile.adjacents():
            if -1 not in position:
                try:
                    self.revealTile(self.tile_grid[position])
                except IndexError:
                    # if adjacent tile is outside the board
                    # skip it and move on
                    pass

    def placeMines(self):
        placed = 0
        #rng = np.random.default_rng(803)
        rng = np.random.default_rng()
        while placed < self.num_mines:
            i = rng.integers(low=0, high=self.num_columns, size=1)
            j = rng.integers(low=0, high=self.num_rows, size=1)
            candidate = self.tile_grid[i, j][0]
            if not(candidate.hasMine()):
                candidate.addMine()
                self.updateSurroundingTiles(candidate)
                placed += 1
        return self

    def revealTile(self, tile, force=False):
        if not tile.isRevealed():
            if (not tile.isFlagged()) | force:
                tile.reveal()
                self.safe_tiles -= 1
                if tile.getNearbyMines() == 0:
                    self.revealSurroundingTiles(tile)

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
            print(self.solution())

    def revealAll(self):
        for row in self.tile_grid:
            for tile in row:
                tile.reveal()

    def forceVictory(self):
        for row in self.tile_grid:
            for tile in row:
                if not tile.hasMine():
                    self.revealTile(tile)

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
