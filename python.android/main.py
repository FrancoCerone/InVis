import kivy
kivy.require('1.0.8')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty, NumericProperty
from kivy.lib.osc import oscAPI
import os


oscAPI.init()

class Constants():
    ip = "localhost"
    #ip = "192.168.1.101" #ElektroWave Wifi
    flashOnLabel = "Flash On"
    flashOffLabel = "Flash Off"
 

class FlashHandler():
    _isFlashRunning = True

class AudioButton(Button):
    flashBt = ObjectProperty(None, allownone=True)
    filename = StringProperty(None)
    sound = ObjectProperty(None, allownone=True)
    volume = NumericProperty(1.0)
    def on_press(self):
        oscAPI.sendMsg('/toSetImage', dataArray=[os.path.basename(self.filename)], ipAddr=Constants.ip, port=57110)
        FlashHandler._isFlashRunning = False
        self.flashBt.text = Constants.flashOnLabel
        

class ColorButton(Button):
    btncolor = StringProperty(None)
    def on_press(self):
        r = ControllerApp.get_Red(self.btncolor)
        g = ControllerApp.get_Green(self.btncolor)
        b = ControllerApp.get_Blue(self.btncolor)
        print r,g,b
        if FlashHandler._isFlashRunning == True:
            oscAPI.sendMsg('/toSetColor', dataArray=[r,g,b], ipAddr=Constants.ip, port=57110)
        else:
            oscAPI.sendMsg('/toOneShotFlash', dataArray=[r,g,b], ipAddr=Constants.ip, port=57110)
            

        

class FlashButton(Button):
    def on_press(self):
        if FlashHandler._isFlashRunning == True:
            runFlash = False
            self.text = "Flash on"
        else:
            runFlash = True
            self.text = "Flash off"
        oscAPI.sendMsg('/toSetFlashRunnable', dataArray=[runFlash], ipAddr=Constants.ip, port=57110)
        FlashHandler._isFlashRunning = runFlash
        

                 
        
class AudioBackground(BoxLayout):
    pass

class AudioBackground2(BoxLayout):
    pass


class ControllerApp(App):
    
    @staticmethod 
    def get_Red(rgbString):
        return rgbString[0:3]
    @staticmethod 
    def get_Green(rgbString):
        return rgbString[3:6]
    @staticmethod 
    def get_Blue(rgbString):
        return rgbString[6:9]
    
    gifMap = { 
        "a.gif" : "a.gif",
        "b.gif" : "b.gif",
        "c.gif" : "c.gif",
        }
    
    colorMap = {
        "blue" :  "  0  0  1",
        "red" :   "  1  0  0",
        "green" : "  0  1  0",
        "white" : ".99.99.99",
        "yellow" :".93.99.09",
        "purple" :".99  0.83",
        }

    def build(self):

        root = AudioBackground(spacing=5)
        
        flashBt = FlashButton(
            text=Constants.flashOffLabel,
            size_hint=(1, 1), 
            )
        
        
        for fn in self.gifMap:
            btn = AudioButton(
                flashBt = flashBt,
                filename=fn,
                background_normal = "resources/" + fn[:-4] + ".png",
                size_hint=(None, None), halign='center',
                size=(200, 200), text_size=(118, None))
            root.ids.sl.add_widget(btn)

        
        
        for color in self.colorMap:
            color2= self.colorMap.get(color)
            r = ControllerApp.get_Red( color2)
            g = ControllerApp.get_Green(color2)
            b = ControllerApp.get_Blue(color2)
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
