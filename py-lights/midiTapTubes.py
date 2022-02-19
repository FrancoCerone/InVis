import rtmidi.midiutil as midiutil
import time
#import pigpio


import time
from neopixel import *
import argparse
from kivy.app import App
import enum
from oscpy.server import OSCThreadServer
from argparse import FileType
import fcntl
from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
from kivy.core.window import Window
from kivy.graphics.instructions import InstructionGroup
from kivy.metrics import MetricsBase
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.videoplayer import VideoPlayer
import os
import struct
import time
import RPi.GPIO as GPIO
import time
from threading import Thread
#from kivy.lib.osc import oscAPI
from kivy.clock import Clock
from pythonosc import udp_client
from pythonosc import dispatcher
from pythonosc import osc_server




def get_ip_address():
    ip = '192.168.0.110'
    return ip
class Network():
    ip = get_ip_address();
    


# LED strip configuration:
LED_COUNT      = 416 #+ 790     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

global color
color = Color(255, 0, 0)
global indexToTurnOn
#indexToTurnOn = logo.get_eyes_and_mounth_strips_index()
#indexToTurnOn = logo.get_bottom_up_border_index()


class PadEnum(enum.IntEnum):
    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_ 
    
class Kick(PadEnum):
    skin = 1

class Pad1(PadEnum):
    border  = 37
    border1  = 38
    border2 = 40

    start = 0 
    end  = 104

class Pad2(PadEnum):
    border = 50
    skin = 48
    
    
    start = 105 
    end  = 208

class Pad3(PadEnum):
    border  = 47
    skin = 45


class Pad4(PadEnum):
    
    border  = 58
    skin = 43
    
    start = 209
    end  = 312

class Crash(PadEnum):
    border  = 49
    skin = 55

class Ride(PadEnum):
    border  = 51
    skin = 59



global blackout
blackout = Color(0, 0, 0)
global flashSleepTime
flashSleepTime = 1/6

global strip
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
global canRunStrip
canRunStrip = False  




