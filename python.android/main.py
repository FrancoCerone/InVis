import kivy
kivy.require('1.0.8')

from kivy.app import App
from kivy.uix.button import Button
from kivy.properties import StringProperty, ObjectProperty, NumericProperty
from kivy.lib.osc import oscAPI
import os
oscAPI.init()
from kivy.uix.screenmanager import ScreenManager, Screen
from ButtonDimension import ButtonDimension
from main1 import Touchtracer

from kivy.lang import Builder

Builder.load_string("""
<MainScreen>:
    BoxLayout:
        orientation: 'vertical'
        
        BoxLayout:
            
            orientation: 'horizontal'
            ScrollView:
                size_hint: 3, 1
                GridLayout:
                    cols: 5
                    padding: 10
                    spacing: 10
                    size_hint: 0.9, 3
                    height: self.minimum_height
                    width: self.minimum_width
                    id: giffButtonContainer
           
            ScrollView:
                size_hint: 1, 1
                GridLayout:
                    cols: 2
                    padding: 10
                    spacing: 10
                    height: self.minimum_height
                    width: self.minimum_width
                    id: colorButtonContainer
        BoxLayout:
            orientation: 'vertical'   
            size_hint: 1, 0.25
            BoxLayout:
                GridLayout:
                    cols: 4
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
                    text: 'UserAnimation->'
                    on_press: 
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'userAnimation'
                
<UsersAnimation>:
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            FloatLayout:
                id: touchTracker
        BoxLayout:
            orientation: 'vertical'   
            size_hint: 1, 0.25
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
                id: modalityAnimationContainer
        BoxLayout:
            StackLayout:
                id: animationButtonContainer
            
        BoxLayout:
            orientation: 'vertical'   
            size_hint: 1, 0.25
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
        orientation: 'vertical'
       
        BoxLayout:
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
        BoxLayout:
            orientation: 'vertical'   
            size_hint: 1, 0.25
            
            BoxLayout:
                orientation: 'horizontal'
                Button:
                    text: '<- UserAnimation'
                    on_press: 
                        root.manager.transition.direction = 'right'
                        root.manager.current = 'userAnimation'
        
                Button:
                    id: backHomeButton
                    text: 'Back Home ->'
                    on_release:
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'main'
                        
""")

buttonDimension = ButtonDimension()

class MainScreen(Screen):
    pass

class UsersAnimation(Screen):
    map = {}
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
userAnimation = UsersAnimation(name='userAnimation')
sm.add_widget(userAnimation)

settingScreen = SettingsScreen(name='settings')
settingScreen.ids.backHomeButton.bind(on_press = SettingsScreen.saveIp)
sm.add_widget(settingScreen)

#sm.switch_to(cameraScreen, direction='right')



class Constants():
    resistMode = "Resist Mode"
    gifMode = "Gif Mode"
    midiMode = "Midi Mode"
    manualMode = "Manual Mode"
    
    
 

class AnimationModalityList():
    modalities = ('linear', 'random')


class ModalityList():
    resist = 'resist'
    gif = 'gif'
    midi = 'midi'
    manual = 'manual'
    modalities = (resist, gif, midi, manual)

class AnimationImageButton(Button):
    filename = StringProperty(None)
    def on_press(self):
        print "map:" , userAnimation.map
        print "send to " + SettingsScreen.getIp(settingScreen), ", Animation Modality: ",  ControllerApp._animation_modality,  ", image: ", os.path.basename(self.filename)
        oscAPI.sendMsg('/toStartUserAnimation', dataArray=[os.path.basename(self.filename), ControllerApp._animation_modality ], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)
        


class GifImageButton(Button):
    filename = StringProperty(None)
    def on_press(self):
        print "send to " + SettingsScreen.getIp(settingScreen)
        print os.path.basename(self.filename)
        if ControllerApp._modality== ModalityList.gif:
            oscAPI.sendMsg('/toSetGif', dataArray=[os.path.basename(self.filename)], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)
        elif ((ControllerApp._modality == ModalityList.manual) | (ControllerApp._modality == ModalityList.resist)): 
            oscAPI.sendMsg('/toSetPng', dataArray=[os.path.basename(self.filename)], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)
        elif ((ControllerApp._modality == ModalityList.midi)):
            oscAPI.sendMsg('/toSetObjectToShow',  dataArray=[os.path.basename(self.filename)], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)

class ColorButton(Button):
    btncolor = StringProperty(None)
    def on_press(self):
        r = ControllerApp.get_Red(self.btncolor)
        g = ControllerApp.get_Green(self.btncolor)
        b = ControllerApp.get_Blue(self.btncolor)
        print r,g,b
        if ((ControllerApp._modality== ModalityList.midi) ):
            oscAPI.sendMsg('/toSetObjectToShow', dataArray=[r,g,b], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)
        elif ((ControllerApp._modality== ModalityList.manual) | (ControllerApp._modality== ModalityList.resist)):
            print SettingsScreen.getIp(settingScreen) 
            oscAPI.sendMsg('/toOneShotFlash', dataArray=[r,g,b], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)
        
