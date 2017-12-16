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



class Network():
    dispatherIp = "192.168.1.100"
    ipList = ["192.168.1.100", '192.168.1.105']
    piIp = '192.168.1.107'


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
        oscAPI.sendMsg('/toSetStatus', dataArray=[message[2]], ipAddr=Network.piIp , port=57120)
    
    
    
    def build(self):
        
        
        #for ip in Network.ipList:
       #     btn = GifImageButton(
        #        filename=ip,
         #       text = ip
         #       #size_hint=(None, None), halign='center',
         #       size=(100, 100)
          #  menuScreen.ids.giffButtonContainer.add_widget(btn)
        
        
        
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
        
        
        return self._parent
    
if __name__ == '__main__':
    Dispatcher().run()
