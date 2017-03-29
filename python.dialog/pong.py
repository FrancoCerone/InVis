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
        Rectangle:
            pos: self.pos
            size: self.size
    
""")

class PongBall(Widget):

    #pos = 40,40
    velocity_x = NumericProperty(1)
    velocity_y = NumericProperty(1)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    
    def move(self, x,y ):
        self.pos = Vector(x,y) + self.pos


class PongGame(Widget):
    ball = ObjectProperty(None)
    balls = []
    def build(self):
        #self._parent = Widget()
        self.ball = PongBall()
        self.add_widget(self.ball)
        #self.ball = PongBall()
        
        #self._parent.add_widget(self.ball)
        print "fatto"
    def update(self, dt):
        for amimation in self.balls:
            #amimation.move(20,20)
            print amimation.pos
            
        self.ball.move(10,10)
        print self.ball.pos.__getitem__(0)
        if(self.ball.pos.__getitem__(0) < 600):
            print self.ball.pos
        else:
            self.ball.pos= 0,0
            return False

    
    def add_animation(self):
        self.balls.append(PongBall())
        print "Dimensione delle animazioni", self.balls.__len__()

class PongApp(App):
    def build(self):
        game = PongGame()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

if __name__ == '__main__':
    PongApp().run()