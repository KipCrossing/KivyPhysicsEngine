from kivy.app import App
from kivy.base import runTouchApp

from kivy.graphics.texture import Texture

from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
import random
import math
import OpenFile
import graidentground


class Mechanics(Widget):
    def __init__(self, **kwargs):
        super(Mechanics, self).__init__(**kwargs)
        Clock.schedule_interval(self.Movements, 1/30.)

        f = open('Saved.txt', 'r')
        b = f.read()
        (x,y) = eval(b)
        (self.Character_Position_x, self.Character_Position_y) = (x,y+1)
        f.close()





        # Initial Values --
        ######## Tweaking #########
        self.gravity = Window.height*0.16*(1/60.)
        self.Velocity_y = Window.height*0.06
        self.Velocity = Window.height*(16./9.)*0.006

        self.Border_Bottom = Window.height*0.1
        self.Border_Top = Window.height*0.12
        self.Border_Left = Window.width*0.45
        self.Border_Right = Window.width*0.55

        self.Elastic_x = Window.width*0.3
        self.Elastic_y_Top = Window.height*20
        self.Elastic_y_Bottom = Window.height*0.8

        self.press = 0
        self.image_direction = 1

        #in X --
        self.Origin_x = -self.Character_Position_x
        self.Character_Actual_x = 0

        self.Character_Velocity_x = 0
        self.Velocity_x = self.Velocity
        #in Y --

        self.Origin_y = 0
        self.Character_Actual_y = 0

        self.Character_Velocity_y = 0
        self.Jump_distance_y = 0
        self.Jumpv = 0
        self.camera_y = 0
        self.Original_Jump_Position = 0
        self.Jump_Activate = False

        # for ground line Lower
        (self.point1_xL, self.point1_yL) = 0,0
        (self.point2_xL, self.point2_yL) = 1,0

        self.Gradient_Lower = 0

        self.P1xL = 0
        self.P1yL = 0
        self.P2xL = 0
        self.P2yL = 0

        self.Lower = 0
        self.Ground_Lower = 0

        self.ChooserL = 2

        # for ground line Upper
        (self.point1_xU, self.point1_yU) = 0,0
        (self.point2_xU, self.point2_yU) = 1,0

        self.Gradient_Upper = 0

        self.P1xU = 0
        self.P1yU = 0
        self.P2xU = 0
        self.P2yU = 0

        self.Upper = 0
        self.Ground_Upper = 0

        self.ChooserU = 2

        # for ground line Lower Top
        (self.point1_xLT, self.point1_yLT) = 0,0
        (self.point2_xLT, self.point2_yLT) =  1,0

        self.Gradient_LowerT = 0

        self.P1xLT = 0
        self.P1yLT = 0
        self.P2xLT = 0
        self.P2yLT = 0

        self.LowerT = 0
        self.Ground_LowerT = 0

        self.ChooserLT = 2

        ################
        self.Ground_Current = 0
        self.Gradient = 0
        self.point1_x = 0
        self.point2_x = 0

        # File and co-ores sorting
        self.file_x = 1
        self.file_y = 1
        self.level_indicator = "L"

        # Positioning

        self.foreground_current_x = 0
        self.foreground_current_y = 0
        self.foreground_right_x = 0
        self.foreground_right_y = 0
        self.foreground_top_x = 0
        self.foreground_top_y = 0
        self.foreground_diag_x = 0
        self.foreground_diag_y = 0

        self.foreground_count_x = 0
        self.foreground_count_y = 0
        self.foreground_current_image = None
        self.foreground_right_image = None
        self.foreground_top_image = None
        self.foreground_diag_image = None


        self.midground_x1 = 0
        self.midground_y1 = 0
        self.midground_x2 = 0
        self.midground_y2 = 0
        self.midground_count1 = 0
        self.midground_count2 = 0

        self.midground2_x1 = 0
        self.midground2_y1 = 0
        self.midground2_x2 = 0
        self.midground2_y2 = 0
        self.midground2_count1 = 0
        self.midground2_count2 = 0

        self.farground_x1 = 0
        self.farground_y1 = 0
        self.farground_x2 = 0
        self.farground_y2 = 0
        self.farground_count1 = 0
        self.farground_count2 = 0

        #Widget
        self.widget_current_image = None
        self.widget_current_x = 0
        self.widget_current_y = 0

        self.widget_right_image = None
        self.widget_right_x = 0
        self.widget_right_y = 0

        self.widget_top_image = None
        self.widget_top_x = 0
        self.widget_top_y = 0

        self.widget_diag_image = None
        self.widget_diag_x = 0
        self.widget_diag_y = 0

        self.widget_opperator = None
        self.hero_image = './WidgetImages/hero_right.png'

    def Home(self):
        Clock.unschedule(self.Movements)
        f = open("gamechoice.txt", "w")
        f.write('mainmenu')
        f.close()

    def Jump(self, *args):
        if self.Jumpv > 0:
            self.Character_Velocity_y = self.Velocity_y
            self.Jump_distance_y = 0.1
            self.Jump_Activate = True
        else:
            pass
        print "Jump pressed "

    def Right(self, *args):
        self.press = 1
        print "Right pressed  "
        self.hero_image = './WidgetImages/hero_right.png'

    def Left(self, *args):
        self.press = -1
        print "Left pressed "
        self.hero_image = './WidgetImages/hero_left.png'

    def Stop(self, *args):
        self.press = 0
        print "STOPPED! " + str(self.Character_Velocity_x)

    def Widget_Button_Current(self,*args):
        print OpenFile.read_widget(self.foreground_count_x+1,self.foreground_count_y+1)
        self.widget_opperator = OpenFile.read_widget(self.foreground_count_x+1,self.foreground_count_y+1)
    def Widget_Button_Right(self,*args):
        print OpenFile.read_widget(self.foreground_count_x+2,self.foreground_count_y+1)
        self.widget_opperator = OpenFile.read_widget(self.foreground_count_x+2,self.foreground_count_y+1)
    def Widget_Button_Top(self,*args):
        print OpenFile.read_widget(self.foreground_count_x+1,self.foreground_count_y+2)
        self.widget_opperator = OpenFile.read_widget(self.foreground_count_x+1,self.foreground_count_y+2)
    def Widget_Button_Diag(self,*args):
        print OpenFile.read_widget(self.foreground_count_x+2,self.foreground_count_y+2)
        self.widget_opperator = OpenFile.read_widget(self.foreground_count_x+2,self.foreground_count_y+2)


    def Movement_x(self, *args):
        if self.Jump_Activate:          #######################################HERE##################################
            self.Character_Velocity_x = self.press*self.Velocity
        else:

            self.Character_Velocity_x = self.press*math.sqrt((self.Velocity**2)/(1+self.Gradient**2))

        self.Velocity_x = math.sqrt((self.Velocity**2)/(1+self.Gradient**2))

        if self.Character_Actual_x > self.Border_Right:

            ratio = ((self.Character_Actual_x - self.Border_Right)/(self.Elastic_x))

            self.Character_Actual_x += self.Character_Velocity_x - self.Velocity_x*ratio

            self.Origin_x += - self.Character_Velocity_x*ratio - self.Velocity_x*ratio

        elif self.Character_Actual_x < self.Border_Left:

            ratio = ((self.Border_Left - self.Character_Actual_x)/(self.Elastic_x))

            self.Character_Actual_x += self.Character_Velocity_x + self.Velocity_x*ratio

            self.Origin_x += -self.Character_Velocity_x*ratio + self.Velocity_x*ratio

        else:
            self.Character_Actual_x += self.Character_Velocity_x
        self.Character_Position_x = self.Character_Actual_x - self.Origin_x

    def Open_File(self, *args):


        f = open('./Scene/'+ OpenFile.read_command(self.file_x,self.file_y)+ '/Lower.txt')
        self.Lower = []
        for line in f:
            self.Lower.append(eval(line))
        f.close()

        g = open('./Scene/'+ OpenFile.read_command(self.file_x,self.file_y)+ '/Upper.txt')
        self.Upper = []
        for line in g:
            self.Upper.append(eval(line))
        g.close()

        h = open('./Scene/'+ OpenFile.read_command(self.file_x,self.file_y+1)+ '/Lower.txt')
        self.Lower_Top = []
        for line in h:
            self.Lower_Top.append(eval(line))
        h.close()
        while True:
            (a,b) = self.Lower[self.ChooserL - 1]
            (c,d) = self.Lower[self.ChooserL]


            if isinstance(a, str) or isinstance(c, str):
                self.ChooserL =2
                (self.point1_xL, self.point1_yL) = (a,b)
                (self.point2_xL, self.point2_yL) = (c,d)
                break
            else:
                (self.point1_xL, self.point1_yL) = (a+Window.height*(16/9.)*(self.file_x-1),b+Window.height*(self.file_y-1))
                (self.point2_xL, self.point2_yL) = (c+Window.height*(16/9.)*(self.file_x-1),d+Window.height*(self.file_y-1))

                if self.Character_Position_x < self.point1_xL:
                    self.ChooserL += -1
                elif self.Character_Position_x > self.point2_xL:
                    self.ChooserL += 1
                else:
                    self.Gradient_Ground()      #make specific
                    break

        while True:
            (a,b) = self.Upper[self.ChooserU - 1]
            (c,d) = self.Upper[self.ChooserU]


            if isinstance(a, str) or isinstance(c, str):
                self.ChooserU =2
                (self.point1_xU, self.point1_yU) = (a,b)
                (self.point2_xU, self.point2_yU) = (c,d)
                break
            else:
                (self.point1_xU, self.point1_yU) = (a+Window.height*(16/9.)*(self.file_x-1),b+Window.height*(self.file_y-1))
                (self.point2_xU, self.point2_yU) = (c+Window.height*(16/9.)*(self.file_x-1),d+Window.height*(self.file_y-1))
                if self.Character_Position_x < self.point1_xU:
                    self.ChooserU += -1
                elif self.Character_Position_x > self.point2_xU:
                    self.ChooserU += 1
                else:
                    self.Gradient_Ground()
                    break

        while True:

            (a,b) = self.Lower_Top[self.ChooserLT - 1]
            (c,d) = self.Lower_Top[self.ChooserLT]

            if isinstance(a, str) or isinstance(c, str):
                self.ChooserLT = 2
                (self.point1_xLT, self.point1_yLT) = (a,b)
                (self.point2_xLT, self.point2_yLT) = (c,d)
                break
            else:
                (self.point1_xLT, self.point1_yLT) = (a+Window.height*(16/9.)*(self.file_x-1),b+Window.height*(self.file_y))
                (self.point2_xLT, self.point2_yLT) = (c+Window.height*(16/9.)*(self.file_x-1),d+Window.height*(self.file_y))
                if self.Character_Position_x < self.point1_xLT:
                    self.ChooserLT += -1
                elif self.Character_Position_x > self.point2_xLT:
                    self.ChooserLT += 1
                else:
                    self.Gradient_Ground()
                    break

        if self.level_indicator == "L":
            self.point1_x = self.point1_xL
            self.point2_x = self.point2_xL
            self.point1_y = self.point1_yL
            self.point2_y = self.point2_yL
            self.Ground_Current = self.Ground_Lower
            self.Gradient = self.Gradient_Lower
        elif self.level_indicator == "U":
            self.point1_x = self.point1_xU
            self.point2_x = self.point2_xU
            self.point1_y = self.point1_yU
            self.point2_y = self.point2_yU
            self.Ground_Current = self.Ground_Upper
            self.Gradient = self.Gradient_Upper

        if isinstance(self.point2_x, str) or isinstance(self.point1_x, str):
            self.Beyond_Ground()


    def Beyond_Ground(self, *args):
        if self.point1_x == "null" or self.point2_x == "null":
            if self.Jumpv > 0:
                self.Jump_Activate = True
                self.Jump_distance_y = 0.1
            else:
                pass
            if self.level_indicator == "L":
                self.file_y += - 1
                self.level_indicator = "U"
                self.Open_File()
                self.Ground_Current = self.Ground_Upper
                self.Gradient = self.Gradient_Upper
            elif self.level_indicator == "U":
                self.level_indicator = "L"
                self.Ground_Current = self.Ground_Lower
                self.Gradient = self.Gradient_Lower
                self.Open_File()

        elif self.point2_x == "Lower+":
            self.file_x += 1
            self.level_indicator = "L"
            self.ChooserL = 2
            self.ChooserU = 2
            self.ChooserLT = 2
            self.Open_File()
        elif self.point2_x == "Upper+":
            self.file_x += 1
            self.level_indicator = "U"
            self.ChooserL = 2
            self.ChooserU = 2
            self.ChooserLT = 2
            self.Open_File()
        elif self.point1_x == "Lower-":
            self.file_x += -1
            self.level_indicator = "L"
            self.ChooserL = 2
            self.ChooserU = 2
            self.ChooserLT = 2
            self.Open_File()
        elif self.point1_x == "Upper-":
            self.file_x += -1
            self.level_indicator = "U"
            self.ChooserL = 2
            self.ChooserU = 2
            self.ChooserLT = 2
            self.Open_File()
        elif self.point2_x == "STOP" or self.point1_x == "STOP":
            self.Character_Actual_x += -self.Character_Velocity_x*2
        else:
            pass

    def Gradient_Ground(self,*args):
    ################### lower ##################
        if isinstance(self.point2_xL, str) or isinstance(self.point1_xL, str):
            pass
        else:
            (self.Gradient_Lower,self.Ground_Lower) = graidentground.Ground(self.point1_xL,self.point1_yL,self.point2_xL,self.point2_yL, self.Character_Position_x)

        ##################### upper ####################
        if isinstance(self.point2_xU, str) or isinstance(self.point1_xU, str):
            pass
        else:

            (self.Gradient_Upper ,self.Ground_Upper) = graidentground.Ground(self.point1_xU,self.point1_yU,self.point2_xU,self.point2_yU, self.Character_Position_x)

        #################### lower Top ###################
        if isinstance(self.point2_xLT, str) or isinstance(self.point1_xLT, str):
            pass
        else:
            (self.Gradient_LowerT, self.Ground_LowerT) = graidentground.Ground(self.point1_xLT,self.point1_yLT,self.point2_xLT,self.point2_yLT, self.Character_Position_x)

    def Update_Ground(self, *args):
        if self.Character_Position_y > self.Ground_LowerT:
            if self.point1_xLT == 'null' or self.point2_xLT == 'null':
                if self.Character_Position_y > self.Ground_Upper:
                    if self.point1_xU == 'null' or self.point2_xU == 'null':
                        pass
                    else:
                        self.Ground_Current = self.Ground_Upper
                        self.Gradient = self.Gradient_Upper
                        self.level_indicator = "U"
                else:
                    pass
            else:
                self.Ground_Current = self.Ground_LowerT
                self.file_y +=1
                self.ChooserL =2
                self.ChooserU =2
                self.ChooserLT =2
                self.Open_File()
                self.level_indicator = "L"
        elif self.Character_Position_y > self.Ground_Upper:
            if self.point1_xU == 'null' or self.point2_xU == 'null':
                pass
            else:
                self.Ground_Current = self.Ground_Upper
                self.Gradient = self.Gradient_Upper
                self.level_indicator = "U"

    def Jump_Physics(self, *args):
        if self.Jump_Activate:                  #Stoped! # Jumping BUG!
            self.Jumpv = 0
            self.Character_Velocity_y += -self.gravity
            self.Jump_distance_y += self.Character_Velocity_y
            if self.Character_Position_y <= self.Ground_Current and self.Character_Velocity_y < 0:
                self.Jump_Activate = False
            else:
                self.Jump_Activate = True
        else:                                                                  #Going
            self.Jump_distance_y = 0
            self.Character_Velocity_y = 0
            self.Jumpv = 1
            self.Original_Jump_Position = self.Ground_Current

    def Movement_y(self,*args):
        if self.Character_Actual_y > self.Border_Top:

            ratioy = ((self.Character_Actual_y - self.Border_Top)/(self.Elastic_y_Top))
            diff = self.Character_Actual_y - self.Border_Top

            self.Origin_y += - diff*ratioy


        elif self.Character_Actual_y < self.Border_Bottom:

            ratioy = ((self.Border_Bottom - self.Character_Actual_y)/(self.Elastic_y_Bottom))
            diff = self.Character_Actual_y - self.Border_Bottom

            self.Origin_y += -diff*ratioy

        self.Character_Actual_y = self.Character_Position_y + self.Origin_y

    def Foreground_Move(self):
        if self.foreground_current_x < -Window.height*(16./9.)-Window.height*(16./9.)*0.2:
            self.foreground_count_x += 1
        elif self.foreground_current_x > 0-Window.height*(16./9.)*0.2:
            self.foreground_count_x += -1
        if self.foreground_current_y < -Window.height-Window.height*0.2:
            self.foreground_count_y += 1
        elif self.foreground_current_y > 0-Window.height*0.2:
            self.foreground_count_y += -1

        self.foreground_current_x = self.Origin_x +(self.foreground_count_x)*Window.height*(16./9.)-Window.height*(16./9.)*0.2
        self.foreground_current_y = self.Origin_y +(self.foreground_count_y)*Window.height-Window.height*0.2
        self.foreground_right_x = self.foreground_current_x + Window.height*(16./9.)
        self.foreground_right_y = self.foreground_current_y
        self.foreground_top_x = self.foreground_current_x
        self.foreground_top_y = self.foreground_current_y + Window.height
        self.foreground_diag_x = self.foreground_current_x + Window.height*(16./9.)
        self.foreground_diag_y = self.foreground_current_y + Window.height

        self.foreground_current_image = './Scene/'+OpenFile.read_command((self.foreground_count_x + 1),(self.foreground_count_y + 1))+'/Image.png'
        self.foreground_right_image = './Scene/'+OpenFile.read_command((self.foreground_count_x + 2),(self.foreground_count_y + 1))+'/Image.png'
        self.foreground_top_image = './Scene/'+OpenFile.read_command((self.foreground_count_x + 1),(self.foreground_count_y + 2))+'/Image.png'
        self.foreground_diag_image = './Scene/'+OpenFile.read_command((self.foreground_count_x + 2),(self.foreground_count_y + 2))+'/Image.png'

    def Widget_Opperator(self):
        self.widget_current_image = './WidgetImages/'+OpenFile.read_widget(self.foreground_count_x+1,self.foreground_count_y+1)+'.png'
        self.widget_current_x = self.foreground_current_x + Window.height*(16./9.)/2
        self.widget_current_y = self.foreground_current_y + Window.height*0.52

        self.widget_right_image = './WidgetImages/'+OpenFile.read_widget((self.foreground_count_x+2),(self.foreground_count_y+1))+'.png'
        self.widget_right_x = self.foreground_right_x + Window.height*(16./9.)/2
        self.widget_right_y = self.foreground_right_y + Window.height*0.52

        self.widget_top_image = './WidgetImages/'+OpenFile.read_widget(self.foreground_count_x+1,self.foreground_count_y+2)+'.png'
        self.widget_top_x = self.foreground_top_x + Window.height*(16./9.)/2
        self.widget_top_y = self.foreground_top_y + Window.height*0.52

        self.widget_diag_image = './WidgetImages/'+OpenFile.read_widget(self.foreground_count_x+2,self.foreground_count_y+2)+'.png'
        self.widget_diag_x = self.foreground_diag_x + Window.height*(16./9.)/2
        self.widget_diag_y = self.foreground_diag_y + Window.height*0.52

    def Position(self,*args):
        position_f = (self.foreground_current_x, self.foreground_current_y)
        the_ground_f = self.ids['foreground_current']
        the_ground_f.pos = position_f
        the_ground_f.size = (Window.height*(16./9.)*1.2, Window.height*1.2)
        the_ground_f.source = self.foreground_current_image

        position_f2 = (self.foreground_right_x, self.foreground_right_y)
        the_ground_f2 = self.ids['foreground_right']
        the_ground_f2.pos = position_f2
        the_ground_f2.size = (Window.height*(16./9.)*1.2, Window.height*1.2)
        the_ground_f2.source = self.foreground_right_image

        position_f3 = (self.foreground_top_x, self.foreground_top_y)
        the_ground_f3 = self.ids['foreground_top']
        the_ground_f3.pos = position_f3
        the_ground_f3.size = (Window.height*(16./9.)*1.2, Window.height*1.2)
        the_ground_f3.source = self.foreground_top_image

        position_f4 = (self.foreground_diag_x, self.foreground_diag_y)
        the_ground_f4 = self.ids['foreground_diag']
        the_ground_f4.pos = position_f4
        the_ground_f4.size = (Window.height*(16./9.)**1.2, Window.height*1.2)
        the_ground_f4.source = self.foreground_diag_image

        #Midground

        position2 = (self.midground_x1, self.midground_y1)
        the_ground2 = self.ids['midground11']
        the_ground2.pos = position2

        position2 = (self.midground_x2, self.midground_y2)
        the_ground2 = self.ids['midground12']
        the_ground2.pos = position2

        position2 = (self.midground2_x1, self.midground2_y1)
        the_ground2 = self.ids['midground21']
        the_ground2.pos = position2

        position2 = (self.midground2_x2, self.midground2_y2)
        the_ground2 = self.ids['midground22']
        the_ground2.pos = position2

        position2 = (self.farground_x1, self.farground_y1)
        the_ground2 = self.ids['farground1']
        the_ground2.pos = position2

        position2 = (self.farground_x2, self.farground_y2)
        the_ground2 = self.ids['farground2']
        the_ground2.pos = position2


        position_widget = (self.widget_current_x ,self.widget_current_y)
        the_widget = self.ids['widget_current']
        the_widget.pos = position_widget
        the_widget.background_normal = self.widget_current_image
        the_widget.background_down = self.widget_current_image

        position_widget = (self.widget_right_x ,self.widget_right_y)
        the_widget = self.ids['widget_right']
        the_widget.pos = position_widget
        the_widget.source = self.widget_right_image
        the_widget.background_normal = self.widget_right_image
        the_widget.background_down = self.widget_right_image


        position_widget = (self.widget_top_x ,self.widget_top_y)
        the_widget = self.ids['widget_top']
        the_widget.pos = position_widget
        the_widget.source = self.widget_top_image
        the_widget.background_normal = self.widget_top_image
        the_widget.background_down = self.widget_top_image

        position_widget = (self.widget_diag_x ,self.widget_diag_y)
        the_widget = self.ids['widget_diag']
        the_widget.pos = position_widget
        the_widget.source = self.widget_diag_image
        the_widget.background_normal = self.widget_diag_image
        the_widget.background_down = self.widget_diag_image

        if self.press == 1:
            self.image_direction = self.press
        elif self.press == -1:
            self.image_direction = self.press
        else:
            pass

        the_char = self.ids['Character']
        the_char.pos = (self.Character_Actual_x - Window.height*0.05*self.image_direction,self.Character_Actual_y)
        the_char.size = (Window.height*0.1*self.image_direction, Window.height*0.075)


    def Background_Move(self,*args):
        if self.midground_x1 < -Window.height*(16./9.)*1.2:
            self.midground_count1 +=1

        elif self.midground_x2 > Window.height*(16./9.)*0.8:
            self.midground_count1 +=-1
        else:
            pass
        self.midground_x1 = self.Origin_x*0.5 + Window.height*(16./9.)*self.midground_count1
        self.midground_x2 = self.Origin_x*0.5 + Window.height*(16./9.)*(self.midground_count1+1)
        self.midground_y1 = self.Origin_y*0.5-Window.height*0.2
        self.midground_y2 = self.Origin_y*0.5-Window.height*0.2

        if self.midground2_x1 < -Window.height*(16./9.)*1.2:
            self.midground2_count1 +=1

        elif self.midground2_x2 > Window.height*(16./9.)*0.8:
            self.midground2_count1 +=-1
        else:
            pass

        self.midground2_x1 = self.Origin_x*0.35 + Window.height*(16./9.)*self.midground2_count1
        self.midground2_x2 = self.Origin_x*0.35 + Window.height*(16./9.)*(self.midground2_count1+1)
        self.midground2_y1 = self.Origin_y*0.35 - Window.height*0.3
        self.midground2_y2 = self.Origin_y*0.35 - Window.height*0.3


        if self.farground_x1 < -Window.height*(16./9.):
            self.farground_count1 +=1

        elif self.farground_x2 > Window.height*(16./9.):
            self.farground_count1 +=-1
        else:
            pass

        self.farground_x1 = self.Origin_x*0.1 + Window.height*(16./9.)*self.farground_count1
        self.farground_x2 = self.Origin_x*0.1 + Window.height*(16./9.)*(self.farground_count1+1)
        self.farground_y1 = self.Origin_y*0.1 - Window.height*0.2
        self.farground_y2 = self.Origin_y*0.1 - Window.height*0.2


    def Movements(self, *args):
        self.Movement_x()
        self.Open_File()
        self.Update_Ground()
        self.Character_Position_y = self.Original_Jump_Position + self.Jump_distance_y
        self.Jump_Physics()
        self.Movement_y()
        self.Background_Move()
        self.Foreground_Move()
        self.Widget_Opperator()
        self.Position()

        f = open("Saved.txt", "w")
        f.write('('+str(self.Character_Position_x)+','+str(self.Character_Position_y)+')')
        f.close()
        ################# CHECKER ###########################
        # print '----------------------start----------------------'
        # print "Origin_x: " + str(self.Origin_x) + " Origin_y: " + str(self.Origin_y)
        # print "Actual_x: " + str(self.Character_Actual_x) + " Actual_y: " + str(self.Character_Actual_y)
        # print "Position_x: " + str(self.Character_Position_x) + " Position_y: " + str(self.Character_Position_y)
        # print "file x: " + str(self.file_x)
        # print "file y: " + str(self.file_y)
        # print "Ground current: "+str(self.Ground_Current)
        # print "Velocity X"+ str(self.Velocity_x)
        #
        # print str(self.level_indicator)
        # print "ChooserL " + str(self.ChooserL)
        # print ""
        # print "self.point1_xU = "+str(self.point1_xU)
        # print "self.point1_yU = "+str(self.point1_yU)
        # print "self.point2_xU = "+str(self.point2_xU)
        # print "self.point2_yU = "+str(self.point2_yU)
        # print "------------------------------------------------------------------"
        # print "Point1 x" + str(self.point1_x) + " Point1 y " + str(self.point1_y)
        # print "Point2 x" + str(self.point2_x) + " Point2 y " + str(self.point2_y)
        # print "------------------------------------------------------------------"
        # print "P1 x" + str(self.P1x) + " P1 y " + str(self.P1y)
        # print "P2 x" + str(self.P2x) + " P2 y " + str(self.P2y)
        # print (self.Original_Jump_Position - self.Ground_y)
        # print self.foreground_current_image
        # print self.foreground_count_x
        # print self.foreground_count_y
        # print self.widget_right_x ,self.widget_right_y
        # print self.widget_right_image

#############################################################