from kivy.app import App

from ui.boardframe import BoardFrame
from ui.tilebutton import TileButton

DEMO_X = 4
DEMO_Y = 4


class SweepApp(App):

    def build(self):

        self.root = BoardFrame(DEMO_X, DEMO_Y, cols=DEMO_X)

        for tile in self.root.board.tileList():
            tileBtn = TileButton(text=tile.toTextTile(), tile=tile)
            self.root.add_widget(tileBtn)


if __name__ == '__main__':
    SweepApp().run()
