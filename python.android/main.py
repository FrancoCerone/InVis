import kivy
from kivy.uix.label import Label

kivy.require('1.0.8')

from kivy.app import App
from kivy.uix.button import Button
from kivy.properties import StringProperty, ObjectProperty
from kivy.lib.osc import oscAPI
import os
oscAPI.init()
from kivy.uix.screenmanager import ScreenManager, Screen
from ButtonDimension import ButtonDimension
from main1 import Touchtracer
from kivy.storage.jsonstore import JsonStore
from kivy.uix.slider import Slider
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from decimal import Decimal
from AnimationList import AnimationList
from VisualList import Visualist



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
                    cols: 3
                    padding: 10
                    spacing: 10
                    size_hint: 1, 5
                    height: self.minimum_height
                    width: self.minimum_width
                    id: giffButtonContainer
            ScrollView:
                size_hint: 0.5, 1
                do_scroll_x: False
                GridLayout:
                    cols: 1
                    padding: 10
                    spacing: 10
                    size_hint: 1, 20
                    height: self.minimum_height
                    width: self.minimum_width
                    id: allGiffButtonContainer
           
            
        BoxLayout:
            orientation: 'vertical'
            size_hint: 1, 0.3
            do_scroll_x: False
            GridLayout:
                cols: 9
                padding: 10
                spacing: 10
                size_hint: 1, 1
                height: self.minimum_height
                width: self.minimum_width
                id: colorButtonContainer
            BoxLayout:
                size_hint: 1, 1
                GridLayout:
                    cols: 8
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
                    text: '<- Musks Control'
                    on_press: 
                        root.manager.transition.direction = 'right'
                        root.manager.current = 'musksControl'
                    
                Button:
                    text: 'Audio Vis Control ->'
                    on_press: 
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'audioVisControl'
                
<UsersAnimation>:
    BoxLayout:
        orientation: 'vertical'
        #BoxLayout:
        #    size_hint: 1, 0.5
        #    FloatLayout:
        #        id: touchTracker
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
        ScrollView:
            size_hint: 1, 1
            do_scroll_x: True
            do_scroll_y: True
            GridLayout:
                cols: 4
                padding: 10
                spacing: 10
                size_hint: 1, 2
                width: self.minimum_width
                height: self.minimum_height
                id: animationButtonContainer
                
        BoxLayout:
            orientation: 'vertical'   
            size_hint: 1, 0.15
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
            
<AudioVisControl>:
    BoxLayout:
        orientation: 'vertical' 
        
        pos_hint:{"right":1,"top":1}
        GridLayout:
            cols: 2
            padding: 0
            spacing: 0
            size_hint: 1, 1
            width: self.minimum_width
            height: self.minimum_height
            id: audioVisContainer
                                      
    BoxLayout:
        orientation: 'horizontal'
        size_hint: 1, 0.15
        Button:
            text: '<- Main Control'
            on_press: 
                root.manager.transition.direction = 'right'
                root.manager.current = 'main'
            
        Button:
            text: 'Animation Control ->'
            on_press: 
                root.manager.transition.direction = 'left'
                root.manager.current = 'userAnimation'     
<MusksControl>:
    BoxLayout:
        orientation: 'vertical'  
        BoxLayout:
            orientation: 'vertical'
            size_hint: 1, 0.25
            do_scroll_x: False
            GridLayout:
                cols: 9
                padding: 10
                spacing: 10
                size_hint: 1, 1
                height: self.minimum_height
                width: self.minimum_width
                id: modalityLogo
        BoxLayout:
            orientation: 'horizontal'
            ScrollView:
                size_hint: 1, 1
                GridLayout:
                    cols: 1
                    padding: 10
                    spacing: 10
                    size_hint: 1, 1
                    height: self.minimum_height
                    width: self.minimum_width
                    id: colorLogoButtonContainer
            ScrollView:
                size_hint: 4, 1
                do_scroll_x: False
                GridLayout:
                    cols: 2
                    padding: 10
                    spacing: 10
                    size_hint: 1,2
                    height: self.minimum_height
                    width: self.minimum_width
                    id: musksControlButtonContainer
            ScrollView:
                size_hint: 1, 1
                do_scroll_x: False
                GridLayout:
                    cols: 1
                    padding: 10
                    spacing: 10
                    size_hint: 1, 1
                    height: self.minimum_height
                    width: self.minimum_width
                    id: flashcolorLogoButtonContainer        

    
        BoxLayout:
            orientation: 'vertical'   
            size_hint: 1, 0.15
            BoxLayout:
                orientation: 'horizontal'
               
                Button:
                    text: 'Main screen ->'
                    on_press: 
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'main'                
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
                        #root.manager.current = 'FrancoPowerGrooveScreen'
                        root.manager.current = 'main'
