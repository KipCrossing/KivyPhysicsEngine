file1 = open("PYTHON.txt", "w")
file2 = open("KIVY.txt", "w")
count_y = 31
count_x = 0
for y in range(1, 31):
    count_y -=1
    for x in range(1, 31):
        if count_x > 29:
            count_x = 1
        else:
            count_x += 1
        print "X: " + str(count_x) +' - Y: ' + str(count_y)
        #file.write("X: " + str(count_x) +' - Y: ' + str(count_y) +"\n")
        file2.write("            Button:"+"\n")
        file2.write("                on_press: root.press_" + str(count_x) + "_"+str(count_y) + "()"+"\n")
        file1.write('    def press_' + str(count_x) + '_' + str(count_y) + '(self):' + "\n")
        file1.write('        self.the_file.write( "(Window.height*(16/9.)*' + str(count_x) + '/30,Window.height*' + str(count_y) + '/30)\\n"' + ')' + "\n")

file1.close()
file2.close()