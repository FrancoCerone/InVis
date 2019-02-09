'''
Created on Dec 6, 2017

@author: franco
'''

from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
from kivy.graphics import Color, Rectangle
from kivy.lib.osc import oscAPI
from kivy.loader import Loader
from kivy.uix.image import AsyncImage
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from symbol import parameters
from kivy.lang import Builder
from kivy.uix.settings      import SettingItem
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from decimal import Decimal


from kivy.lang import Builder

Builder.load_string("""
<MainScreen>:
    BoxLayout:
        orientation: 'vertical'
        id: id
""")



class Network():
    dispatherIp = '192.168.0.4'
    ipList = ["localhost"]
    piIp = '192.168.0.5'


class MainScreen(Screen):
    pass

sm = ScreenManager()
menuScreen = MainScreen(name='main')
sm.add_widget(menuScreen)

class Dispatcher(App):
    

    def normalizeValueForRaspberry(self, message):
        if  '.' in message:
            print "contiene il punto"
            message = '0'+ message
        return message

    def forward_message(self, message, *args):
        i=2;
        parameters = []
        while i< len(message):
            print 'message[i]:', message[i] 
            parameters.append(message[i])
            i=i+1;
        
        for ip in Network.ipList:
            print 'message[0]: ', message[0]
            print 'paramenters: ', parameters
            print 'ip: ', ip
            if message[0] in( '/toOneShotFlash' ,  '/toSetColor'):
                
                red = int(( Decimal( self.normalizeValueForRaspberry(message[2])) * 255))
                green = int(( Decimal( self.normalizeValueForRaspberry(message[3])) * 255))
                message[4] = int(( Decimal( self.normalizeValueForRaspberry(message[4])) * 255))
                message[2] = green
                message[3] = red
                self.set_logo_color(message )
                
            oscAPI.sendMsg(message[0],  dataArray=parameters, ipAddr=ip , port=57115)

    
    def set_status_Musk(self, message, *args):
        print Network.piIp
        print "messaggio raspberry:" , message[2]
        oscAPI.sendMsg('/toSetMusk', dataArray=[message[2]], ipAddr=Network.piIp , port=57110)
    
    def set_status_Musk1(self, message, *args):
        print Network.piIp
        oscAPI.sendMsg('/toSetMusk1', dataArray=[message[2]], ipAddr=Network.piIp , port=57110)
    
    def set_status_Musk2(self, message, *args):
        print Network.piIp
        oscAPI.sendMsg('/toSetMusk2', dataArray=[message[2]], ipAddr=Network.piIp , port=57110)
    def change_status_musk(self, message, *args):
        print Network.piIp
        oscAPI.sendMsg('/changeStatus', dataArray=[message[2]], ipAddr=Network.piIp , port=57110)
    
    
    def set_turn_on_logo(self, message, *args):
        print Network.piIp
        oscAPI.sendMsg('/turnOnLogo', dataArray=[message[2]], ipAddr=Network.piIp , port=57110)
        
    def set_turn_off_logo(self, message, *args):
        print Network.piIp
        oscAPI.sendMsg('/turnOffLogo', dataArray=[message[2]], ipAddr=Network.piIp , port=57110)
    
    def set_incremental_turn_on_logo(self, message, *args):
        print Network.piIp
        oscAPI.sendMsg('/incrementalTurnOnLogo', dataArray=[message[2]], ipAddr=Network.piIp , port=57110)    
    def set_logo_flash(self, message, *args):
        print Network.piIp
        oscAPI.sendMsg('/logoFlash', dataArray=[message[2]], ipAddr=Network.piIp , port=57110)    
    def set_logo_color(self, message, *args):
        print "setto il colore del  logo"
        print message
        i=2;
        parameters = []
        while i< len(message):
            parameters.append(message[i])
            i=i+1;
        oscAPI.sendMsg('/toSetLogoColor', dataArray=parameters, ipAddr=Network.piIp , port=57110)   
        
    

    
    
    
    def build(self):
        Window.size = (300, 100)
        oscAPI.init()
        self._parent = Widget()
        oscid = oscAPI.listen(ipAddr=Network.dispatherIp, port=57110)
        
        oscAPI.bind(oscid, self.forward_message, '/toFlash')
        oscAPI.bind(oscid, self.forward_message, '/toOneShotFlash')
        oscAPI.bind(oscid, self.forward_message, '/toSetObjectToShow')
        oscAPI.bind(oscid, self.forward_message, '/toSetGif')
        oscAPI.bind(oscid, self.forward_message, '/toSetPng')
        oscAPI.bind(oscid, self.forward_message, '/toSetModality')
        oscAPI.bind(oscid, self.forward_message, '/toStartUserAnimation')
        #maschere
        oscAPI.bind(oscid, self.set_status_Musk, '/toSetMusk');
        oscAPI.bind(oscid, self.set_status_Musk1, '/toSetMusk1');
        oscAPI.bind(oscid, self.set_status_Musk2, '/toSetMusk2');
        #logo
        oscAPI.bind(oscid, self.set_turn_on_logo, '/turnOnLogo');
        oscAPI.bind(oscid, self.set_turn_off_logo, '/turnOffLogo');
        oscAPI.bind(oscid, self.set_incremental_turn_on_logo, '/incrementalTurnOnLogo');
        oscAPI.bind(oscid, self.set_logo_flash, '/logoFlash');
        oscAPI.bind(oscid, self.set_logo_color, '/toSetLogoColor');
        
        
        oscAPI.bind(oscid, self.change_status_musk, '/changeStatus');
        oscAPI.bind(oscid, self.forward_message, '/toSetAudioVisualizerGraph');
        oscAPI.bind(oscid, self.forward_message, '/toSetMicLevel');
        oscAPI.bind(oscid, self.forward_message, '/toSetVelocity');
        
        oscAPI.bind(oscid, self.forward_message, '/toSetColor');

        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        dispatcherIpLabel = Label(text='Dipatcher IP  ->' + Network.dispatherIp, markup=True)
        menuScreen.ids.id.add_widget(dispatcherIpLabel)
                
        raspberryIpLAbel = Label(text='Raspberry IP  ->' + Network.piIp, markup=True)
        menuScreen.ids.id.add_widget(raspberryIpLAbel)
        
        for ip in Network.ipList:
            invisIp = Label(text='InViS IP  ->' +ip, markup=True)
            menuScreen.ids.id.add_widget(invisIp)
        
        
        return sm
    
if __name__ == '__main__':
    Dispatcher().run()
