from kivy.app import App
import kivy

kivy.require('1.8.0')

from MainMenu import Main_Menu
import map
import box

from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
# Builder.load_file()

#############################################################
class AdventureApp(App):

    def __init__(self, **kwargs):
        super(AdventureApp, self).__init__(**kwargs)
        Builder.load_file('mainMenu.kv')
        Builder.load_file('adventure.kv')
        Builder.load_file('movement.kv')
        self.WidgetSet = BoxLayout()
        self.Game = Main_Menu()
        self.b = None
        f = open("gamechoice.txt", "w")
        f.write('mainmenu')
        f.close()

    def build(self):
        Clock.schedule_interval(self.update, 1)
        return self.WidgetSet


    def update(self, dt):
        print 'update'
        f = open('gamechoice.txt', 'r')
        a = f.read()
        f.close()
        if self.b == a:
            print 'passed'
        else:
            self.b = a
            if a == "mainmenu":
                print 'MainMenu!!'
                self.WidgetSet.clear_widgets()
                self.Game = Main_Menu()
                self.WidgetSet.add_widget(self.Game)
            elif a == 'scratch':
                print 'Scratch!!'
                self.WidgetSet.clear_widgets()
                self.Game = map.Mechanics()
                self.WidgetSet.add_widget(self.Game)
            elif a == 'box':
                print 'BOX!!'
                self.WidgetSet.clear_widgets()
                self.Game = box.stuff_moving()
                self.WidgetSet.add_widget(self.Game)
            else:
                pass





if __name__ == "__main__":
    AdventureApp().run()