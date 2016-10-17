from kivy.uix.button import Button
from kivy.uix.widget import Widget



class Main_Menu(Widget):
    def __init__(self, **kwargs):
        super(Main_Menu, self).__init__(**kwargs)


    def Box_Game(self):
        f = open("gamechoice.txt", "w")
        f.write('box')
        f.close()

    def Scratch(self):
        f = open("gamechoice.txt", "w")
        f.write('scratch')
        f.close()

