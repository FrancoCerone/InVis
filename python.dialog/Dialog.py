from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.graphics.instructions import InstructionGroup
from kivy.graphics import Color, Rectangle

from kivy.lib.osc import oscAPI
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import MetricsBase
from kivy.config import Config
from kivy.uix.image import Image


class FlashWidget(Widget):
    def add_rectangele(self, color):
        with self.canvas:
            blue = InstructionGroup()
            blue.add(color)
            Rectangle(pos=(0, 0), size=(13660, 7680))
            


class MyPaintApp(App):
    _color = Color(1, 1, 1)
    _isRunning = True
    im = Image()
    im=Image(source="a.gif", anim_delay=0.1, pos=(0, 0),size=(800, 600))
    
    def build(self):
        #Window.size = (1366, 768)
        oscAPI.init()
        oscid = oscAPI.listen(ipAddr='localhost', port=57110) # per elektroWave WiFi: 192.168.0.12
        oscAPI.bind(oscid, self.elaborate_osculator_message, '/toFlash')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        oscAPI.bind(oscid, self.set_color, '/toSelectColor')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        #oscAPI.bind(oscid, self.set_runnable, '/setRunnable')
        #Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        oscAPI.bind(oscid, self.set_Image, '/toSetImage')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        self._parent = Widget()
        self.painter = FlashWidget()
        
        self._parent.add_widget(self.painter)
        self.im.keep_ratio= False
        self.im.allow_stretch = True
        self._parent.add_widget(self.im)
        #_parent.remove_widget(self.im)  #questo funziona qua ma non nel metodo
        return self._parent
    

    def clear_canvas1(self, obj):
        self.painter.canvas.clear()
    
    
    def set_Image(self, message, *args):
        print "setting image:" + message[2]
        im=Image(source=message[2]+ ".gif", anim_delay=0.05, pos=(0, 0),size=(800, 600) )
        self._parent.remove_widget(self.im)
        #self.remove_widget(self.im)
        #self.im.keep_ratio= False
        #self.im.allow_stretch = True
        #_parent.add_widget(im)

    
    def elaborate_osculator_message(self, message, *args):
        if MyPaintApp._isRunning == True:
            if MyPaintApp._color is None:
                self.painter.add_rectangele(Color(1., 1., 1.))
            else:
                print "da elaborate"
                print MyPaintApp._color
                self.painter.add_rectangele(MyPaintApp._color)
            Clock.schedule_once(self.clear_canvas1, 0.1)
            print("Messaggio: %s" % message)

    def set_color(self, message, *args):
        MyPaintApp._color = Color( message[2], message[3], message[4])
    
    def set_runnable(self, message, *args):
        if message[2] == True:
            MyPaintApp._isRunning = True
        else:
            MyPaintApp._isRunning = False

if __name__ == '__main__':
    MyPaintApp().run()