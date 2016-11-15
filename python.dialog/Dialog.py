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


class MyPaintWidget(Widget):
    
    
    def add_rectangele(self, color):
        #self.color = Color(1., 1., 1.)
        color
        with self.canvas:
            Rectangle(pos=(0, 0), size=(13660, 7680))

   

class MyPaintApp(App):
    _color = None
    def build(self):
        
        # Window.size = (1366, 768)
        oscAPI.init()
        oscid = oscAPI.listen(ipAddr='192.168.0.12', port=57110) # here I put my internal IP
        oscAPI.bind(oscid, self.elaborate_osculator_message, '/toFlash')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        oscAPI.bind(oscid, self.elaborate_osculator_message, '/toSelectColor')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        parent = Widget()
        self.painter = MyPaintWidget()
        parent.add_widget(self.painter)
        return parent
    

    def clear_canvas1(self, obj):
        self.painter.canvas.clear()
    
    def elaborate_osculator_message(self, message, *args):
        if MyPaintApp._color is None:
            self.painter.add_rectangele(Color(1., 1., 1.))
        else:
            self.painter.add_rectangele(MyPaintApp._color)
        Clock.schedule_once(self.clear_canvas1, 0.1)
        print("Messaggio: %s" % message)


if __name__ == '__main__':
    MyPaintApp().run()