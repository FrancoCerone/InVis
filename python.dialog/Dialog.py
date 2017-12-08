
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.graphics.instructions import InstructionGroup
from kivy.lib.osc import oscAPI
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.config import Config
from ScreenResolution import ScreenResolution
from SpeedMaper import SpeedMapper
from KeepRatioOverwriter import KeepRatioOverwriter
from pong import PongGame
from kivy.uix.image import AsyncImage
from kivy.loader import Loader
#Config.set('graphics', 'fullscreen', 'auto')



screenResolution = ScreenResolution()


def get_ip_address():
    ip = '192.168.1.102'
    #ip = 'localhost'
    return ip 


def get_PiIp_address():
    ip = '192.168.1.103'
    return ip 

def get_SecondIp_address():
    ip = '192.168.1.101'
    return ip 

def get_sedond_port():
    port = '57200'
    #ip = 'localhost'
    return port 

class Network():
    myIp = get_ip_address()
    piIp = get_PiIp_address()
    secondIp = get_SecondIp_address()
    secondPort= get_sedond_port()

class ObjectToFlash():
    isColor= True
    color = Color(1, 1, 1)
    pngToFlash= ""

class ModalityList():
    resist = 'resist'
    gif = 'gif'
    midi = 'midi'
    manual = 'manual'
    modalities = (resist, gif, midi, manual)

class FlashWidget(Widget):
    def add_rectangele(self, color):
        with self.canvas:
            blue = InstructionGroup()
            blue.add(color)
            Rectangle(pos=(0, 0), size=(screenResolution.get_width(), screenResolution.get_height()))

class ImageWidget(Widget):

    def setRatio(self, imageFileName, _im):
        if (KeepRatioOverwriter.ratioOverwriterMap.get(imageFileName) != None):
            _im.keep_ratio = KeepRatioOverwriter.ratioOverwriterMap.get(imageFileName)
            print "Overwrite keep ratio for:  " + imageFileName + " in " + str(KeepRatioOverwriter.ratioOverwriterMap.get(imageFileName))
        else:
            _im.keep_ratio = False

    def add_gif(self, imageFileName):
        with self.canvas:
            self.canvas.clear()
            fileType="zip"
            fileFolder =fileType+"s"
            print "loading file: "+ "resources/"+fileFolder+"/"+ imageFileName + "."+fileType
            gifSpeed = 0.05
            if(SpeedMapper.speedMap.get(imageFileName)!= None):
                gifSpeed = SpeedMapper.speedMap.get(imageFileName)
                print "Overwrite seep for:  "+imageFileName
            _im = Image(source="resources/"+fileFolder+"/"+ imageFileName + "."+fileType, anim_delay=float(gifSpeed), pos=(0, 0) )
            _im.keep_data = True
            self.setRatio(imageFileName, _im)
            _im.allow_stretch = True
            _im.size =screenResolution.get_width(), screenResolution.get_height()
    def add_png(self, imageFileName):
        with self.canvas:
            self.canvas.clear()
            _im = Image(source="resources/pngs/"+ imageFileName + ".png", anim_delay=0.2, pos=(0, 0), keep_data = True)
            _im.keep_data = True
            self.setRatio(imageFileName, _im)
            _im.allow_stretch = True
            _im.size =screenResolution.get_width(), screenResolution.get_height()
    def remove_Image(self):
        self.canvas.clear()

class UserAnimation(PongGame):
    pass
    

