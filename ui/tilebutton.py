from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.clock import Clock

from functools import partial

from ui.menu import FlagMenu


class TileButton(Button):

    tile = ObjectProperty()

    def update(self):
        self.text = self.tile.toTextTile()
        self.self = self.tile.isRevealed()

    def explode(self):
        self.parent.explode()

    def clickTile(self):

        self.parent.revealTile(self.tile)

        if self.tile.hasMine():
            self.explode()

        self.parent.updateBoard()

    def menu(self, touch, *args):
        self.add_widget(FlagMenu(center=touch.pos))

    def scheduleMenu(self):
        touch = self.last_touch
        callback = partial(self.menu, touch)
        touch.ud['event'] = Clock.schedule_once(callback, .5)

    def unscheduleMenu(self):
        touch = self.last_touch
        Clock.unschedule(touch.ud['event'])

    #on_press = clickTile
    on_press = scheduleMenu
    on_release = unscheduleMenu
