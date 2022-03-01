from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

from parts.board import Board


class BoardFrame(GridLayout):

    board = ObjectProperty()

    def __init__(self, x, y, **kwargs):
        super(BoardFrame, self).__init__(**kwargs)
        self.board = Board(x, y).placeMines()

    def update(self):
        for tilebtn in self.children:
            tilebtn.update()

    def explode(self):
        self.board.revealAll()

    def revealTile(self, tile):
        self.board.revealTile(tile)