<FrancoPowerGrooveScreen>:
    BoxLayout:
        orientation: 'vertical'  
        ScrollView:
            size_hint: 1, 1
            do_scroll_x: True
            do_scroll_y: True
            GridLayout:
                cols: 1
                padding: 10
                spacing: 10
                size_hint: 1, 1
                width: self.minimum_width
                height: self.minimum_height
                id: francoButtonContainer
                    
    BoxLayout:
        orientation: 'vertical'   
        size_hint: 1, 0.05
        BoxLayout:
            orientation: 'horizontal'
           
            Button:
                text: ''
                background_color: (0, 0, 0.0, 1)
                on_press: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'main'
                        
""")

buttonDimension = ButtonDimension()

class MainScreen(Screen):
    pass


class UsersAnimation(Screen):
    map = {}
    pass
class AudioVisControl(Screen):
    pass

class MusksControl(Screen):
    pass


class FrancoPowerGrooveScreen(Screen):
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
audioVisScreen = AudioVisControl(name='audioVisControl')
sm.add_widget(audioVisScreen)
muskControlScreen = MusksControl(name='musksControl')
sm.add_widget(muskControlScreen)

#francoPowerGrooveScreen = FrancoPowerGrooveScreen(name='FrancoPowerGrooveScreen')
#sm.add_widget(francoPowerGrooveScreen) 
 
# later
userAnimation = UsersAnimation(name='userAnimation')
sm.add_widget(userAnimation)

settingScreen = SettingsScreen(name='settings')
settingScreen.ids.backHomeButton.bind(on_press = SettingsScreen.saveIp)
sm.add_widget(settingScreen)

#sm.switch_to(cameraScreen, direction='right')



    
class Constants():
    resistMode = "Resist"
    gifMode = "Gif"
    midiMode = "Midi"
    manualMode = "Manual"
    
    
 

class AnimationModalityList():
    modalities = ('linear', 'random')


class ModalityList():
    resist = 'resist'
    gif = 'gif'
    midi = 'midi'
    manual = 'manual'
    modalities = (resist, gif, midi, manual)

class AnimationImageButton(Button):
    store = ObjectProperty(None)
    filename = StringProperty(None)
    def on_press(self):
        print "map:" , userAnimation.map
        print "send to " + SettingsScreen.getIp(settingScreen), ", Animation Modality: ",  ControllerApp._animation_modality,  ", image: ", os.path.basename(self.filename)
        oscAPI.sendMsg('/toStartUserAnimation', dataArray=[os.path.basename(self.filename), ControllerApp._animation_modality ], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)
        

class MicFader(Slider):
    def on_touch_up(self, touch):
        if touch.grab_current == self:
            oscAPI.sendMsg('/toSetMicLevel', dataArray=[self.value], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)

class VelocityFader(Slider):
    def on_touch_up(self, touch):
        if touch.grab_current == self:
            oscAPI.sendMsg('/toSetVelocity', dataArray=[int(self.value)], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)

class GifImageButton(Button):
    filename = StringProperty(None)
    def on_press(self):
        print "send to " + SettingsScreen.getIp(settingScreen)
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
        elif (ControllerApp._modality== ModalityList.gif):
            print SettingsScreen.getIp(settingScreen) 
            oscAPI.sendMsg('/toSetColor', dataArray=[r,g,b], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)

class ColorLogoButton(Button):
    btncolor = StringProperty(None)
    def on_press(self):
        r = int((Decimal(ControllerApp.get_Red(self.btncolor)) * 255))
        g = int((Decimal(ControllerApp.get_Green(self.btncolor))* 255))
        b = int((Decimal(ControllerApp.get_Blue(self.btncolor))* 255))
        print r,g,b
        oscAPI.sendMsg('/toSetLogoColor', dataArray=[r,g,b], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)




class FlasLogoButton(Button):
    btncolor = StringProperty(None)
    def on_press(self):
        r = int((Decimal(ControllerApp.get_Red(self.btncolor)) * 255))
        g = int((Decimal(ControllerApp.get_Green(self.btncolor))* 255))
        b = int((Decimal(ControllerApp.get_Blue(self.btncolor))* 255))
        print r,g,b
        oscAPI.sendMsg('/toSetLogoColor', dataArray=[r,g,b], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)
        oscAPI.sendMsg('/logoFlash', dataArray=[0], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)
        
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
##lOGO CONTROLLER
class TurnOnLogo(Button):
    text="Accendi"
    def on_press(self):
        oscAPI.sendMsg('/turnOnLogo', dataArray=[0], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)

class AllLogoOn(Button):
    btncolor = StringProperty(None)
    def on_press(self):
        oscAPI.sendMsg('/toSetAllLedsOn', dataArray=[0], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)

class BorderLogoOn(Button):
    btncolor = StringProperty(None)
    def on_press(self):
        oscAPI.sendMsg('/toSetBorderLedOn', dataArray=[0], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)

class BorderEyesMouthLogoOn(Button):
    btncolor = StringProperty(None)
    def on_press(self):
        oscAPI.sendMsg('/toSetBorderEyesMouthLedOn', dataArray=[0], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)
   

class EyesOnLogoOn(Button):
    btncolor = StringProperty(None)
    def on_press(self):
        oscAPI.sendMsg('/toSetEyesLedOn', dataArray=[0], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)
   
class EyesAndMounthLogoOn(Button):
    btncolor = StringProperty(None)
    def on_press(self):
        oscAPI.sendMsg('/toSetEyesAndMounthLedOn', dataArray=[0], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)
   

        
class TurnOffLogo(Button):
    text="Spengi"
    def on_press(self):
        oscAPI.sendMsg('/turnOffLogo', dataArray=[0], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)

class TheaterChaseEffectLogo(Button):
    text="Teather Chase"
    def on_press(self):
        oscAPI.sendMsg('/theaterChase', dataArray=[0], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)
        
class IncrementalTurnOnLogo(Button):
    text="Accensione Incrementale"
    def on_press(self):
        oscAPI.sendMsg('/incrementalTurnOnLogo', dataArray=[0], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)
        
class ToBottomUpCurten(Button):
    text="Bottom Up Curten"
    def on_press(self):
        oscAPI.sendMsg('/toBottomUpCurten', dataArray=[0], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)
class FlashLogo(Button):
    text="Flash"
    def on_press(self):
        oscAPI.sendMsg('/logoFlash', dataArray=[0], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)


class MuskButtonOn(Button):
    background_normal = "button_icons/msOn.png"
    def on_press(self):
        oscAPI.sendMsg('/toSetMusk', dataArray=[0], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)
class MuskButtonOff(Button):
    background_normal = "button_icons/msOff.png"
    def on_press(self):
        oscAPI.sendMsg('/toSetMusk', dataArray=[1], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)
class GraphButtonOn(Button):
    def on_press(self):
        oscAPI.sendMsg('/toSetAudioVisualizerGraph', dataArray=[0], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)
class GraphButtonOff(Button):
    def on_press(self):
        oscAPI.sendMsg('/toSetAudioVisualizerGraph', dataArray=[1], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)
                
class Musk1ButtonOn(Button):
    background_normal = "button_icons/mOn.png"
    def on_press(self):
        oscAPI.sendMsg('/toSetMusk1', dataArray=[0], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)
class Musk1ButtonOff(Button):
    background_normal = "button_icons/mOff.png"
    def on_press(self):
        oscAPI.sendMsg('/toSetMusk1', dataArray=[1], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)
            
class Musk2ButtonOn(Button):
    background_normal = "button_icons/mOn.png"
    def on_press(self):
        oscAPI.sendMsg('/toSetMusk2', dataArray=[0], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)
class Musk2ButtonOff(Button):
    background_normal = "button_icons/mOff.png"
    def on_press(self):
        oscAPI.sendMsg('/toSetMusk2', dataArray=[1], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)                

class ChangeMuskStatusButton(Button):
    background_normal = "button_icons/mOn.png"
    def on_press(self):
        oscAPI.sendMsg('/changeStatus', dataArray=[1], ipAddr=SettingsScreen.getIp(settingScreen), port=57110)   

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
    muskButton = MuskButtonOn(
            text="",
            size_hint=(1, 1), 
    )
    muskButtonOff = MuskButtonOff(
            text="",
            size_hint=(1, 1), 
    )
    graphButtonOn = GraphButtonOn(
            background_normal = "button_icons/graphicon.jpg",
            text="",
            size_hint=(1, 1), 
    )
    graphButtonOff = GraphButtonOff(
            background_normal = "button_icons/graphic_off.jpg",
            text="",
            size_hint=(1, 1), 
    )
    musk1ButtonOn = Musk1ButtonOn(
            text="Musk On",
            size_hint=(1, 1), 
    )
    musk1ButtonOff= Musk1ButtonOff(
            text="Musk Off",
            size_hint=(1, 1), 
    )
    
    musk2ButtonOn = Musk2ButtonOn(
            text="Musk On",
            size_hint=(1, 1), 
    )
    musk2ButtonOff= Musk2ButtonOff(
            text="Musk Off",
            size_hint=(1, 1), 
    )
    changeStatus = ChangeMuskStatusButton(
            text="Cambia Stato",
            size_hint=(1, 1), 
    )
    
class ButtonAnimationModalityHandler():
    linearBnt = LinearModality(
            background_normal = "button_icons/linearLine.png",
            size_hint=(1, 1), 
            background_color =  [0.2, 0.3, 0.2, 1]
            )

    
    randomBnt = RandomModality(
            background_normal = "button_icons/randomLine.png",
            size_hint=(1, 1), 
            )
    



class ControllerApp(App):
    store = JsonStore('hello.json')
    
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
    _muskOnOff=0   
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
    
    colorMap = {
        "blue" :  "  0  0  1",
        "darkblue" : "  0  0.45",
        "turquoise3" : "  0.77.80",
        "red" :   "  1  0  0",
        #"saddlebrown" : ".55.27.07",
        "green" : "  0  1  0",
        "white" : ".99.99.99",
        "yellow" :".93.99.09",
        "purple" :".99  0.83",
        }
    logocolorMap = {
        "blue" :  "  0  0  1",
        "darkblue" : "  0  0.45",
        "turquoise3" : "  0.77.80",
        "red" :   "  1  0  0",
        #"saddlebrown" : ".55.27.07",
        "green" : "  0  1  0",
        "white" : "  1  1  1",
        "yellow" :".93.99.09",
        "purple" :".99  0.83",
        }
    def build(self):
        touchtracer = Touchtracer()
        touchtracer.set_store(self.store)
        
        textfile = open('properties.txt', 'r') 
        ipFromTxt = textfile.read()
        print ipFromTxt
        SettingsScreen.setIp(settingScreen, ipFromTxt)

        

        keylist = Visualist.visualListMap.keys()
        
        for fn in keylist:
            print fn
            print "valore " , Visualist.visualListMap[fn]
            if(Visualist.visualListMap[fn] ==True):
                btn = GifImageButton(
                    filename=fn,
                    background_normal = "resources/" + fn + ".png",
                    #size_hint=(None, None), halign='center',
                    size=(buttonDimension.get_width(), buttonDimension.get_height()))
                menuScreen.ids.giffButtonContainer.add_widget(btn)
            
        keylist = Visualist.visualListMap.keys()
        for fn in keylist:
            print fn
            btn = GifImageButton(
                filename=fn,
                background_normal = "resources/" + fn + ".png",
                #size_hint=(None, None), halign='center',
                size=(buttonDimension.get_width(), buttonDimension.get_height()))
            menuScreen.ids.allGiffButtonContainer.add_widget(btn)

        #userAnimation.ids.touchTracker.add_widget(touchtracer)
                
        for fn in AnimationList.animationListMap:
            btn = AnimationImageButton(
                store= self.store,
                filename=fn,
                background_normal = "resources/" + fn + ".png",
                #size_hint=(None, None), halign='center'
                size=(buttonDimension.get_width(), buttonDimension.get_height())
                )
            userAnimation.ids.animationButtonContainer.add_widget(btn)

        for color in self.colorMap:
            color2= self.colorMap.get(color)
            r = ControllerApp.get_Red( color2)
            g = ControllerApp.get_Green(color2)
            b = ControllerApp.get_Blue(color2)
            btn = ColorButton(
                btncolor = self.colorMap.get(color),
                background_color=(r, g, b, 1),
                #size_hint=(None, None), halign='center',
                size=(buttonDimension.get_width(), buttonDimension.get_height()), text_size=(118, None)
                )
            menuScreen.ids.colorButtonContainer.add_widget(btn)
        
        userAnimation.ids.modalityAnimationContainer.add_widget(ButtonAnimationModalityHandler.linearBnt)
        userAnimation.ids.modalityAnimationContainer.add_widget(ButtonAnimationModalityHandler.randomBnt) 
        
        
        
        menuScreen.ids.modalityContainer.add_widget(ButtonModalityHandler.resisthBnt)
        menuScreen.ids.modalityContainer.add_widget(ButtonModalityHandler.gifBnt)
        menuScreen.ids.modalityContainer.add_widget(ButtonModalityHandler.midiBnt) 
        menuScreen.ids.modalityContainer.add_widget(ButtonModalityHandler.manualBnt) 
        menuScreen.ids.modalityContainer.add_widget(ButtonModalityHandler.muskButton)
        menuScreen.ids.modalityContainer.add_widget(ButtonModalityHandler.muskButtonOff)
        menuScreen.ids.modalityContainer.add_widget(ButtonModalityHandler.graphButtonOn)
        menuScreen.ids.modalityContainer.add_widget(ButtonModalityHandler.graphButtonOff)
         
               
            
        muskControlScreen.ids.modalityLogo.add_widget(AllLogoOn(text="", background_normal = "button_icons/logo1.png",size_hint=(1, 2),))
        muskControlScreen.ids.modalityLogo.add_widget(BorderLogoOn(text="", background_normal = "button_icons/logo2.png",size_hint=(1, 2),))
        muskControlScreen.ids.modalityLogo.add_widget(BorderEyesMouthLogoOn(text="", background_normal = "button_icons/logo3.png",size_hint=(1, 2),))
        muskControlScreen.ids.modalityLogo.add_widget(EyesAndMounthLogoOn(text="", background_normal = "button_icons/logo4.png",size_hint=(1, 2),))
        muskControlScreen.ids.modalityLogo.add_widget(EyesOnLogoOn(text="", background_normal = "button_icons/logo5.png",size_hint=(1, 2),))
        
                                              
        muskControlScreen.ids.musksControlButtonContainer.add_widget(IncrementalTurnOnLogo(text="",size_hint=(1, 1),))
        muskControlScreen.ids.musksControlButtonContainer.add_widget(ToBottomUpCurten(text="",size_hint=(1, 1),))
        muskControlScreen.ids.musksControlButtonContainer.add_widget(TheaterChaseEffectLogo(text="",size_hint=(1, 1),))
        muskControlScreen.ids.musksControlButtonContainer.add_widget(FlashLogo(text="",))
        muskControlScreen.ids.musksControlButtonContainer.add_widget(TurnOffLogo(text="",size_hint=(1, 1),))
        
        
        muskControlScreen.ids.musksControlButtonContainer.add_widget(Label(text = "effetto4"))
        muskControlScreen.ids.musksControlButtonContainer.add_widget(Label(text = "effetto5"))
        muskControlScreen.ids.musksControlButtonContainer.add_widget(Label(text = "effetto6"))
        muskControlScreen.ids.musksControlButtonContainer.add_widget(Label(text = "effetto7"))
        muskControlScreen.ids.musksControlButtonContainer.add_widget(Label(text = "effetto8"))
        
        muskControlScreen.ids.musksControlButtonContainer.add_widget(MuskButtonOn(text="",size_hint=(1, 1),))
        muskControlScreen.ids.musksControlButtonContainer.add_widget(ButtonModalityHandler.changeStatus)
        muskControlScreen.ids.musksControlButtonContainer.add_widget(MuskButtonOff(text="",size_hint=(1, 1),))
        
        for color in self.logocolorMap:
            color2= self.colorMap.get(color)
            g = ControllerApp.get_Red( color2)
            r = ControllerApp.get_Green(color2)
            b = ControllerApp.get_Blue(color2)
            btn = ColorLogoButton(
                btncolor = self.colorMap.get(color),
                background_color=(r, g, b, 1),
                #size_hint=(None, None), halign='center',
                size=(buttonDimension.get_width(), buttonDimension.get_height()), text_size=(118, None)
                )
            muskControlScreen.ids.colorLogoButtonContainer.add_widget(btn)
        for color in self.logocolorMap:
            color2= self.colorMap.get(color)
            g = ControllerApp.get_Red( color2)
            r = ControllerApp.get_Green(color2)
            b = ControllerApp.get_Blue(color2)
            btn = FlasLogoButton(
                btncolor = self.colorMap.get(color),
                background_color=(r, g, b, 1),
                background_normal = "button_icons/flash.png",
                
                #size_hint=(None, None), halign='center',
                size=(buttonDimension.get_width(), buttonDimension.get_height()), text_size=(118, None)
                )
            muskControlScreen.ids.flashcolorLogoButtonContainer.add_widget(btn)
        #muskControlScreen.ids.musksControlButtonContainer.add_widget(ButtonModalityHandler.musk1ButtonOn)
        #muskControlScreen.ids.musksControlButtonContainer.add_widget(ButtonModalityHandler.musk2ButtonOn)

        #muskControlScreen.ids.musksControlButtonContainer.add_widget(ButtonModalityHandler.musk1ButtonOff)
        #muskControlScreen.ids.musksControlButtonContainer.add_widget(ButtonModalityHandler.musk2ButtonOff)
        
        b = BoxLayout(orientation='vertical')
        s1 = MicFader(orientation='vertical', value=350, min=400, max=1)
        b.add_widget(s1)
        micImage = Image(source = "button_icons/mic.png") 
        b.add_widget(micImage)
        audioVisScreen.ids.audioVisContainer.add_widget(b)
        
        b2 = BoxLayout(orientation='vertical')
        s2 = VelocityFader(orientation='vertical', value=3500, min=4000, max=1000)
        b2.add_widget(s2)
        speedImage = Image(source = "button_icons/speed.png") 
        b2.add_widget(speedImage)
        audioVisScreen.ids.audioVisContainer.add_widget(b2)
        

            
        
        fn = 'FrancoLogo'
        francoLogoButton = GifImageButton(
                filename=fn,
                background_normal = "resources/" + fn + ".png",
                #size_hint=(None, None), halign='center',
                size=(buttonDimension.get_width(), buttonDimension.get_height()))
        graphButtonOn = GraphButtonOn(
            text="",
            background_normal = "button_icons/graphicon.jpg",
            size_hint=(1, 1), 
        )
        
        #francoPowerGrooveScreen.ids.francoButtonContainer.add_widget(francoLogoButton)
        #francoPowerGrooveScreen.ids.francoButtonContainer.add_widget(graphButtonOn)
        
        return sm



if __name__ == '__main__':
    ControllerApp().run()
