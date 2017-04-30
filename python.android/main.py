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
            StackLayout:
                id: animationButtonContainer
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
    modalities = ('linear', 'parabolic', 'random')


class ModalityList():
    resist = 'resist'
    gif = 'gif'
    midi = 'midi'
    manual = 'manual'
    modalities = (resist, gif, midi, manual)

class AnimationImageButton(Button):
    filename = StringProperty(None)
    def on_press(self):
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
        ButtonAnimationModalityHandler.parabolaBnt.background_color =  [0.9, 0.9, 0.9, 1]
        ButtonAnimationModalityHandler.randomBnt.background_color =  [0.9, 0.9, 0.9, 1]
        ControllerApp._animation_modality = AnimationModalityList.modalities.index("linear", )

class ParabolaModality(Button):
    def on_press(self):
        self.background_color =  [0.2, 0.3, 0.2, 1]
        ButtonAnimationModalityHandler.linearBnt.background_color =  [0.9, 0.9, 0.9, 1]
        ButtonAnimationModalityHandler.randomBnt.background_color = [0.9, 0.9, 0.9, 1]
        ControllerApp._animation_modality = AnimationModalityList.modalities.index("parabolic", )
        
class RandomModality(Button):
    def on_press(self):
        self.background_color =  [0.2, 0.3, 0.2, 1]
        ButtonAnimationModalityHandler.parabolaBnt.background_color =  [0.9, 0.9, 0.9, 1]
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
            text="Lineare",
            size_hint=(1, 1), 
            background_color =  [0.2, 0.3, 0.2, 1]
            )

    parabolaBnt = ParabolaModality(
            text="Parabolico",
            size_hint=(1, 1), 
            )
    
    randomBnt = RandomModality(
            text="Random",
            size_hint=(1, 1), 
            )
    



class ControllerApp(App):
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
            print fn
            btn = GifImageButton(
                #flashBt = flashBt,
                filename=fn,
                background_normal = "resources/" + fn + ".png",
                size_hint=(None, None), halign='center',
                size=(buttonDimension.get_width(), buttonDimension.get_height()), text_size=(118, None))
            menuScreen.ids.giffButtonContainer.add_widget(btn)


                
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
        userAnimation.ids.modalityAnimationContainer.add_widget(ButtonAnimationModalityHandler.parabolaBnt)
        userAnimation.ids.modalityAnimationContainer.add_widget(ButtonAnimationModalityHandler.randomBnt) 
        
        
        
        menuScreen.ids.modalityContainer.add_widget(ButtonModalityHandler.resisthBnt)
        menuScreen.ids.modalityContainer.add_widget(ButtonModalityHandler.gifBnt)
        menuScreen.ids.modalityContainer.add_widget(ButtonModalityHandler.midiBnt) 
        menuScreen.ids.modalityContainer.add_widget(ButtonModalityHandler.manualBnt) 
        #userAnimation.ids.startUserAmimation.add_widget(UserAnimation())                                           

        return sm



if __name__ == '__main__':
    ControllerApp().run()
