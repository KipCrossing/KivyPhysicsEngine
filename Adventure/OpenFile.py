def read_command(file_x,file_y):
    d = {}
    with open("Command.txt") as f:
        for line in f:
           (key, val) = line.split()
           d[key] = val

    if 'x'+ str(file_x) + 'y' + str(file_y) in d:
        k = d['x'+ str(file_x) + 'y' + str(file_y)]
    else:
        k = d['x'+ str(0) + 'y' + str(0)]
    return k

def read_widget(file_x,file_y):
    d = {}
    with open("Widget.txt") as f:
        for line in f:
           (key, val) = line.split()
           d[key] = val

    if 'x'+ str(file_x) + 'y' + str(file_y) in d:
        k = d['x'+ str(file_x) + 'y' + str(file_y)]
    else:
        k = d['x'+ str(0) + 'y' + str(0)]
    return k




    # def Open_File(self, *args):
    #     f = open("x"+str(self.file_x)+"y"+str(self.file_y)+"L.txt",'rU')
    #     self.Lower = []
    #     for line in f:
    #         self.Lower.append(eval(line))
    #     f.close()
    #
    #     g = open("x"+str(self.file_x)+"y"+str(self.file_y)+"U.txt",'rU')
    #     self.Upper = []
    #     for line in g:
    #         self.Upper.append(eval(line))
    #     g.close()
    #
    #     h = open("x"+str(self.file_x)+"y"+str(self.file_y+1)+"L.txt",'rU')
    #     self.Lower_Top = []
    #     for line in h:
    #         self.Lower_Top.append(eval(line))
    #     h.close()
    #
    #     while True:
    #         (self.point1_xL, self.point1_yL ) = self.Lower[self.ChooserL - 1]
    #         (self.point2_xL, self.point2_yL) = self.Lower[self.ChooserL]
    #         if isinstance(self.point2_xL, str) or isinstance(self.point1_xL, str):
    #             self.ChooserL =2
    #             break
    #         elif self.Character_Position_x < self.point1_xL:
    #             self.ChooserL += -1
    #         elif self.Character_Position_x > self.point2_xL:
    #             self.ChooserL += 1
    #         else:
    #             self.Gradient_Ground()      #make specific
    #             break
    #
    #     while True:
    #         (self.point1_xU, self.point1_yU ) = self.Upper[self.ChooserU - 1]
    #         (self.point2_xU, self.point2_yU) = self.Upper[self.ChooserU]
    #         if isinstance(self.point2_xU, str) or isinstance(self.point1_xU, str):
    #             self.ChooserU =2
    #             break
    #         elif self.Character_Position_x < self.point1_xU:
    #             self.ChooserU += -1
    #         elif self.Character_Position_x > self.point2_xU:
    #             self.ChooserU += 1
    #         else:
    #             self.Gradient_Ground()
    #             break
    #
    #     while True:
    #         (self.point1_xLT, self.point1_yLT ) = self.Lower_Top[self.ChooserLT - 1]
    #         (self.point2_xLT, self.point2_yLT) = self.Lower_Top[self.ChooserLT]
    #         if isinstance(self.point2_xLT, str) or isinstance(self.point1_xLT, str):
    #             self.ChooserLT = 2
    #             break
    #         elif self.Character_Position_x < self.point1_xLT:
    #             self.ChooserLT += -1
    #         elif self.Character_Position_x > self.point2_xLT:
    #             self.ChooserLT += 1
    #         else:
    #             self.Gradient_Ground()
    #             break
    #
    #     if self.level_indicator == "L":
    #         self.point1_x = self.point1_xL
    #         self.point2_x = self.point2_xL
    #         self.point1_y = self.point1_yL
    #         self.point2_y = self.point2_yL
    #         self.Ground_Current = self.Ground_Lower
    #         self.Gradient = self.Gradient_Lower
    #     elif self.level_indicator == "U":
    #         self.point1_x = self.point1_xU
    #         self.point2_x = self.point2_xU
    #         self.point1_y = self.point1_yU
    #         self.point2_y = self.point2_yU
    #         self.Ground_Current = self.Ground_Upper
    #         self.Gradient = self.Gradient_Upper
    #
    #     if isinstance(self.point2_x, str) or isinstance(self.point1_x, str):
    #         self.Beyond_Ground()