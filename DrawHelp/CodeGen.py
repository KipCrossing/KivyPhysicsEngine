file = open("THISONE.txt", "w")

count_y = 91
count_x = 0
for y in range(1, 91):
    count_y -=1
    for x in range(1, 91):
        if count_x > 89:
            count_x = 1
        else:
            count_x += 1
        print "X: " + str(count_x) +' - Y: ' + str(count_y)
        #file.write("X: " + str(count_x) +' - Y: ' + str(count_y) +"\n")
        file.write("            Button:"+"\n")
        file.write("                on_press: root.press_" + str(count_x) + "_"+str(count_y) + "()"+"\n")
        #file.write('    def press_' + str(count_x) + '_' + str(count_y) + '(self):' + "\n")
        #file.write('        self.the_file.write( "(Window.height*(16/9.)*' + str(count_x) + '/90,Window.height*' + str(count_y) + '/90)\\n"' + ')' + "\n")

file.close()