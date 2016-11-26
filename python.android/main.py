import kivy
kivy.require('1.0.8')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty, NumericProperty
from glob import glob
from os.path import dirname, join, basename
from kivy.lib.osc import oscAPI
import os


class FlashButton(Button):

    filename = StringProperty(None)
    sound = ObjectProperty(None, allownone=True)
    volume = NumericProperty(1.0)

    def on_press(self):
        print os.path.basename(self.filename)
        oscAPI.init()
        oscAPI.sendMsg('/toSetImage', dataArray=[os.path.basename(self.filename)], ipAddr='localhost', port=57110)

   


class AudioBackground(BoxLayout):
    pass


class AudioApp(App):

    def build(self):

        root = AudioBackground(spacing=5)
        
        path = os.path.dirname(__file__) + "/resources/"
        for fn in glob(join(dirname(path ), '*.*')):
            btn = FlashButton(
                text=basename(fn[:-4]).replace('_', ' '), filename=fn,
                size_hint=(None, None), halign='center',
                size=(128, 128), text_size=(118, None))
            root.ids.sl.add_widget(btn)

        return root


    def release_audio(self):
        for audiobutton in self.root.ids.sl.children:
            audiobutton.release_audio()

    def set_volume(self, value):
        for audiobutton in self.root.ids.sl.children:
            audiobutton.set_volume(value)

if __name__ == '__main__':
    AudioApp().run()
