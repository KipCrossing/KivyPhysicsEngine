from kivy.app import App

#from kivy.uix.widget import Widget

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock

#from kivy.core.window import Window



#############################App Mechanics################################

class stuff_moving(BoxLayout):
  # Define Initial Values
    x_pos = 0
    y_pos = 0
    count = 1
    # Animate approprate functions
    def __init__(self, **kwargs):
        super(stuff_moving, self).__init__(**kwargs)
        Clock.schedule_interval(self.Anmiation, 1/14.) #Calls Animation function at 14 FPS  

#############################moving Object################################
    def Anmiation(self, *args):
        self.count += 1


        if self.count == 8:	#After 7 resets to 1
            self.count = 1
        else:
            pass
        print 'frame: ' + str(self.count)
        position = (self.x_pos, self.y_pos)
        the_graphic = self.ids['Graphic']	#Calls to Widget in KV file
        the_graphic.pos = position
        picture = 'loading' + str(self.count) + '.png'	#Opens each frame
        the_graphic.source = picture
        
#############################################################
class LoadingApp(App):
    def build(self):
        return stuff_moving()


if __name__ == "__main__":
    LoadingApp().run()