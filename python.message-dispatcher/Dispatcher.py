'''
Created on Dec 6, 2017

@author: franco
'''

from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.lib.osc import oscAPI
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.uix.image import AsyncImage
from kivy.loader import Loader
from symbol import parameters
#Config.set('graphics', 'fullscreen', 'auto')




def get_ip_address():
    ip = '192.168.1.103'
    #ip = 'localhost'
    return ip 


def get_PiIp_address():
    ip = '192.168.1.107'
    return ip 

def get_SecondIp_address():
    ip = '192.168.1.104'
    return ip 

def get_sedond_port():
    port = '57200'
    #ip = 'localhost'
    return port 

class Network():
    dispatherIp = "192.168.1.103"
    ipList = ["localhost", "3445"]
    piIp = get_PiIp_address()


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
    
    
    
    def build(self):
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
        
         
        oscAPI.bind(oscid, self.forward_message, '/toSetMusk');
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        
        
        
        
        
        return self._parent
    
if __name__ == '__main__':
    Dispatcher().run()
