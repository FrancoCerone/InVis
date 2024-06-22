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
from kivy.properties import ( ObjectProperty)
from kivy.uix.boxlayout import BoxLayout

screenResolution = ScreenResolution()
levels = []

class Network():
    myIp = "127.0.0.1"

class ImageWidget(Widget):
    texture = ObjectProperty(None)
    rect = None
    _im = None  # Manteniamo il riferimento all'oggetto Image caricato

    def setRatio(self, imageFileName, _im):
        if KeepRatioOverwriter.ratioOverwriterMap.get(imageFileName) is not None:
            _im.keep_ratio = KeepRatioOverwriter.ratioOverwriterMap.get(imageFileName)
        else:
            _im.keep_ratio = False
            
    def add_musicSheet(self, note, imageWidget):
        if self._im:
           self._im.unbind(on_load=self.on_load)
           imageWidget._im = None
           imageWidget.texture =  ObjectProperty(None)
        
        self._im = Loader.image("resources/music_sheet/" + str(note), nocache=True)  # Force no cache
        self._im.allow_stretch = False
        self._im.keep_ratio = True  # Mantiene il rapporto di aspetto
        self._im.bind(on_load=self.on_load)
        self.bind(size=self.update_rect, pos=self.update_rect)

    def on_load(self, image):
        self.texture = image.texture
        self.canvas.clear()  # Pulisce la canvas prima di disegnare l'immagine
        with self.canvas:
            self.rect = Rectangle(texture=self.texture, pos=self.pos, size=self.size)
        self.update_rect()

    def update_rect(self, *args):
        if self.rect:
            self.rect.pos = self.pos
            self.rect.size = self.size




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
            self.imageWidget.add_musicSheet( args[0], self.imageWidget)

        return self._parent


if __name__ == '__main__':
    InViS().run()
