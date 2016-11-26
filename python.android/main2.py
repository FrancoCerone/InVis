'''
Audio example
=============

This example plays sounds of different formats. You should see a grid of
buttons labelled with filenames. Clicking on the buttons will play, or
restart, each sound. Not all sound formats will play on all platforms.

All the sounds are from the http://woolyss.com/chipmusic-samples.php
"THE FREESOUND PROJECT", Under Creative Commons Sampling Plus 1.0 License.

'''

import kivy
kivy.require('1.0.8')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from glob import glob
from os.path import dirname, join, basename
from kivy.lib.osc import oscAPI
import os


class ImageButton(Button):
    filename = StringProperty(None)
    def on_press(self):
        print os.path.basename(self.filename)
        oscAPI.init()
        oscAPI.sendMsg('/toSetImage', dataArray=[os.path.basename(self.filename)], ipAddr='localhost', port=57110)
        

class AudioBackground(BoxLayout):
    pass


class ControllerApp(App):

    def build(self):
        root = AudioBackground(spacing=5)
        
        path = os.path.dirname(__file__) + "/resources/"
        for fn in glob(join(dirname(path ), '*.*')):
            btn = ImageButton(
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
    ControllerApp().run()
