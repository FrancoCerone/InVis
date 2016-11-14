from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.graphics.instructions import InstructionGroup
from kivy.graphics import Color, Rectangle

from kivy.lib.osc import oscAPI
from kivy.clock import Clock


class MyPaintWidget(Widget):
    
    def add_rectangele(self):
        with self.canvas:
            Color(1., 0, 0)
            Rectangle(pos=(10, 10), size=(500, 500))

    def on_touch_down(self, touch):
        self.add_rectangele()
        
        color = (random(), 1, 1)
        with self.canvas:
            Color(*color, mode='hsv')
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class MyPaintApp(App):
    _i = 1;
    
      
        
    def build(self):
        oscAPI.init()
        oscid = oscAPI.listen(ipAddr='192.168.0.5', port=57110) # here I put my internal IP
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
        #self._i += 1  
        #print("Contatore: %s" % self._i )
        




if __name__ == '__main__':
    MyPaintApp().run()