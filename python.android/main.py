import kivy
kivy.require('1.0.8')

from kivy.app import App
from kivy.uix.button import Button
from kivy.properties import StringProperty, ObjectProperty, NumericProperty
from kivy.lib.osc import oscAPI
#from plyer import camera #object to read the camera
#from plyer import Camera
import os
oscAPI.init()
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.lang import Builder

Builder.load_string("""
<MainScreen>:
    BoxLayout:
        orientation: 'vertical'
        
        BoxLayout:
            
            orientation: 'horizontal'
            BoxLayout:
                StackLayout:
                    id: giffButtonContainer
           
            BoxLayout:
                StackLayout:
                    id: colorButtonContainer
        BoxLayout:
            orientation: 'vertical'   
            size_hint: 1, 0.25
            BoxLayout:
                GridLayout:
                    cols: 3
                    rows: 1
                    canvas:
                        Color:
                            rgb: 0.5,0.5,0.5
                        Rectangle:
                            pos: self.pos
                            size: self.size
                    orientation:'horizontal'
                    id: modalityContainer
            BoxLayout:
                orientation: 'horizontal'
                Button:
                    text: '<- Settings'
                    on_press: 
                        root.manager.transition.direction = 'right'
                        root.manager.current = 'settings'
                    
                Button:
                    text: 'Camera ->'
                    on_press: 
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'camera'
                
<CameraScreen>:
    BoxLayout:
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text: '<- Back to home'
                on_press: 
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'main'
                
            Button:
                text: 'Settings ->'
                on_press: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'settings'
<SettingsScreen>:
    BoxLayout:
        orientation: 'horizontal'
        AnchorLayout:
            anchor_x: 'left'
            anchor_y: 'top'
            AnchorLayout:
                anchor_x: 'right'
                anchor_y: 'top'
                GridLayout:
                    cols: 2
                    rows: 2
                    Label:
                        text: "Ip to:"
                        color: (1, 1, 1, .8)
                        size_hint: None, None
                        height: sp(30)
                    TextInput:
                        id: ipAdressText
                        text: 'bo'
                        multiline: False
                        write_tab: False    
                        size_hint: None, None
                        height: sp(30)
                        width: sp(300)
        Button:
            id: backHomeButton
            text: 'Back Home ->'
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'main' 
                        
""")





class MainScreen(Screen):
    pass

class CameraScreen(Screen):
    pass

class SettingsScreen(Screen):
    def getIp(self):
        return str(self.ids.ipAdressText.text)
    def setIp(self, ip):
        self.ids.ipAdressText.text = ip
    
    def saveIp(self):
        fob = open('properties.txt','w')
        fob.write(str(settingScreen.ids.ipAdressText.text))
        fob.close()


    
    pass

sm = ScreenManager()
menuScreen = MainScreen(name='main')
sm.add_widget(menuScreen)
# later
cameraScreen = CameraScreen(name='camera')
sm.add_widget(cameraScreen)

settingScreen = SettingsScreen(name='settings')
settingScreen.ids.backHomeButton.bind(on_press = SettingsScreen.saveIp)
sm.add_widget(settingScreen)

#sm.switch_to(cameraScreen, direction='right')



class Constants():
    resistMode = "Resist Mode"
    automaticMode = "Auto Mode"
    manualMode = "Manual Mode"
    
    
 

class ModalityHandler():
    modalities = ('resist', 'auto', 'manual')


class GifImageButton(Button):
    #flashBt = ObjectProperty(None, allownone=True)
    filename = StringProperty(None)
    sound = ObjectProperty(None, allownone=True)
    volume = NumericProperty(1.0)
    def on_press(self):
        print "send to " + SettingsScreen.getIp(settingScreen)
        print os.path.basename(self.filename)
        if ControllerApp._modality== 1:
            oscAPI.sendMsg('/toSetGif', dataArray=[os.path.basename(self.filename)], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)
        else: 
            oscAPI.sendMsg('/toSetPng', dataArray=[os.path.basename(self.filename)], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)          

