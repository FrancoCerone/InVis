import kivy
kivy.require('1.0.8')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty, NumericProperty
from kivy.lib.osc import oscAPI
from os.path import basename
import os


oscAPI.init()

class Network():
    ip = "localhost"
    flashOnLabel = "Flash On"
    flashOffLabel = "Flash Off"
 

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

class ColorButton(Button):
    btncolor = StringProperty(None)
    def on_press(self):
        r = self.btncolor[0:2]
        g = self.btncolor[2:4]
        b = self.btncolor[4:6]
        print [r,g,b]
        oscAPI.sendMsg('/toSetColor', dataArray=[r,g,b], ipAddr=Network.ip, port=57110)
        print "premuto"

        

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
    
    colorMap = {
        "blue" :  " 0 0 1",
        "red" :   " 1 0 0",
        "green" : " 0 1 0",
        "white" :" 1 1 1",
          
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
        
        
        for color in self.colorMap:
            color2= self.colorMap.get(color)
            r = color2[0:2]
            g = color2[2:4]
            b = color2[4:6]
            btn = ColorButton(
                btncolor = self.colorMap.get(color),
                background_color=(r, g, b, 1),
                size_hint=(None, None), halign='center',
                size=(128, 128), text_size=(118, None)
                )
            root.ids.sl2.add_widget(btn)
        
        root.ids.flashButton.add_widget(flashBt)


        print root.ids.sl2.size
        
        
   
        return root



if __name__ == '__main__':
    ControllerApp().run()