class RaspBerryApp(App):
    def addAction(self, action):
        self.actions.append(action)
        return action



    def build(self):
        
        print("Starting py-lights...")

        self.params = {
            "R": 0,
            "G": 0, 
            "B": 0, 
            "MAX": 255, 
            "Counter": 1,
            "PIN_R": 0,
            "PIN_G": 0,
            "PIN_B": 0
        }
        self.actions = []
        self.inputs = []
        print("Initializing MIDI")
        midiin, port_name = midiutil.open_midiinput(1)
        midiin.set_callback(self)
        parser = argparse.ArgumentParser()
        parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
        args = parser.parse_args()
        strip.begin()

        numpixel = strip.numPixels()
        
        for i in range(LED_COUNT):
            strip.setPixelColor(numpixel - i, 50)
        strip.show()

        print("Ready... dfg")
        
        while True:
            self.params["Counter"] += 1

            self.params["R"] = 0
            self.params["G"] = 0
            self.params["B"] = 0
            self.params["VISIBILITY"] = 1
            
            for action in self.actions:
                action.update(self.params)

            for action in self.actions:
                self.params["R"] += action.settings["Color"].r
                self.params["G"] += action.settings["Color"].g
                self.params["B"] += action.settings["Color"].b
                if action.settings["MUTE"] == True:
                    self.params["VISIBILITY"] = 0

            self.params["R"] = min(self.params["R"], self.params["MAX"])
            self.params["G"] = min(self.params["G"], self.params["MAX"])
            self.params["B"] = min(self.params["B"], self.params["MAX"])

            time.sleep(0.01)

        print("Goodbye!")

    def __call__(self, event, data=None):

        
        message, deltatime = event

        print(message)
        
        vel = message[0]
        pad = message[1]
        state = message[2] * 2
        
        if(vel == 153 or vel == 144 ):
            if(Kick.has_value(pad)):
                for i in range(0,20):
                    
                    ledColor = Color(0,255,0)
                    strip.setPixelColor(i, ledColor)
                    strip.setPixelColor(i+ (52 + 32), ledColor)
                    
                    strip.setPixelColor(i +104, ledColor)
                    strip.setPixelColor(i +104 + (52 + 32), ledColor)
                    
                    strip.setPixelColor(i +104 + 104, ledColor)
                    strip.setPixelColor(i +104 + 104 + (52 + 32), ledColor)
                    
                    strip.setPixelColor(i +104 + 104+ 104, ledColor)
                    strip.setPixelColor(i +104 + 104+ 104 + (52 + 32), ledColor)
                    
                strip.show()
                
            if(Crash.has_value(pad)):
                for i in range(0,20):
                    strip.setPixelColor(i + 52 -20, Color(255 - i,0,255))
                    strip.setPixelColor(i + 52, Color(255 - i -i ,0,255))
                    
                    strip.setPixelColor(i +156, Color(255 - i,255,0))
                    strip.setPixelColor(i +156 - 20, Color(255 - i -i ,255,0))
                    
                    strip.setPixelColor(i +260, Color(255 - i,255,0))
                    strip.setPixelColor(i +260 - 20, Color(255 - i -i ,255,0))
                    
                    strip.setPixelColor(i + 364, Color(255 - i,255,255))
                    strip.setPixelColor(i + 364 - 20, Color(255 - i -i ,255,0))
                strip.show()
            
            if(Ride.has_value(pad)):
                for i in range(0,20):
                    strip.setPixelColor(i + 52 -20 -10 , Color(255 - i,0,255))
                    strip.setPixelColor((i + 52) + 10, Color(255 - i -i ,0,255))
                    
                    strip.setPixelColor(i +156 - 20 - 10, Color(255 - i -i ,255,0))
                    strip.setPixelColor(i +156 +10 , Color(255 - i,255,0))
                    
                    strip.setPixelColor(i +260 - 20 - 10, Color(255 - i -i ,255,0))
                    strip.setPixelColor(i +260 + 10, Color(255 - i,255,0))
                    
                    strip.setPixelColor(i + 364 - 20 -10, Color(255 - i -i ,255,0))
                    strip.setPixelColor(i + 364 +10 , Color(255 - i,255,255))
                strip.show()
            
            
            
            
            
            if(Pad1.has_value(pad)):
                for i in range(0,104):
                    ledColor = Color(255,255,255)
                    strip.setPixelColor(i, ledColor)
                strip.show()
            
            if(Pad2.has_value(pad)):
                for i in range(105,208):
                    #blue
                    ledColor = Color(0,0,255)
                    
                    strip.setPixelColor(i, ledColor)
                strip.show()
            
            if(Pad3.has_value(pad)):
                for i in range(209,312):
                    ledColor = Color(0,255,0)
                    strip.setPixelColor(i, ledColor)
                strip.show()
            
            if(Pad4.has_value(pad)):
                for i in range(313, 416):
                    ledColor = Color(255,0,0)
                    strip.setPixelColor(i, ledColor)
                strip.show()
            
            
            time.sleep(0.01)
            #( G , R , B)
            ledColor =  Color(0,0,255)
            for i in range(416):
                strip.setPixelColor(i, 25)
            
            # for i in range(416):
            #     if(i % 52) < 7:
            #         #( G , R , B)
            #         ledColor =  Color(0,255,0)
            #     elif(i % 52) < 14:
            #         ledColor = Color(127,255,0)
            #     elif(i % 52) < 21:
            #         ledColor = Color(255,255,0)
            #     elif(i % 52) < 28:    
            #         ledColor = Color(255,0, 0)
            #     elif(i % 52) < 34:   tou        #         ledColor = Color(0,0,255)
            #     elif(i % 52) < 41:    
            #         ledColor = Color(46, 43, 95)
            #     else:
            #         ledColor = Color( 0, 139, 255)
            #     strip.setPixelColor(i, ledColor)
                
            strip.show()
                    
                
if __name__ == '__main__':
    RaspBerryApp().run()
