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


from kivy.lang import Builder

Builder.load_string("""
<MainScreen>:
    BoxLayout:
        orientation: 'vertical'
        id: id
""")



class Network():
    dispatherIp = "localhost"
    ipList = ["localhost"]
    piIp = '192.168.1.107'


class MainScreen(Screen):
    pass

sm = ScreenManager()
menuScreen = MainScreen(name='main')
sm.add_widget(menuScreen)

class Dispatcher(App):
    
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
            oscAPI.sendMsg(message[0],  dataArray=parameters, ipAddr=ip , port=57115)
    
    def set_status_Musk(self, message, *args):
        print Network.piIp
        oscAPI.sendMsg('/toSetMusk', dataArray=[message[2]], ipAddr=Network.piIp , port=57110)
    
    def set_status_Musk1(self, message, *args):
        print Network.piIp
        oscAPI.sendMsg('/toSetMusk1', dataArray=[message[2]], ipAddr=Network.piIp , port=57110)
    
    def set_status_Musk2(self, message, *args):
        print Network.piIp
        oscAPI.sendMsg('/toSetMusk2', dataArray=[message[2]], ipAddr=Network.piIp , port=57110)
    
    def build(self):
        Window.size = (300, 100)
        oscAPI.init()
        self._parent = Widget()
        oscid = oscAPI.listen(ipAddr=Network.dispatherIp, port=57110)
        
        oscAPI.bind(oscid, self.forward_message, '/toFlash')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        oscAPI.bind(oscid, self.forward_message, '/toOneShotFlash')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        oscAPI.bind(oscid, self.forward_message, '/toSetObjectToShow')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        oscAPI.bind(oscid, self.forward_message, '/toSetGif')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        oscAPI.bind(oscid, self.forward_message, '/toSetPng')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        oscAPI.bind(oscid, self.forward_message, '/toSetModality')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        oscAPI.bind(oscid, self.forward_message, '/toStartUserAnimation')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        oscAPI.bind(oscid, self.set_status_Musk, '/toSetMusk');
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
                
        oscAPI.bind(oscid, self.set_status_Musk1, '/toSetMusk1');
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        oscAPI.bind(oscid, self.set_status_Musk2, '/toSetMusk2');
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        oscAPI.bind(oscid, self.set_audio_visualizer, '/toSetAudioVisualizerGraph');
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
