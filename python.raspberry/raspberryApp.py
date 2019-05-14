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
from logo_model import Logo 
from threading import Thread


GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)


logo = Logo()
# LED strip configuration:
LED_COUNT      = logo.get_number_of_leds()#731      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 11  # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

global color
color = Color(255, 0, 0)
global indexToTurnOn
#indexToTurnOn = logo.get_eyes_and_mounth_strips_index()
#indexToTurnOn = logo.get_bottom_up_border_index()
indexToTurnOn = logo.get_bottom_up_border_leds_index()



global blackout
blackout = Color(0, 0, 0)
global flashSleepTime
flashSleepTime = 1/6

global strip
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
global canRunStrip
canRunStrip = False    



def get_ip_address():
    ip = '192.168.0.52'
    return ip
class Network():
    ip = get_ip_address();
    
def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in indexToTurnOn:
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)
                

           

class WipeStripsRunner(Thread):
    def __init__(self):
        self.running = True
    def teriminate(self):
        self._running = False
    def run(self):
        print "accensione da thread Separato incrermentale"
        print "canRunStrip fuori", canRunStrip
        
        for i in indexToTurnOn:
            RaspBerryApp.setColorForElemtOrListWithOutWaitAndShow(i, strip)
            strip.show()
            time.sleep(10/1000.0)
            if canRunStrip == False:
                print 'break'
                break


class TheaterChaseRunner(Thread):
    def __init__(self):
        self.running = True
    def teriminate(self):
        self._running = False
    def run(self):
        iterations = 100
        wait_ms=50
        for j in range(iterations):
            print "1"
            for q in range(3):
                print "2"
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i+q, color)
                    if canRunStrip == False:
                        break
                strip.show()
                time.sleep(wait_ms/1000.0)
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i+q, 0)
                    if canRunStrip == False:
                        break
                if canRunStrip == False:
                    break                    
            if canRunStrip == False:
                break

        


class BottomUpCurtenRunner(Thread):
    def __init__(self):
        self.running = True
    def teriminate(self):
        print "terminated bottomUp"
        self._running = False
    def run(self):
        print "accensione BottomUpCurtenRunner"
        internalList = list(indexToTurnOn)
        for elementLed in internalList:
            if canRunStrip == False:
                    break            
            RaspBerryApp.setColorForElemtOrList(elementLed, strip)

class TopDownCurtenRunner(Thread):
    def __init__(self):
        self.running = True
    def teriminate(self):
        print "terminated topDown"
        self._running = False
    def run(self):
        print "accensione TopDownCurtenRunner"
        internalList = list(indexToTurnOn)
        for elementLed in reversed(internalList):
            if canRunStrip == False:
                    break            
            RaspBerryApp.setColorForElemtOrList(elementLed, strip)


class DownUpDownRunner(Thread):
    def __init__(self):
        self.running = True
    def teriminate(self):
        print "terminated DownUpDownRunner"
        self._running = False
    def run(self):
        numberOfRows = 30
        iterations = 2
        for j in range(iterations):
            for j in range(len(indexToTurnOn) - numberOfRows +1 ):
                if canRunStrip == False:
                    break            
                for count in range(0,numberOfRows):
                    RaspBerryApp.setColorForElemtOrListWithOutWaitAndShow(indexToTurnOn[j + count], strip)
                    if canRunStrip == False:
                        break            
                if(j>0):
                    RaspBerryApp.turnOffForElemtOrList(indexToTurnOn[j -1], strip)
                    if canRunStrip == False:
                        break            
                strip.show() 
            j = len(indexToTurnOn)
            while j > numberOfRows and canRunStrip:
                if canRunStrip == False:
                    break     
                count  = numberOfRows
                while count > 0 :
                    if canRunStrip == False:
                        break     
                    RaspBerryApp.setColorForElemtOrListWithOutWaitAndShow(indexToTurnOn[j - count], strip)
                    count = count - 1
                if(j>0 and j< len(indexToTurnOn)):
                    if canRunStrip == False:
                        break  
                    RaspBerryApp.turnOffForElemtOrList(indexToTurnOn[j], strip)
                strip.show()    
                j = j - 1
        global color
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)
            if canRunStrip == False:
                break  
        strip.show()
        

    
