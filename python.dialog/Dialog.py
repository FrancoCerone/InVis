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
from kivy.properties import ObjectProperty

class ScreenResolution():
    width = 1280
    height = 720

class Network():
    #ip = '192.168.1.101' #ElektroWave WiFi
    ip = 'localhost'
    
#class Helper():
   # print "Start Gif Loading"
   # gifMap = { 
   #     "a.gif" : Image(source="resources/a.gif", anim_delay=0.1, pos=(0, 0), size=(ScreenResolution.width, ScreenResolution.height), keep_data = True),
   #     "b.gif" : Image(source="resources/b.gif", anim_delay=0.1, pos=(0, 0), size=(ScreenResolution.width, ScreenResolution.height), keep_data = True),
   #     "c.gif" : Image(source="resources/c.gif", anim_delay=0.1, pos=(0, 0), size=(ScreenResolution.width, ScreenResolution.height), keep_data = True),
   #     }
   # print "Gif Loaded"
    
    

class FlashWidget(Widget):
    def add_rectangele(self, color):
        with self.canvas:
            blue = InstructionGroup()
            blue.add(color)
            Rectangle(pos=(0, 0), size=(ScreenResolution.width, ScreenResolution.height))

class ImageWidget(Widget):
    

  
    def add_Image(self, imageFileName):
        with self.canvas:
            self.canvas.clear()
            _im = Image(source="resources/"+ imageFileName, anim_delay=0.1, pos=(0, 0), size=(ScreenResolution.width, ScreenResolution.height), keep_data = True)
            _im.keep_ratio= False
            _im.allow_stretch = True
    
    def remove_Image(self):
        self.canvas.clear()
             
             


class MyPaintApp(App):
    _color = Color(1, 1, 1)
    _isFlashRunning = True
    
    
    def build(self):
        #Window.size = (1366, 768)
        oscAPI.init()
        oscid = oscAPI.listen(ipAddr=Network.ip, port=57110) # per elektroWave WiFi: 192.168.0.12
        oscAPI.bind(oscid, self.automatic_flash, '/toFlash')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        oscAPI.bind(oscid, self.one_shot_flash, '/toOneShotFlash')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        oscAPI.bind(oscid, self.set_color, '/toSetColor')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        oscAPI.bind(oscid, self.set_Image, '/toSetImage')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        oscAPI.bind(oscid, self.remove_Image, '/toClearImage')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        oscAPI.bind(oscid, self.set_Runnuble, '/toSetFlashRunnable')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        self._parent = Widget()
        
        self.flashWidget = FlashWidget()
        self._parent.add_widget(self.flashWidget)
        
        self.imageWidget = ImageWidget()
        self._parent.add_widget(self.imageWidget)
        
        #_parent.remove_widget(self.im)  #questo funziona qua ma non nel metodo
        return self._parent
    

    def clear_canvas1(self, obj):
        self.flashWidget.canvas.clear()
    
    
    def set_Image(self, message, *args):
        MyPaintApp._isFlashRunning = False
        self.imageWidget.add_Image( message[2])
        
    def set_Runnuble(self, message, *args):
        if message[2] == 1:
            MyPaintApp._isFlashRunning = True
            self.imageWidget.remove_Image()
        else:
            MyPaintApp._isFlashRunning = False
                
    def remove_Image(self, message, *args):
        self.imageWidget.remove_Image()
        
        
        
    def one_shot_flash(self, message, *args):
            self.imageWidget.remove_Image() #Forse rallenta il flash, trovare il modo per farlo una volta sola
            self.flashWidget.add_rectangele(Color( message[2], message[3], message[4]))
            Clock.schedule_once(self.clear_canvas1, 0.1)
        
    
    def automatic_flash(self, message, *args):
        if MyPaintApp._isFlashRunning == True:
            if MyPaintApp._color is None:
                self.flashWidget.add_rectangele(Color(1., 1., 1.))
            else:
                self.imageWidget.remove_Image() #Forse rallenta il flash, trovare il modo per farlo una volta sola
                self.flashWidget.add_rectangele(MyPaintApp._color)
            Clock.schedule_once(self.clear_canvas1, 0.1)

    def set_color(self, message, *args):
        print message[2], message[3], message[4]
        MyPaintApp._color = Color( message[2], message[3], message[4])
    
    def set_runnable(self, message, *args):
        if message[2] == True:
            MyPaintApp._isFlashRunning = True
        else:
            MyPaintApp._isFlashRunning = False

if __name__ == '__main__':
    MyPaintApp().run()