
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.graphics.instructions import InstructionGroup
from kivy.lib.osc import oscAPI
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.config import Config
from ScreenResolution import ScreenResolution
from pong import PongGame
#Config.set('graphics', 'fullscreen', 'auto')


#import pyglet

screenResolution = ScreenResolution()


def get_ip_address():
    #s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #s.connect(('192.0.0.8', 1027))
    #ip = s.getsockname()[0]
   
    #ip = '192.168.1.102'
    #ip = '192.168.0.6'
    ip = 'localhost'
    return ip 

class Network():
    ip = get_ip_address()

class FlashWidget(Widget):
    def add_rectangele(self, color):
        with self.canvas:
            blue = InstructionGroup()
            blue.add(color)
            Rectangle(pos=(0, 0), size=(screenResolution.get_width(), screenResolution.get_height()))

class ImageWidget(Widget):
    def add_gif(self, imageFileName):
        with self.canvas:
            self.canvas.clear()
            fileType="zip"
            fileFolder =fileType+"s"
            print "loading file: "+ "resources/"+fileFolder+"/"+ imageFileName + "."+fileType
            _im = Image(source="resources/"+fileFolder+"/"+ imageFileName + "."+fileType, anim_delay=0.04, pos=(0, 0))
            _im.keep_data = True
            _im.keep_ratio= False
            _im.allow_stretch = True
            _im.size =screenResolution.get_width(), screenResolution.get_height()
    def add_png(self, imageFileName):
        with self.canvas:
            self.canvas.clear()
            _im = Image(source="resources/pngs/"+ imageFileName + ".png", anim_delay=0.1, pos=(0, 0), keep_data = True)
            _im.keep_ratio= False
            _im.allow_stretch = True
            _im.size =screenResolution.get_width(), screenResolution.get_height()
    def remove_Image(self):
        self.canvas.clear()

class UserAnimation(PongGame):
    pass

class MyPaintApp(App):
    #Window.borderless = True
    #Window.fullscreen = True
    _color = Color(1, 1, 1)
    _isFlashRunning = False
    _isRersistable = True
    _modality=0
    
    
    def build(self):
        oscAPI.init()
        oscid = oscAPI.listen(ipAddr=Network.ip, port=57110) # per elektroWave WiFi: 192.168.0.12

        oscAPI.bind(oscid, self.to_flash, '/toFlash')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        oscAPI.bind(oscid, self.one_shot_flash, '/toOneShotFlash')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        oscAPI.bind(oscid, self.set_color, '/toSetColor')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        oscAPI.bind(oscid, self.set_gif, '/toSetGif')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        oscAPI.bind(oscid, self.set_png, '/toSetPng')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        oscAPI.bind(oscid, self.set_Modality, '/toSetModality')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        oscAPI.bind(oscid, self.set_UserAnimation, '/toStartUserAnimation')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        self._parent = Widget()
        
        self.flashWidget = FlashWidget()
        self._parent.add_widget(self.flashWidget)
        
        self.imageWidget = ImageWidget()
        self._parent.add_widget(self.imageWidget)
        
        self.game = PongGame()
        self._parent.add_widget(self.game)
        Clock.schedule_interval(self.game.update, 0.2)
        
        #_parent.remove_widget(self.im)  #questo funziona qua ma non nel metodo
        return self._parent
    

    def clear_canvas1(self, obj):
        self.flashWidget.canvas.clear() 
    
    
    def set_gif(self, message, *args):
        MyPaintApp._isFlashRunning = False
        self.imageWidget.add_gif( message[2])
        
        
    def set_png(self, message, *args):
        self.flashWidget.canvas.clear()
        self.imageWidget.add_png( message[2])
        if MyPaintApp._isRersistable == False:
            Clock.schedule_once(self.remove_Image, 0.1)
        
    def set_Modality(self, message, *args):
        MyPaintApp._modality = message[2]
        if message[2] == 0:
            MyPaintApp._isFlashRunning = False
            MyPaintApp._isRersistable = True
            self.imageWidget.remove_Image()
        elif message[2] == 1:
            MyPaintApp._isFlashRunning = True
            MyPaintApp._isRersistable = False
        elif message[2] == 2:
            MyPaintApp._isFlashRunning = False
            MyPaintApp._isRersistable = False
            
    def set_UserAnimation(self, message, *args):
        self.game.add_animation()
       
    
                
    def remove_Image(self, message, *args):
        self.imageWidget.remove_Image()
        
        
        
    def one_shot_flash(self, message, *args):
        self.imageWidget.remove_Image() #Forse rallenta il flash, trovare il modo per farlo una volta sola
        self.flashWidget.add_rectangele(Color( message[2], message[3], message[4]))
        if MyPaintApp._isRersistable == False:
            Clock.schedule_once(self.clear_canvas1, 0.1)
        
    
    def to_flash(self, message, *args):
        if MyPaintApp._isFlashRunning == True:
            if MyPaintApp._color is None:
                self.flashWidget.add_rectangele(Color(1., 1., 1.))
            else:
                self.imageWidget.remove_Image() #Forse rallenta il flash, trovare il modo per farlo una volta sola
                self.flashWidget.add_rectangele(MyPaintApp._color)
            Clock.schedule_once(self.clear_canvas1, 0.1)

    def set_color(self, message, *args):
        MyPaintApp._isFlashRunning = True
        MyPaintApp._color = Color( message[2], message[3], message[4])
    
    def set_runnable(self, message, *args):
        if message[2] == True:
            MyPaintApp._isFlashRunning = True
        else:
            MyPaintApp._isFlashRunning = False

if __name__ == '__main__':
    MyPaintApp().run()
