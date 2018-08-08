from argparse import FileType
import fcntl
from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.graphics.instructions import InstructionGroup
from kivy.lib.osc import oscAPI
from kivy.metrics import MetricsBase
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.widget import Widget
import os
import socket
import struct
import time
import RPi.GPIO as GPIO
#GPIO.cleanup()
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)

#GPIO.cleanup()



def get_ip_address():

    ip = '192.168.1.106'

    return ip 

class Network():
    ip = get_ip_address()


class RaspBerryApp(App):
    
    def build(self):
        oscAPI.init()
        oscid = oscAPI.listen(ipAddr=Network.ip, port=57110) # per elektroWave WiFi: 192.168.0.12
        oscAPI.bind(oscid, self.setStatus, '/toSetMusk')
        oscAPI.bind(oscid, self.setStatusMask1, '/toSetMusk1')
        oscAPI.bind(oscid, self.setStatusMask2, '/toSetMusk2')
	oscAPI.bind(oscid, self.changeStatus, '/changeStatus')

        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        self._parent = Widget()
        return self._parent
    
  
    def setStatus(self, message, *args):
        #print 'arrivato il messaggio' , message[2]
	if message[2] == 0 :
		#print 'accendo'
        	GPIO.output(10,(message[2])%2)
		time.sleep(0.1)
        	GPIO.output(8,(message[2])%2)
	else:
		#print 'spengo'
		GPIO.output(10,(message[2])%2)
		GPIO.output(8,(message[2])%2)		

    def changeStatus(self, message, *args):
	GPIO.output(8,1)	
	time.sleep(0.1)
 	GPIO.output(8,0)



	        
    def setStatusMask1(self, message, *args):
        print 'arrivato il messaggio' , message[2]
        GPIO.output(8,(message[2]+1)%2)
        
    def setStatusMask2(self, message, *args):
        print 'arrivato il messaggio' , message[2]
        GPIO.output(10, (message[2]+1)%2)
        
if __name__ == '__main__':
    RaspBerryApp().run()
