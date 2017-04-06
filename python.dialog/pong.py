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

Builder.load_string("""
<PongBall>:
    size: 50, 50
    pos:   -50, -50
    canvas:
        Ellipse:
            pos: self.pos
            size: self.size
            source: root.image()
    
""")

class PongBall(Widget):

    #pos = 40,40
    velocity_x = NumericProperty(1)
    velocity_y = NumericProperty(1)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    
    def move(self, x,y ):
        self.pos = Vector(x,y) + self.pos
        
    def image(self):
        return 'resources/pngs/a.png'


class PongGame(Widget):
    balls = []
    def build(self):
        self.ball = PongBall()
        self.add_widget(self.ball)
        print "fatto"
        
    def update(self, dt):
        for amimation in self.balls:
            amimation.move(3, 3)
            #print amimation.pos
            if(amimation.pos.__getitem__(0) <1000):
                #print "Posizione dell'animation", amimation.pos
                continue
            else:
                self.balls.remove(amimation)
                if (self.balls.__len__() == 0):
                    return    
                
            

    
    def add_animation(self):
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