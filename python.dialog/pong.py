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


Builder.load_string("""
<PongBall>:
    size: 100, 100
    pos:   1366, -50
    canvas:
        Ellipse:
            pos: self.pos
            size: self.size
            source: root.get_image()
    
""")

class ImageDispatcher():
    image = ObjectProperty
    def set_image(self, image):
        self.image = image;
    def get_image(self):
        return 'resources/pngs/'+self.image+'.png';
    
screenResolution = ScreenResolution()

imageDispatcher = ImageDispatcher()

class PongBall(Widget):
    def move(self, x,y ):
        x= -x
        self.pos = Vector(x,y) + self.pos
        
    def get_image(self):
        print "da image disp", imageDispatcher.get_image()
        return imageDispatcher.get_image() 
    
    def set_image(self, image):
        print image


    
class PongGame(Widget):
    balls = []
    def build(self):
        self.ball = PongBall()
        self.add_widget(self.ball)
        
    def update(self, dt):
        for amimation in self.balls:
            amimation.move(3, 3)
            if(amimation.pos.__getitem__(0) > 0):
                continue
            else:
                self.balls.remove(amimation)
                if (self.balls.__len__() == 0):
                    return    
    
    def add_animation(self, image):
        imageDispatcher.set_image(image)
        newAnimation = PongBall()
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