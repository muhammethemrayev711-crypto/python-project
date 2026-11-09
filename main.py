# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.config import Config

from ui import MusicPanel


Config.set("graphics", "width", "300")
Config.set("graphics", "height", "600")


class MusicAssistant(App):

    def build(self):

        return MusicPanel()



if __name__ == "__main__":

    MusicAssistant().run()