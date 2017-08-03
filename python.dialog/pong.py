'''
Created on 14 mar 2017

@author: francescocerone
'''
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.lang import Builder
from ScreenResolution import ScreenResolution
from kivy.graphics import Color, Rectangle
from kivy import animation
from math import log10
from random import randint

Builder.load_string("""
<PongBall>:
    size: 100, 100
    pos:   0, 0
    canvas:
        Ellipse:
            pos: self.pos
            size: self.size
            source: root.get_image()
    
""")


screenResolution = ScreenResolution()


class ImageDispatcher():
    image = ObjectProperty
    modality = ObjectProperty
    lastHeightGiven = NumericProperty
    def set_image(self, image):
        self.image = image;
    def get_image(self):
        return 'resources/animations/'+self.image+'.png';
    
    def set_modality(self, modality):
        self.modality = modality;
    def get_modality(self):
        return self.modality;
    
    def get_ball_hegth(self):
        heigth = randint(0, screenResolution.get_height()) 
        module = heigth % 100
        heigth = heigth - module
        if( heigth == self.lastHeightGiven):
            heigth = heigth - 100
        self.lastHeightGiven = heigth
        print "calculated height: ", heigth
        return heigth
        
class PongBall(Widget):
    modality = ObjectProperty
    status = ObjectProperty
    status = 'asc'
    def set_height(self, height):
        print "setted height", height
        self.pos[1] = height
        
    def move(self, x, y ):
        x= self.pos[0] +x
        y= self.pos[1] +y
    
   
        self.pos = Vector(x,y) 
        
    def get_image(self):
        print "da image disp", imageDispatcher.get_image()
        return imageDispatcher.get_image() 
    
    def set_image(self, image):
        print image
    
    def set_modality(self, modality):
        self.modality = modality;
    def get_modality(self):
        return self.modality;

    def get_status(self):
        return self.status;

imageDispatcher = ImageDispatcher()


class PongGame(Widget): 
    balls = []
    def build(self):
        self.ball = PongBall()
        self.add_widget(self.ball)
        
    def update(self, dt):
        for effect in self.balls:
            if(effect.get_modality() == 0):
                effect.move(3,0)
            if (effect.get_modality() == 1):
                #setto lo stato 
                if(effect.pos.__getitem__(1) >= screenResolution.get_height()- effect.size[1]):
                    effect.status = 'desc'
                if(effect.pos.__getitem__(1) <= 0 ):
                    effect.status = 'asc'

                if(effect.status == 'desc'):   
                    effect.move(3,-4)
                else:
                    effect.move(3,4)
            if(effect.pos.__getitem__(0) < screenResolution.get_width()):
                continue
            else:
                self.balls.remove(effect)
            if (self.balls.__len__() == 0):
                return    
    
    def add_animation(self, image, modality):
        print "Start animation with image", image, " on modality", modality
        imageDispatcher.set_image(image)
        imageDispatcher.set_modality(modality)
        heightToStart = imageDispatcher.get_ball_hegth()
        
        newAnimation = PongBall()
        newAnimation.set_height(heightToStart)
        newAnimation.set_modality(modality)
        self.balls.append(newAnimation)
        self.add_widget(newAnimation)
        print "Dimensione delle animazioni", self.balls.__len__()

class PongApp(App):
    def build(self):
        game = PongGame()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

if __name__ == '__main__':
    PongApp().run()