from kivy.app import App
from kivy.base import runTouchApp
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.graphics.vertex_instructions import (Rectangle)
from kivy.graphics.context_instructions import Color
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.properties import ListProperty
from kivy.core.window import Window
from kivy.core.audio import SoundLoader

import random

#############################App Mechanics################################
#############################App Mechanics################################
#############################App Mechanics################################

class stuff_moving(BoxLayout):
    # initial Values
    value = 0                   #used to initilize jump. 1 - Jump, 0 - Stay still
    position_variation = 0      #used to vary the position of the attacking object
    velocity_variation = 1  
    counter = 0                 #used to count the score

    # Called when Button is pressed    
    def Pressed(self, *args):
        self.value = 1
        self.position_variation = (random.random())*Window.width*0.8
    
    #Called when restart button is pressed. Resets Values
    def Restart(self, *args):
        self.value = 0
        self.position_variation = 0
        self.counter = 0
        self.time_k = 1
        self.y_velocity_k = Window.width*0.021
        self.x_pos_k = Window.width/5
        self.y_pos_k = 0
        self.loose = 0
        self.time_a = 1
        self.x_velocity_a = -Window.width*0.03
        self.y_pos_a = 0
        self.x_pos_a = Window.width
        self.velocity_variation = 1

        
    # Animate approprate functions
    def __init__(self, **kwargs):
        super(stuff_moving, self).__init__(**kwargs)
        Clock.schedule_interval(self.Bounce, 1/60.)  
        Clock.schedule_interval(self.Attack, 1/60.)
        Clock.schedule_interval(self.MoveSmallBox, 1/60.)  

#############################Jumping Object animation##########################
    count = 1
    def animation(self, *args):
        self.count += 1
        if self.count == 4:
            self.count = 1
        else:
            pass
#############################Jumping Object################################
    time_k = 1                  
    y_velocity_k = Window.width*0.021
    x_pos_k = Window.width/5
    y_pos_k = 0
    loose = 0
    def Bounce(self, *args):
        if self.loose == 1:
            self.x_pos_k = Window.width/5
            self.y_pos_k = 0
            position = (self.x_pos_k, self.y_pos_k)
            the_ball = self.ids['Jump']
            the_ball.pos = position
            pass
        else:
            the_ball = self.ids['Jump']
            if self.value == 1:
                self.time_k += 1/60.

                self.y_velocity_k += -self.time_k*Window.width*0.0005

                self.y_pos_k += self.y_velocity_k*self.time_k

                if self.y_pos_k < 0:
                   self.time_k = 1
                   self.y_velocity_k = Window.width*0.021
                   self.y_pos_k = 0
                   self.value = 0
                       
                position = (self.x_pos_k, self.y_pos_k)
                the_ball.pos = position


#############################Attacking Object###############################

###########Size of attaking object#################

    x_ratio_a = 0.2
    y_ratio_a = 0.2
    def Attack_Size(self, *args):
        swing = random.random()
        if 0 < swing < 0.25:
                self.x_ratio_a = 0.1
                self.y_ratio_a = 0.1
        elif 0.25 < swing < 0.5:
                self.x_ratio_a = 0.2
                self.y_ratio_a = 0.2
        elif 0.5 < swing < 0.75:
                self.x_ratio_a = 0.42
                self.y_ratio_a = 0.1
        else:
                self.x_ratio_a = 0.1
                self.y_ratio_a = 0.265
        pass
#########Movement of attacking object###############
    time_a = 1
    x_velocity_a = -Window.width*0.03
    y_pos_a = 0
    x_pos_a = Window.width 
    def Attack(self, *args):
        #Check if objects have colided
        if (self.y_pos_k < self.y_pos_a + Window.width*self.y_ratio_a and 
            self.x_pos_a < self.x_pos_k + Window.width*0.1 and 
            self.x_pos_a + Window.width*self.x_ratio_a> self.x_pos_k):
            self.loose = 1

            HighScore = open('highscore.txt', 'r')
            b =  HighScore.read()
            if int(b) > self.counter:
                pass
            else:
                HighScore = open('highscore.txt', 'w')
                HighScore.write(str(self.counter))
            HighScore = open('highscore.txt', 'r')
            score = 'Game Over\n  Score: ' + str(self.counter) + '\n High Score: ' + str(HighScore.read())
            the_square = self.ids['Out_Score']
            the_square.text = score
            f = open("gamechoice.txt", "w")
            f.write('scratch')
            f.close()
            Clock.unschedule(self.Bounce)
            Clock.unschedule(self.Attack)
            Clock.unschedule(self.MoveSmallBox)
            pass
        else:
            self.time_a += 1/60. 

            self.x_pos_a += (-Window.width*0.015)*self.velocity_variation
            
            if self.x_pos_a < -Window.width*self.x_ratio_a:
                self.velocity_variation = 0.9 + random.random()*0.55
                self.x_pos_a = Window.width + self.position_variation
                self.counter += 1
                self.Attack_Size()
            position = (self.x_pos_a, self.y_pos_a)
            the_square = self.ids['Attack']
            the_square.size = (Window.width*self.x_ratio_a, Window.width*self.y_ratio_a)
            the_square.pos = position
            if self.counter < 1:
                score = 'Tap to Jump'
            else:
                score = 'Score: ' + str(self.counter)
            the_square = self.ids['Out_Score']
            the_square.text = score
