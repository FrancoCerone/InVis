import rtmidi.midiutil as midiutil
import time
#import pigpio


import time
from neopixel import *
import argparse
from kivy.app import App
from kivy.lib.osc import oscAPI

from argparse import FileType
import fcntl
from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
from kivy.core.window import Window
from kivy.graphics.instructions import InstructionGroup
from kivy.lib.osc import oscAPI
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


GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)


# LED strip configuration:
LED_COUNT      = 731     # Number of LED pixels.
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



global blackout
blackout = Color(0, 0, 0)
global flashSleepTime
flashSleepTime = 1/6

global strip
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
global canRunStrip
canRunStrip = False  

from setup import initialize

from midi_in.InputControl import InputControl
from midi_in.InputLogger import InputLogger


class RaspBerryApp(App):
    def addAction(self, action):
        self.actions.append(action)
        return action

    def addInput(self, action, type, key, setting):
        midiInput = InputControl(action, type, key, setting)
        self.inputs.append(midiInput)
        self.inputLogger.addInput(midiInput)

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
        self.inputLogger = InputLogger()
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
        for i in range(numpixel):
            strip.setPixelColor(numpixel - i, 255)
        strip.show()
        
        print("Ready...")
        
        for i in range(strip.numPixels()):
            strip.setPixelColor(strip.numPixels() - i, 0)
        strip.show()
        
        
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

            #pi.set_PWM_dutycycle(self.params["PIN_R"], self.params["R"] * self.params["VISIBILITY"])
            #pi.set_PWM_dutycycle(self.params["PIN_G"], self.params["G"] * self.params["VISIBILITY"])
            #pi.set_PWM_dutycycle(self.params["PIN_B"], self.params["B"] * self.params["VISIBILITY"])

            time.sleep(0.01)

        print("Goodbye!")

    def __call__(self, event, data=None):
        message, deltatime = event

        print(message)
        print "leym!"
        vel = message[0]
        key = message[1]
        state = message[2] * 2
        if(vel == 144):
            for i in range(strip.numPixels()):
                
                if(key == 42):
                    ledColor = Color(255,0,0)
                else:
                    ledColor = Color(0,255,0)
                strip.setPixelColor(strip.numPixels() - i, ledColor)
            strip.show()
            for i in range(strip.numPixels()):
                strip.setPixelColor(strip.numPixels() - i, 0)
            strip.show()


        '''for midiInput in self.inputs:
            print ("primo for")
            if(midiInput.key == key):
                print ("prima if")
                
                if(midiInput.type == "trigger" and state != 0 ):
                    print('trigger')
                    midiInput.trigger(self.params, state)
                if(midiInput.type == "trigger_hold"):
                    print('trigger hold')
                    midiInput.triggerHold(self.params, state)
                if(midiInput.type == "toggle" and state != 0):
                    print('toogle')
                    midiInput.otoggle(self.params)
                if(midiInput.type == "hold"):
                    print(' hold')
                    midiInput.hold(self.params, 255 if state > 0 else 0)
                if(midiInput.type == "knob"):
                    print('tknob')
                    midiInput.knob(self.params, state)
        '''
if __name__ == '__main__':
    RaspBerryApp().run()