class MyPaintApp(App):
    _objToFlash= ObjectToFlash()
    _objectToFlash = Color(1, 1, 1)
    _modality = ModalityList.resist
    
    
    def build(self):
        
        oscAPI.init()
        oscid = oscAPI.listen(ipAddr=Network.myIp, port=57110)

        oscAPI.bind(oscid, self.to_flash, '/toFlash')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        oscAPI.bind(oscid, self.one_shot_flash, '/toOneShotFlash')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        oscAPI.bind(oscid, self.set_object_to_flash, '/toSetObjectToShow')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        oscAPI.bind(oscid, self.set_gif, '/toSetGif')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        oscAPI.bind(oscid, self.set_png, '/toSetPng')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        oscAPI.bind(oscid, self.set_Modality, '/toSetModality')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        oscAPI.bind(oscid, self.set_UserAnimation, '/toStartUserAnimation')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
         
        oscAPI.bind(oscid, self.set_status_Musk, '/toSetMusk');
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        self._parent = Widget()
        
        self.flashWidget = FlashWidget()
        self._parent.add_widget(self.flashWidget)
        
        self.imageWidget = ImageWidget()
        self._parent.add_widget(self.imageWidget)
        
        self.game = PongGame()
        self._parent.add_widget(self.game)
        Clock.schedule_interval(self.game.update, 0)
        
        return self._parent
    

    def clear_canvas1(self, obj):
        self.flashWidget.set_top(100)
        self.flashWidget.canvas.clear() 
    
    
    def set_gif(self, message, *args):
        print message[0]
        print message[2]
        print Network.secondIp
        print Network.secondPort
        oscAPI.sendMsg('/toSetGif', dataArray=[message[2]], ipAddr=Network.secondIp , port=57200)
        MyPaintApp._lastGif =  message[2]
        if MyPaintApp._modality ==  ModalityList.resist:
            self.imageWidget.add_png( message[2]) 
        elif MyPaintApp._modality ==  ModalityList.manual:
            self.imageWidget.add_png( message[2])
            Clock.schedule_once(self.remove_Image, 0.2  )
        else:
            self.imageWidget.add_gif(  MyPaintApp._lastGif)
        #oscAPI.sendMsg(message[0], dataArray=[ message[2] ] , ipAddr="123.123.123.123", port=111)
        
    def set_png(self, message, *args):
        self.flashWidget.canvas.clear()
        self.imageWidget.add_png( message[2])
        if MyPaintApp._modality  !=  ModalityList.resist:
            Clock.schedule_once(self.remove_Image, 0.2  )
        
    def set_Modality(self, message, *args):
        MyPaintApp._modality = ModalityList.modalities.__getitem__(message[2])
            
    def set_UserAnimation(self, message, *args):
        self.game.add_animation(message[2], message[3] )
        if(MyPaintApp._modality == ModalityList.gif ):
            self.imageWidget.add_gif(  MyPaintApp._lastGif)
       
    def set_status_Musk(self, message, *args):
        print "arrivato il messsagio"
        print "parametro1", message[2]
        print Network.piIp
        oscAPI.sendMsg('/toSetStatus', dataArray=[message[2]], ipAddr=Network.piIp , port=57120)
        
    def remove_Image(self, message, *args):
        self.imageWidget.remove_Image()
        
        
        
    def one_shot_flash(self, message, *args):
        self.imageWidget.remove_Image() #Forse rallenta il flash, trovare il modo per farlo una volta sola
        self.flashWidget.add_rectangele(Color( message[2], message[3], message[4]))
        if MyPaintApp._modality !=  ModalityList.resist:
            Clock.schedule_once(self.clear_canvas1, 0.3)
        

    def to_flash(self, message, *args):
        oscAPI.sendMsg('/toFlash', dataArray=[message[0], message[2] ] , ipAddr='192.168.1.103', port=57120)
        if MyPaintApp._modality == ModalityList.midi:
            self.imageWidget.remove_Image() #Forse rallenta il flash, trovare il modo per farlo una volta sola
            if (MyPaintApp._objToFlash.isColor):
                self.flashWidget.add_rectangele(MyPaintApp._objectToFlash)
            else:
                self.imageWidget.add_png(MyPaintApp._objToFlash.pngToFlash)
                Clock.schedule_once(self.remove_Image, 0.25)
                
            Clock.schedule_once(self.clear_canvas1, 0.25)

    def set_object_to_flash(self, message, *args):
        if(len(message)==3):
            MyPaintApp._objToFlash.isColor= False
            MyPaintApp._objToFlash.pngToFlash = message[2]
        else:
            MyPaintApp._objectToFlash = Color( message[2], message[3], message[4])
            MyPaintApp._objToFlash.isColor= True
            MyPaintApp._objToFlash.color = Color( message[2], message[3], message[4])
   
    
if __name__ == '__main__':
    MyPaintApp().run()
