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

GPIO.setmode(GPIO.BOARD)

GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)

#GPIO.cleanup()



def get_ip_address():

    ip = '192.168.1.107'

    return ip 

class Network():
    ip = get_ip_address()


class RaspBerryApp(App):
    _color = Color(1, 1, 1)
    _isFlashRunning = False
    _isRersistable = True
    _modality=0
    a=True
    couter=0
    
    def build(self):
        oscAPI.init()
        oscid = oscAPI.listen(ipAddr=Network.ip, port=57110) # per elektroWave WiFi: 192.168.0.12
        oscAPI.bind(oscid, self.setStatus, '/toSetMusk')
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        self._parent = Widget()
        return self._parent
    
  
    def setStatus(self, message, *args):
        print 'arrivato il messaggio' , message[2]
        GPIO.output(8,message[2])
        GPIO.output(10,message[2])

if __name__ == '__main__':
    RaspBerryApp().run()