class ResistModality(Button):
    def on_press(self):
        self.background_color =  [0.2, 0.3, 0.2, 1]
        ButtonModalityHandler.midiBnt.background_color =  [0.9, 0.9, 0.9, 1]
        ButtonModalityHandler.gifBnt.background_color =  [0.9, 0.9, 0.9, 1]
        ButtonModalityHandler.manualBnt.background_color =  [0.9, 0.9, 0.9, 1]
        oscAPI.sendMsg('/toSetModality',dataArray=[ModalityList.modalities.index("resist", ) ], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)
        ControllerApp._modality = ModalityList.resist

class GifModality(Button):
    def on_press(self):
        self.background_color =  [0.2, 0.3, 0.2, 1]
        ButtonModalityHandler.resisthBnt.background_color =  [0.9, 0.9, 0.9, 1]
        ButtonModalityHandler.midiBnt.background_color =  [0.9, 0.9, 0.9, 1]
        ButtonModalityHandler.manualBnt.background_color =  [0.9, 0.9, 0.9, 1]
        self.text = Constants.gifMode
        oscAPI.sendMsg('/toSetModality', dataArray=[ModalityList.modalities.index("gif", ) ], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)
        ControllerApp._modality = ModalityList.gif

class MidiModality(Button):
    def on_press(self):
        self.background_color =  [0.2, 0.3, 0.2, 1]
        ButtonModalityHandler.resisthBnt.background_color =  [0.9, 0.9, 0.9, 1]
        ButtonModalityHandler.gifBnt.background_color =  [0.9, 0.9, 0.9, 1]
        ButtonModalityHandler.manualBnt.background_color =  [0.9, 0.9, 0.9, 1]
        self.text = Constants.midiMode
        oscAPI.sendMsg('/toSetModality', dataArray=[ModalityList.modalities.index("midi", ) ], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)
        ControllerApp._modality = ModalityList.midi
        
class ManualModality(Button):
    def on_press(self):
        self.background_color =  [0.2, 0.3, 0.2, 1]
        ButtonModalityHandler.resisthBnt.background_color =  [0.9, 0.9, 0.9, 1]
        ButtonModalityHandler.gifBnt.background_color =  [0.9, 0.9, 0.9, 1]
        ButtonModalityHandler.midiBnt.background_color =  [0.9, 0.9, 0.9, 1]
        oscAPI.sendMsg('/toSetModality', dataArray=[ModalityList.modalities.index("manual", ) ], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)
        ControllerApp._modality = ModalityList.manual
        
        

class LinearModality(Button):
    def on_press(self):
        self.background_color =  [0.2, 0.3, 0.2, 1]
        ButtonAnimationModalityHandler.randomBnt.background_color =  [0.9, 0.9, 0.9, 1]
        ControllerApp._animation_modality = AnimationModalityList.modalities.index("linear", )
        
class RandomModality(Button):
    def on_press(self):
        self.background_color =  [0.2, 0.3, 0.2, 1]
        ButtonAnimationModalityHandler.linearBnt.background_color =  [0.9, 0.9, 0.9, 1]
        ControllerApp._animation_modality = AnimationModalityList.modalities.index("random", )
        
class ButtonModalityHandler():
    resisthBnt = ResistModality(
            text=Constants.resistMode,
            size_hint=(1, 1), 
            background_color =  [0.2, 0.3, 0.2, 1]
            )

    gifBnt = GifModality(
            text=Constants.gifMode,
            size_hint=(1, 1), 
            )
    
    midiBnt = MidiModality(
            text=Constants.midiMode,
            size_hint=(1, 1), 
            )
    
    manualBnt = ManualModality(
            text=Constants.manualMode,
            size_hint=(1, 1), 
            )

class ButtonAnimationModalityHandler():
    linearBnt = LinearModality(
            background_normal = "button_incons/linearLine.png",
            size_hint=(1, 1), 
            background_color =  [0.2, 0.3, 0.2, 1]
            )

    
    randomBnt = RandomModality(
            background_normal = "button_incons/randomLine.png",
            size_hint=(1, 1), 
            )
    