class RaspBerryApp(App):
    @staticmethod 
    def setColorForElemtOrList(elementLed, strip):
        if (type(elementLed) == list):
            for ledStrip in elementLed:
                strip.setPixelColor(ledStrip, color)
        else:
            strip.setPixelColor(elementLed, color)
        strip.show()    
        time.sleep(10/1000.0)
        
    @staticmethod 
    def turnOffForElemtOrList(elementLed, strip):
        if (type(elementLed) == list):
            for ledStrip in elementLed:
                strip.setPixelColor(ledStrip, Color(0, 0, 0))
        else:
            strip.setPixelColor(elementLed, Color(0, 0, 0))
        strip.show()    
    
        
    @staticmethod 
    def setColorForElemtOrListWithOutWaitAndShow(elementLed, strip):
        if (type(elementLed) == list):
            for ledStrip in elementLed:
                strip.setPixelColor(ledStrip, color)
        else:
            strip.setPixelColor(elementLed, color)
    
    def build(self):


        
        parser = argparse.ArgumentParser()
        parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
        args = parser.parse_args()
        strip.begin()

        print "Accensione in corso"
        
        numpixel = strip.numPixels()
        for i in range(numpixel):
            strip.setPixelColor(numpixel - i, Color(0, 0, 0))
            strip.show()
        
        oscAPI.init()
        oscid = oscAPI.listen(ipAddr=Network.ip, port=57110) # per elektroWave WiFi: 192.168.0.12
        oscAPI.bind(oscid, self.turnOn, '/turnOnLogo') 
        oscAPI.bind(oscid, self.turnOff, '/turnOffLogo')
        oscAPI.bind(oscid, self.flash, '/logoFlash')
        oscAPI.bind(oscid, self.incrementalTurnOnLogocolorWipe, '/incrementalTurnOnLogo')
        oscAPI.bind(oscid, self.downUpDownTurnOn, '/downUpDownTurnOnLogo')
        oscAPI.bind(oscid, self.theaterChaseEffect, '/theaterChase')
        oscAPI.bind(oscid, self.setColor, '/toSetLogoColor')
        oscAPI.bind(oscid, self.setStatus, '/toSetMusk')
        oscAPI.bind(oscid, self.setStatusMask1, '/toSetMusk1')
        oscAPI.bind(oscid, self.setStatusMask2, '/toSetMusk2')
        oscAPI.bind(oscid, self.changeStatus, '/changeStatus')
        
        oscAPI.bind(oscid, self.setAllLedsOn, '/toSetAllLedsOn')
        oscAPI.bind(oscid, self.setBorderLedOn, '/toSetBorderLedOn')
        oscAPI.bind(oscid, self.setBorderEyesMouthLedOn, '/toSetBorderEyesMouthLedOn')
        oscAPI.bind(oscid, self.setEyesLedOn, '/toSetEyesLedOn')
        oscAPI.bind(oscid, self.setEyesAndMouthLedOn, '/toSetEyesAndMounthLedOn')
        oscAPI.bind(oscid, self.setEyesAndMouthLedOn, '/toSetEyesAndMounthLedOn')
        oscAPI.bind(oscid, self.setBottomUpCurten, '/toBottomUpCurten')
        oscAPI.bind(oscid, self.setTopDownCurten, '/toTopDownCurten')
    
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)

        #################################################
        #Show case accensione ###########################
        
        '''for indexLed in indexToTurnOn:
            print "indice**************: ",i
            strip.setPixelColor(indexLed, Color(127, 127, 127))
            strip.show()
        '''
        
        
        ######################################
        indexToTurnOn = logo.get_bottom_up_border_leds_index()
        numberOfRows = 40
        for jj in range(1):
            for j in range(len(indexToTurnOn) - numberOfRows +1 ):
                for count in range(0,numberOfRows):
                    RaspBerryApp.setColorForElemtOrListWithOutWaitAndShow(indexToTurnOn[j + count], strip)
                if(j>0):
                    RaspBerryApp.turnOffForElemtOrList(indexToTurnOn[j -1], strip)
                strip.show() 
            j = len(indexToTurnOn)
            while j > numberOfRows:
                print "ci passas 1 "
                count  = numberOfRows
                while count > 0 :
                    print "ci passas 2 "
                    RaspBerryApp.setColorForElemtOrListWithOutWaitAndShow(indexToTurnOn[j - count], strip)
                    count = count - 1
                if(j>0 and j< len(indexToTurnOn)):
                    print "ci passas 3 "
                    RaspBerryApp.turnOffForElemtOrList(indexToTurnOn[j], strip)
                strip.show()    
                j = j - 1
            
            
        global color
        for elementLed in indexToTurnOn:
            if(type(elementLed) == list):
                for ledStrip in elementLed:
                    strip.setPixelColor(ledStrip, color)
                strip.show()
                time.sleep(0.05)
            else:
                strip.setPixelColor(elementLed, color)
                strip.show()
        
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
        
        for elementLed in reversed(indexToTurnOn):
            if(type(elementLed) == list):
                for ledStrip in elementLed:
                    strip.setPixelColor(ledStrip, color)
                strip.show()
                time.sleep(0.05)
            else:
                strip.setPixelColor(elementLed, color)
                strip.show()

    

    def setColor(self, message, *args):
        print "Tunn on"
        print 'color 1' , int(message[2])
        print 'color 2' , int(message[3])
        print 'color 3' , int(message[4])
        global color
        color = Color(int(message[2]), int(message[3]), int(message[4]))
        canRunStrip = True
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0,0,0))
        strip.show()
        for i in indexToTurnOn:
            #print "set Color in the for", color
            RaspBerryApp.setColorForElemtOrListWithOutWaitAndShow(i, strip)
        strip.show()
    def turnOn(self, message, *args):
        print "Tunn on"
        canRunStrip = True

        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
        
        for i in indexToTurnOn:
            strip.setPixelColor(i, color)
        strip.show()
        
    def setAllLedsOn(self, message, *args):
        print "setAllLedsOn"
        global indexToTurnOn
        indexToTurnOn = logo.get_allSripIndex()
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
        
        for i in indexToTurnOn:
            strip.setPixelColor(i, color)
        strip.show()
    
    def setBorderLedOn(self, message, *args):
        print "setBorderLedOn"
        global indexToTurnOn
        indexToTurnOn = logo.get_border_index()
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
        
        for i in indexToTurnOn:
            strip.setPixelColor(i, color)
        strip.show()
        
    
    def setBorderEyesMouthLedOn(self, message, *args):
        print "setBorderEyesMouthLedOn"
        global indexToTurnOn
        indexToTurnOn = logo.get_border_eyes_mouth_index()
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
        
        for i in indexToTurnOn:
            strip.setPixelColor(i, color)
        strip.show()
        
    def setEyesLedOn(self, message, *args):
        print "setBorderEyesMouthLedOn"
        global indexToTurnOn
        indexToTurnOn = logo.get_eyes_strips_index()
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
        
        for i in indexToTurnOn:
            strip.setPixelColor(i, color)
        strip.show()
    
    def setEyesAndMouthLedOn(self, message, *args):
        print "setBorderEyesMouthLedOn"
        global indexToTurnOn
        indexToTurnOn = logo.get_eyes_and_mounth_strips_index()
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
        
        for i in indexToTurnOn:
            strip.setPixelColor(i, color)
        strip.show()
    
                
    def flash(self, message, *args):
        global canRunStrip
        canRunStrip = False
        print "flash"
        for i in indexToTurnOn:
            strip.setPixelColor(i, color)
        strip.show()
        time.sleep(flashSleepTime)
        print "acceso"
        global blackout
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
        print "spento"
    
    def turnOff(self, message, *args):
        print "Turn off"
        global canRunStrip
        canRunStrip = False
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()


    def incrementalTurnOnLogocolorWipe(self, message, *args):
        print "accensione incrermentale"
        global canRunStrip 
        canRunStrip = True
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
        if(len(indexToTurnOn)== 52):
            global indexToTurnOn
            indexToTurnOn = logo.get_allSripIndex()
        
        A = WipeStripsRunner();
        At = Thread(target=A.run)
        At.start()
        print "Fine"
    
    def downUpDownTurnOn(self, message, *args):
        print "top Up Down"
        global canRunStrip 
        canRunStrip = True
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
        global indexToTurnOn
        indexToTurnOn = logo.get_bottom_up_border_leds_index()
        A = DownUpDownRunner();
        At = Thread(target=A.run)
        At.start()
        print "Fine"

    

    def theaterChaseEffect(self, message, *args):
        global canRunStrip 
        canRunStrip = True
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
        
        A = TheaterChaseRunner();
        At = Thread(target=A.run)
        At.start()
        print "Fine"
    
    def setBottomUpCurten(self, message, *args):
        global canRunStrip 
        canRunStrip = True
        global indexToTurnOn
        indexToTurnOn = logo.get_bottom_up_border_leds_index()
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
        A = BottomUpCurtenRunner();
        At = Thread(target=A.run)
        At.start()
        
    
    def setTopDownCurten(self, message, *args):
        global canRunStrip 
        canRunStrip = True
        global indexToTurnOn
        indexToTurnOn = logo.get_bottom_up_border_leds_index()
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
        A = TopDownCurtenRunner();
        At = Thread(target=A.run)
        At.start()
    
    
      
    def setStatus(self, message, *args):
        print 'arrivato il messaggio' , message[2]
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



                    




                    


    def wheel(pos):
        """Generate rainbow colors across 0-255 positions."""
        if pos < 85:
            return Color(pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return Color(255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return Color(0, pos * 3, 255 - pos * 3)

    def rainbow(strip, wait_ms=20, iterations=1):
        """Draw rainbow that fades across all pixels at once."""
        for j in range(256*iterations):
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, wheel((i+j) & 255))
            strip.show()
            time.sleep(wait_ms/1000.0)

    def rainbowCycle(strip, wait_ms=20, iterations=5):
        """Draw rainbow that uniformly distributes itself across all pixels."""
        for j in range(256*iterations):
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
            strip.show()
            time.sleep(wait_ms/1000.0)

    def theaterChaseRainbow(strip, wait_ms=50):
        """Rainbow movie theater light style chaser animation."""
        for j in range(256):
            for q in range(3):
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i+q, wheel((i+j) % 255))
                strip.show()
                time.sleep(wait_ms/1000.0)
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i+q, 0)
        
if __name__ == '__main__':
    RaspBerryApp().run()