class ColorButton(Button):
    btncolor = StringProperty(None)
    def on_press(self):
        r = ControllerApp.get_Red(self.btncolor)
        g = ControllerApp.get_Green(self.btncolor)
        b = ControllerApp.get_Blue(self.btncolor)
        print r,g,b
        if ControllerApp._modality== 1:
            oscAPI.sendMsg('/toSetColor', dataArray=[r,g,b], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)
        else:
            print SettingsScreen.getIp(settingScreen) 
            oscAPI.sendMsg('/toOneShotFlash', dataArray=[r,g,b], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)
            


class ResistModality(Button):
    def on_press(self):
        self.background_color =  [0.2, 0.3, 0.2, 1]
        ButtonModalityHandler.manualBnt.background_color =  [0.9, 0.9, 0.9, 1]
        ButtonModalityHandler.automaticBnt.background_color =  [0.9, 0.9, 0.9, 1]
        oscAPI.sendMsg('/toSetModality',dataArray=[ModalityHandler.modalities.index("resist", ) ], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)
        ControllerApp._modality = ModalityHandler.modalities.index("resist", )

class AutomaticModality(Button):
    def on_press(self):
        self.background_color =  [0.2, 0.3, 0.2, 1]
        ButtonModalityHandler.manualBnt.background_color =  [0.9, 0.9, 0.9, 1]
        ButtonModalityHandler.resisthBnt.background_color = [0.9, 0.9, 0.9, 1]
        self.text = Constants.automaticMode
        oscAPI.sendMsg('/toSetModality', dataArray=[ModalityHandler.modalities.index("auto", ) ], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)
        ControllerApp._modality = ModalityHandler.modalities.index("auto", )
        
class ManualModality(Button):
    def on_press(self):
        self.background_color =  [0.2, 0.3, 0.2, 1]
        ButtonModalityHandler.resisthBnt.background_color =  [0.9, 0.9, 0.9, 1]
        ButtonModalityHandler.automaticBnt.background_color =  [0.9, 0.9, 0.9, 1]
        oscAPI.sendMsg('/toSetModality', dataArray=[ModalityHandler.modalities.index("manual", ) ], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)
        ControllerApp._modality = ModalityHandler.modalities.index("manual", )
        

class ButtonModalityHandler():
    resisthBnt = ResistModality(
            text=Constants.resistMode,
            size_hint=(1, 1), 
            background_color =  [0.2, 0.3, 0.2, 1]
            )

    automaticBnt = AutomaticModality(
            text=Constants.automaticMode,
            size_hint=(1, 1), 
            )
    
    manualBnt = ManualModality(
            text=Constants.manualMode,
            size_hint=(1, 1), 
            )
    



class ControllerApp(App):
    _modality=0
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
        "a" : "a.gif",
        "b" : "b.gif",
        "c" : "c.gif",
        "d" : "d.gif",
        "e" : "e.gif",
        "f" : "f.gif",
        "g" : "g.gif",
        "h" : "h.gif"
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
        textfile = open('properties.txt', 'r') 
        ipFromTxt = textfile.read()
        print ipFromTxt
        SettingsScreen.setIp(settingScreen, ipFromTxt)

        

        
        for fn in self.gifMap:
            btn = GifImageButton(
                #flashBt = flashBt,
                filename=fn,
                background_normal = "resources/" + fn + ".png",
                size_hint=(None, None), halign='center',
                size=(200, 200), text_size=(118, None))
            menuScreen.ids.giffButtonContainer.add_widget(btn)

        
        
        for color in self.colorMap:
            color2= self.colorMap.get(color)
            r = ControllerApp.get_Red( color2)
            g = ControllerApp.get_Green(color2)
            b = ControllerApp.get_Blue(color2)
            btn = ColorButton(
                btncolor = self.colorMap.get(color),
                background_color=(r, g, b, 1),
                size_hint=(None, None), halign='center',
                size=(200, 200), text_size=(118, None)
                )
            menuScreen.ids.colorButtonContainer.add_widget(btn)
        
        menuScreen.ids.modalityContainer.add_widget(ButtonModalityHandler.resisthBnt)
        menuScreen.ids.modalityContainer.add_widget(ButtonModalityHandler.automaticBnt)
        menuScreen.ids.modalityContainer.add_widget(ButtonModalityHandler.manualBnt) 
                                                    

        return sm



if __name__ == '__main__':
    ControllerApp().run()