#            print str(score)
##############################################################################
    x_pos_b1 = (random.random()*Window.width)
    y_pos_b1 = (random.random()*Window.width)
    x_pos_b2 = (random.random()*Window.width)
    y_pos_b2 = (random.random()*Window.width)
    x_pos_b3 = (random.random()*Window.width)
    y_pos_b3 = (random.random()*Window.width)
    x_pos_b4 = (random.random()*Window.width)
    y_pos_b4 = (random.random()*Window.width)
    x_pos_b5 = (random.random()*Window.width)
    y_pos_b5 = (random.random()*Window.width)
    x_pos_b6 = (random.random()*Window.width)
    y_pos_b6 = (random.random()*Window.width)
    x_pos_b7 = (random.random()*Window.width)
    y_pos_b7 = (random.random()*Window.width)
    x_pos_b8 = (random.random()*Window.width)
    y_pos_b8 = (random.random()*Window.width)

    def MoveSmallBox (self, *args):
        self.x_pos_b1 = self.x_pos_b1 - Window.width*0.001
        if self.x_pos_b1 < 0:
            self.x_pos_b1 = Window.width
            self.y_pos_b1 = (random.random()*Window.height)
        else:
            pass
        the_box = self.ids['Box1']
        the_box.pos = (self.x_pos_b1, self.y_pos_b1)

        #######################New Small Box###################
        self.x_pos_b2 = self.x_pos_b2 - Window.width*0.001
        if self.x_pos_b2 < 0:
            self.x_pos_b2 = Window.width
            self.y_pos_b2 = (random.random()*Window.height)
        else:
            pass
        the_box = self.ids['Box2']
        the_box.pos = (self.x_pos_b2, self.y_pos_b2)
        #######################New Small Box###################
        self.x_pos_b3 = self.x_pos_b3 - Window.width*0.001
        if self.x_pos_b3 < 0:
            self.x_pos_b3 = Window.width
            self.y_pos_b3 = (random.random()*Window.height)
        else:
            pass
        the_box = self.ids['Box3']
        the_box.pos = (self.x_pos_b3, self.y_pos_b3)
        #######################New Small Box###################
        self.x_pos_b4 = self.x_pos_b4 - Window.width*0.001
        if self.x_pos_b4 < 0:
            self.x_pos_b4 = Window.width
            self.y_pos_b4 = (random.random()*Window.height)
        else:
            pass
        the_box = self.ids['Box4']
        the_box.pos = (self.x_pos_b4, self.y_pos_b4)
        #######################New Small Box###################
        self.x_pos_b5 = self.x_pos_b5 - Window.width*0.001
        if self.x_pos_b5 < 0:
            self.x_pos_b5 = Window.width
            self.y_pos_b5 = (random.random()*Window.height)
        else:
            pass
        the_box = self.ids['Box5']
        the_box.pos = (self.x_pos_b5, self.y_pos_b5)
        #######################New Small Box###################
        self.x_pos_b6 = self.x_pos_b6 - Window.width*0.001
        if self.x_pos_b6 < 0:
            self.x_pos_b6 = Window.width
            self.y_pos_b6 = (random.random()*Window.height)
        else:
            pass
        the_box = self.ids['Box6']
        the_box.pos = (self.x_pos_b6, self.y_pos_b6)
        #######################New Small Box###################
        self.x_pos_b7 = self.x_pos_b7 - Window.width*0.001
        if self.x_pos_b7 < 0:
            self.x_pos_b7 = Window.width
            self.y_pos_b7 = (random.random()*Window.height)
        else:
            pass
        the_box = self.ids['Box7']
        the_box.pos = (self.x_pos_b7, self.y_pos_b7)
        #######################New Small Box###################
        self.x_pos_b8 = self.x_pos_b8 - Window.width*0.001
        if self.x_pos_b8 < 0:
            self.x_pos_b8 = Window.width
            self.y_pos_b8 = (random.random()*Window.height)
        else:
            pass
        the_box = self.ids['Box8']
        the_box.pos = (self.x_pos_b8, self.y_pos_b8)
        
##############################################################################    
class SmallBox(FloatLayout):
    pass
        

#############################################################
class MovementApp(App):
    def build(self):
        return stuff_moving()
        return SmallBox()


if __name__ == "__main__":
    MovementApp().run()