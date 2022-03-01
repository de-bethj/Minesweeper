from kivy.uix.boxlayout import BoxLayout


class ContextMenu(BoxLayout):
    pass


class FlagMenu(ContextMenu):

    def addFlag(self, flag):
        self.close_menu()

    def removeFlag(self, flag):
        self.close_menu()

    def close_menu(self, *args):
        self.parent.remove_widget(self)
