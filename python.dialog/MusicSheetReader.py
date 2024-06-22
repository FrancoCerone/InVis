from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.graphics.instructions import InstructionGroup
from oscpy.server import OSCThreadServer
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.config import Config
from ScreenResolution import ScreenResolution
from SpeedMaper import SpeedMapper
from KeepRatioOverwriter import KeepRatioOverwriter
from kivy.uix.image import AsyncImage
from kivy.loader import Loader
from kivy.lang import Builder
from oscpy.server import OSCThreadServer
from kivy.resources import resource_find
from kivy.properties import (
    NumericProperty, StringProperty, AliasProperty, ReferenceListProperty,
    ObjectProperty, ListProperty, DictProperty, BooleanProperty)
from kivy.uix.boxlayout import BoxLayout

# Config.set('graphics', 'fullscreen', 'auto')

screenResolution = ScreenResolution()
levels = []

class Network():
    # myIp = "192.168.1.100"
    myIp = "127.0.0.1"

class ImageWidget(Widget):
    texture = ObjectProperty(None)
    rect = None

    def setRatio(self, imageFileName, _im):
        if KeepRatioOverwriter.ratioOverwriterMap.get(imageFileName) is not None:
            _im.keep_ratio = KeepRatioOverwriter.ratioOverwriterMap.get(imageFileName)
        else:
            _im.keep_ratio = False

    def add_musicSheet(self, note):
        # Carica l'immagine
        def on_load(image):
            self.texture = image.texture
            with self.canvas:
                self.rect = Rectangle(texture=self.texture, pos=self.pos, size=self.size)
            self.update_rect()  # Aggiorna immediatamente la posizione e le dimensioni del rettangolo
        # Utilizza il loader per caricare l'immagine
        self.remove_Image()
        _im = Loader.image("resources/music_sheet/"+ str(note))
        _im.allow_stretch = False
        _im.keep_ratio = True  # Mantiene il rapporto di aspetto
        _im.bind(on_load=on_load)
        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, *args):
        if self.rect:
            self.rect.pos = self.pos
            self.rect.size = self.size

    def remove_Image(self):
        self.canvas.clear()

class InViS(App):
    screenResolution = ScreenResolution()

    def build(self):
        osc = OSCThreadServer()
        sock = osc.listen(address=Network.myIp, port=8000, default=True)

        self._parent = BoxLayout(orientation='vertical')  # Usa BoxLayout per il layout principale

        self.imageWidget = ImageWidget(size_hint=(1, 1))
        self._parent.add_widget(self.imageWidget)

        @osc.address(b'/Note1')
        def open_sheet_music(*args):
            self.imageWidget.add_musicSheet( args[0])
            

        return self._parent

    def remove_Image(self, message, *args):
        self.imageWidget.remove_Image()

if __name__ == '__main__':
    InViS().run()
