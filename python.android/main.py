import kivy
kivy.require('1.0.8')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty, NumericProperty
from kivy.lib.osc import oscAPI
from os.path import basename
import os
from kivy.uix.slider import Slider 
from kivy.graphics import Rectangle, Color

oscAPI.init()

class Network():
    ip = "localhost"
    flashOnLabel = "Flash On"
    flashOffLabel = "Flash Off"
class ColorHelper():
    slider_colors = [1, 1, 1]    

class FlashHandler():
    _isFlashRunning = True

class AudioButton(Button):
    filename = StringProperty(None)
    sound = ObjectProperty(None, allownone=True)
    volume = NumericProperty(1.0)
    def on_press(self):
        print os.path.basename(self.filename)
        oscAPI.sendMsg('/toSetImage', dataArray=[os.path.basename(self.filename)], ipAddr=Network.ip, port=57110)
        FlashHandler._isFlashRunning = False


class FlashButton(Button):
    def on_press(self):
        if FlashHandler._isFlashRunning == True:
            runFlash = False
            self.text = "Flash on"
        else:
            runFlash = True
            self.text = "Flash off"
        oscAPI.sendMsg('/toSetFlashRunnable', dataArray=[runFlash], ipAddr=Network.ip, port=57110)
        FlashHandler._isFlashRunning = runFlash
        
class ColorSlider3(Slider):
    def on_touch_up(self, touch):
        if touch.grab_current == self:
            ColorHelper.slider_colors[2] = self.value/100
            with self.canvas.before:
                Color(ColorHelper.slider_colors[0],ColorHelper.slider_colors[1],ColorHelper.slider_colors[2])
                Rectangle(pos=(0, 0), size=(self.size))
    def on_touch_move(self, touch):
        if touch.grab_current == self:
            ColorHelper.slider_colors[2] = self.value/100
            with self.canvas.before:
                Color(ColorHelper.slider_colors[0],ColorHelper.slider_colors[1],ColorHelper.slider_colors[2])
                Rectangle(pos=(0, 0), size=(self.size))
            print "on touch move"
            return Slider.on_touch_move(self, touch)
                      
class ColorSlider1(Slider):
    def on_touch_up(self, touch):
        if touch.grab_current == self:
            ColorHelper.slider_colors[0] = self.value/100
            with self.canvas.before:
                print ColorHelper.slider_colors[0]
                Color(ColorHelper.slider_colors[0],ColorHelper.slider_colors[1],ColorHelper.slider_colors[2])
                Rectangle(pos=(0, 0), size=(self.size))
                 
class ColorSlider2(Slider):
    def on_touch_up(self, touch):
        if touch.grab_current == self:
            ColorHelper.slider_colors[1] = self.value/100
            with self.canvas.before:
                Color(ColorHelper.slider_colors[0],ColorHelper.slider_colors[1],ColorHelper.slider_colors[2])
                Rectangle(pos=(0, 0), size=(self.size))
    

        
class AudioBackground(BoxLayout):
    pass

class AudioBackground2(BoxLayout):
    pass


class ControllerApp(App):
    
    gifMap = { 
        "a.gif" : "a.gif",
        "b.gif" : "b.gif",
        "c.gif" : "c.gif",
        }

    def build(self):

        root = AudioBackground(spacing=5)
      
        
        for fn in self.gifMap:
            btn = AudioButton(
                text=basename(fn[:-4]).replace('_', ' '), filename=fn,
                size_hint=(None, None), halign='center',
                size=(128, 128), text_size=(118, None))
            root.ids.sl.add_widget(btn)
            
        flashBt = FlashButton(
            text=Network.flashOffLabel,
            size_hint=(.0, 1), 
             
            )
        root.ids.flashButton.add_widget(flashBt)
        
        s1 = ColorSlider1(
            size_hint=(1, 1), 
            min=0, 
            max=100, 
            value=ColorHelper.slider_colors[0]*100)
        s2 = ColorSlider2(
            min=0, 
            max=100, 
            value=ColorHelper.slider_colors[1]*100)
        s3 = ColorSlider3(
            min=0, 
            max=100, 
            value=ColorHelper.slider_colors[2]*100)
        root.ids.sl2.add_widget(s1)
        root.ids.sl2.add_widget(s2)
        root.ids.sl2.add_widget(s3)
        print root.ids.sl2.size
        
        
   
        return root



if __name__ == '__main__':
    ControllerApp().run()
