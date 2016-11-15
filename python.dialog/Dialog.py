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
    
    def add_rectangele(self):
        with self.canvas:
            Color(1., 1., 1.)
            Rectangle(pos=(0, 0), size=(13660, 7680))

   

class MyPaintApp(App):
    
    def build(self):
        
        # Window.size = (1366, 768)
        oscAPI.init()
        oscid = oscAPI.listen(ipAddr='localhost', port=57110) # here I put my internal IP
        oscAPI.bind(oscid, self.elaborate_osculator_message, '/toDialog')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        parent = Widget()
        self.painter = MyPaintWidget()
        parent.add_widget(self.painter)
        return parent
    

    def clear_canvas1(self, obj):
        self.painter.canvas.clear()
    
    def elaborate_osculator_message(self, message, *args):
        
        
        self.painter.add_rectangele()
        Clock.schedule_once(self.clear_canvas1, 0.1)
        print("Messaggio: %s" % message)


if __name__ == '__main__':
    MyPaintApp().run()