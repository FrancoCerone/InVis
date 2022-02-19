import time
from neopixel import *
import argparse
from kivy.app import App

from oscpy.server import OSCThreadServer

from time import sleep


from kivy.graphics.instructions import InstructionGroup
import RPi.GPIO as GPIO
import time
from logo_model_Franco import LogoFranco 
from threading import Thread
#from argh.decorators import arg


GPIO.setmode(GPIO.BOARD)


logo = LogoFranco()
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




global blackout
blackout = Color(0, 0, 0)
global flashSleepTime
flashSleepTime = 1/6

global strip
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
global canRunStrip
canRunStrip = False    



def get_ip_address():
    ip = '192.168.0.110'
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
        for i in indexToTurnOn:
            RaspBerryApp.setColorForElemtOrListWithOutWaitAndShow(i, strip)
            strip.show()
            time.sleep(100/1000.0)
            if canRunStrip == False:
                break


class TheaterChaseRunner(Thread):
    def __init__(self):
        self.running = True
    def teriminate(self):
        self._running = False
    def run(self):
        iterations = 100
        wait_ms=50
        print ("theater chase")
        for j in range(iterations):
            for q in range(3):
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
        self._running = False
    def run(self):
        internalList = list(indexToTurnOn)
        for elementLed in internalList:
            if canRunStrip == False:
                    break            
            RaspBerryApp.setColorForElemtOrList(elementLed, strip)

class TopDownCurtenRunner(Thread):
    def __init__(self):
        self.running = True
    def teriminate(self):
        self._running = False
    def run(self):
        internalList = list(indexToTurnOn)
        for elementLed in reversed(internalList):
            if canRunStrip == False:
                    break            
            RaspBerryApp.setColorForElemtOrList(elementLed, strip)


class DownUpDownRunner(Thread):
    def __init__(self):
        self.running = True
    def teriminate(self):
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
        

    
class RaspBerryApp():
    
    
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
        global indexToTurnOn
        indexToTurnOn = logo.get_bottom_up_border_leds_index()

        
        parser = argparse.ArgumentParser()
        parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
        args = parser.parse_args()
        strip.begin()

        print ("Accensione in corso")
        
        numpixel = strip.numPixels()
        for i in range(numpixel):
            strip.setPixelColor(numpixel - i, Color(0, 0, 0))
            strip.show()
        
        
        osc = OSCThreadServer()  # See sources for all the arguments
        sock = osc.listen(address=Network.ip, port=57110, default=True)
        osc.bind(b'/turnOnLogo', self.turnOn) 
        osc.bind(b'/turnOffLogo', self.turnOff)
        osc.bind(b'/logoFlash',self.flash)
        osc.bind(b'/incrementalTurnOnLogo', self.incrementalTurnOnLogocolorWipe)
        osc.bind(b'/downUpDownTurnOnLogo',self.downUpDownTurnOn)
        osc.bind(b'/theaterChase', self.theaterChaseEffect)
        
        osc.bind(b'/toSetLogoColor', self.setColor)
        
        osc.bind(b'/toSetAllLedsOn', self.setAllLedsOn)
        osc.bind(b'/toSetBorderLedOn', self.setBorderLedOn )
        osc.bind(b'/toSetBorderEyesMouthLedOn', self.setBorderEyesMouthLedOn)
        osc.bind(b'/toSetEyesLedOn',self.setEyesLedOn)
        osc.bind(b'/toSetEyesAndMounthLedOn',self.setEyesAndMouthLedOn )
        osc.bind(b'/toSetEyesAndMounthLedOn', self.setEyesAndMouthLedOn)
        osc.bind(b'/toBottomUpCurten',self.setBottomUpCurten)
        osc.bind(b'/toTopDownCurten', self.setTopDownCurten)
        #sleep(1000)
        
        #print("Serving on {}".format(server.server_address))
        #server.serve_forever()
        
        print ("fatti i bind")
    
        


        
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
                count  = numberOfRows
                while count > 0 :
                    RaspBerryApp.setColorForElemtOrListWithOutWaitAndShow(indexToTurnOn[j - count], strip)
                    count = count - 1
                if(j>0 and j< len(indexToTurnOn)):
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

    
        while True:
            time.sleep(0.01)
            
    def setColor(self, message, *args):
        print ("Tunn on")
        global color
        print ( "message", message)
        print ("args", args)

        color = Color(int(args[2]) ,int(args[0]),int(args[1]))
        print ("color da setColor", color)
        canRunStrip = True
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0,0,0))
        strip.show()
        for i in indexToTurnOn:
            #print "set Color in the for", color
            RaspBerryApp.setColorForElemtOrListWithOutWaitAndShow(i, strip)
        strip.show()
    def turnOn(self, message, *args):
        canRunStrip = True

        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
        
        for i in indexToTurnOn:
            strip.setPixelColor(i, color)
        strip.show()
        
    def setAllLedsOn(self, message, *args):
        global indexToTurnOn
        indexToTurnOn = logo.get_allSripIndex()
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
        
        for i in indexToTurnOn:
            strip.setPixelColor(i, color)
        strip.show()
    
    def setBorderLedOn(self, message, *args):
        global indexToTurnOn
        indexToTurnOn = logo.get_half1()
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
        
        for i in indexToTurnOn:
            strip.setPixelColor(i, color)
        strip.show()
        
    
    def setBorderEyesMouthLedOn(self, message, *args):
        global indexToTurnOn
        indexToTurnOn = logo.get_half2()
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
        
        for i in indexToTurnOn:
            strip.setPixelColor(i, color)
        strip.show()
        
    def setEyesLedOn(self, message, *args):
        global indexToTurnOn
        indexToTurnOn = logo.get_eyes_strips_index()
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
        
        for i in indexToTurnOn:
            strip.setPixelColor(i, color)
        strip.show()
    
    def setEyesAndMouthLedOn(self, message, *args):
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
        global color
        for i in indexToTurnOn:
            self.setColorForElemtOrListWithOutWaitAndShow(i, strip)
        strip.show()
        time.sleep(flashSleepTime)
        global blackout
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
    
    def turnOff(self, message, *args):
        global canRunStrip
        canRunStrip = False
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()


    def incrementalTurnOnLogocolorWipe(self, message, *args):
        global canRunStrip 
        canRunStrip = True
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
        global indexToTurnOn
        if(len(indexToTurnOn)== 52):
            indexToTurnOn = logo.get_left2rightSripIndex()
        
        A = WipeStripsRunner();
        At = Thread(target=A.run)
        At.start()
    
    def downUpDownTurnOn(self, message, *args):
        global canRunStrip 
        canRunStrip = True
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
        global indexToTurnOn
        indexToTurnOn = logo.get_cross_leds_index()
        A = DownUpDownRunner();
        At = Thread(target=A.run)
        At.start()

    

    def theaterChaseEffect(self, message, *args):
        global canRunStrip 
        canRunStrip = True
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
        
        A = TheaterChaseRunner();
        At = Thread(target=A.run)
        At.start()
    
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
    RaspBerryApp().build()