class ControllerApp(App):
    
    def on_pause(self):
        # Here you can save data if needed
        return True
    
    def on_resume(self):
        # Here you can check if any data needs replacing (usually nothing)
        pass
    
    def build_config(self, config):
        config.setdefaults('section1', {
        'key1': 'value1',
        'key2': '42'
    })

    _modality=ModalityList.resist
    _animation_modality=0
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
        "h" : "h.gif",
        "ele" : "ele.gif",
        "m" : "m.gif",
        "n" : "n.gif",
        "o" : "o.gif",
        "p" : "p.gif",
        "q" : "q.gif",
        "r" : "r.gif",
        "s" : "s.gif",
        "t" : "t.gif",
        "u" : "u.gif",
        "v" : "v.gif",
        "z" : "z.gif",
        "0a" : "0a.gif",
        "0b" : "0b.gif",
        "0c" : "0c.gif",
        "0d" : "0d.gif",
        "0e" : "0e.gif",
        "0f" : "0f.gif",
        "0g" : "0g.gif",
        "0h" : "0h.gif",
        "0i" : "0i.gif",
        "0l" : "0l.gif",
        "0m" : "0m.gif",
        "0n" : "0n.gif",
        "0o" : "0o.gif",
        "0p" : "0p.gif",
        "0q" : "0q.gif",
        "0r" : "0r.gif",
        "0s" : "0s.gif",
        "0t" : "0t.gif",
        "0u" : "0u.gif",
        "0v" : "0v.gif",
        "0z" : "0z.gif",
        "1a" : "1a.gif",
        "1b" : "1b.gif",
        "1c" : "1c.gif",
        "1d" : "1d.gif",
        "1e" : "1e.gif",
        "1f" : "1f.gif",
        "1g" : "1g.gif",
        "1h" : "1h.gif",
        "1i" : "1i.gif",
        "1l" : "1l.gif",
        "1m" : "1m.gif",
        "1n" : "1n.gif",
        "1o" : "1o.gif",
        "1p" : "1p.gif",
        "1q" : "1q.gif",
        "1v" : "1v.gif",
        "1z" : "1z.gif",
        "2a" : "2a.gif",
        
        
        
        }
    
    colorMap = {
        "blue" :  "  0  0  1",
        "darkblue" : "  0  0.45",
        "turquoise3" : "  0.77.80",
        "red" :   "  1  0  0",
        "saddlebrown" : ".55.27.07",
        "green" : "  0  1  0",
        "white" : ".99.99.99",
        "yellow" :".93.99.09",
        "purple" :".99  0.83",
        }

    def build(self):
        touchtracer = Touchtracer()
        textfile = open('properties.txt', 'r') 
        ipFromTxt = textfile.read()
        print ipFromTxt
        SettingsScreen.setIp(settingScreen, ipFromTxt)

        

        
        for fn in self.gifMap:
            print fn
            btn = GifImageButton(
                #flashBt = flashBt,
                filename=fn,
                background_normal = "resources/" + fn + ".png",
                size_hint=(None, None), halign='center',
                size=(buttonDimension.get_width(), buttonDimension.get_height()), text_size=(118, None))
            menuScreen.ids.giffButtonContainer.add_widget(btn)

        userAnimation.ids.touchTracker.add_widget(touchtracer)
                
        for fn in self.gifMap:
            btn = AnimationImageButton(
                #flashBt = flashBt,
                filename=fn,
                background_normal = "resources/" + fn + ".png",
                size_hint=(None, None), halign='center',
                size=(buttonDimension.get_width(), buttonDimension.get_height()), text_size=(118, None))
            userAnimation.ids.animationButtonContainer.add_widget(btn)

        for color in self.colorMap:
            color2= self.colorMap.get(color)
            r = ControllerApp.get_Red( color2)
            g = ControllerApp.get_Green(color2)
            b = ControllerApp.get_Blue(color2)
            btn = ColorButton(
                btncolor = self.colorMap.get(color),
                background_color=(r, g, b, 1),
                size_hint=(None, None), halign='center',
                size=(buttonDimension.get_width(), buttonDimension.get_height()), text_size=(118, None)
                )
            menuScreen.ids.colorButtonContainer.add_widget(btn)
        
        userAnimation.ids.modalityAnimationContainer.add_widget(ButtonAnimationModalityHandler.linearBnt)
        userAnimation.ids.modalityAnimationContainer.add_widget(ButtonAnimationModalityHandler.randomBnt) 
        
        
        
        menuScreen.ids.modalityContainer.add_widget(ButtonModalityHandler.resisthBnt)
        menuScreen.ids.modalityContainer.add_widget(ButtonModalityHandler.gifBnt)
        menuScreen.ids.modalityContainer.add_widget(ButtonModalityHandler.midiBnt) 
        menuScreen.ids.modalityContainer.add_widget(ButtonModalityHandler.manualBnt) 
        #userAnimation.ids.startUserAmimation.add_widget(UserAnimation())                                           

        return sm



if __name__ == '__main__':
    ControllerApp().run()
