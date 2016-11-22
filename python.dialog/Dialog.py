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


class MyPaintWidget(Widget):
    
    def add_rectangele(self, color):
        
        with self.canvas:
            blue = InstructionGroup()
            blue.add(color)
            Rectangle(pos=(0, 0), size=(13660, 7680))
   

class MyPaintApp(App):
    _color = Color(1, 1, 1)
    _isRunning = True
    
    im = Image(source='3.gif', anim_delay=0.05, pos=(0, 0),size=(400, 400) )
    def build(self):
        #im = setImage('3.gif')
        # Window.size = (1366, 768)
        oscAPI.init()
        oscid = oscAPI.listen(ipAddr='localhost', port=57110) # per elektroWave WiFi: 192.168.0.12
        oscAPI.bind(oscid, self.elaborate_osculator_message, '/toFlash')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        oscAPI.bind(oscid, self.set_color, '/toSelectColor')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        #oscAPI.bind(oscid, self.set_runnable, '/setRunnable')
        #Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        parent = Widget()
        self.painter = MyPaintWidget()
        parent.add_widget(self.painter)
        self.im.keep_ratio= False
        self.im.allow_stretch = True
        parent.add_widget(self.im)
        return parent
    

    def clear_canvas1(self, obj):
        self.painter.canvas.clear()
    
    
    #def setImage(imageName):
     #   im=Image(source='3.gif', anim_delay=0.05, pos=(0, 0),size=(400, 400) )
     #   return im
    
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