import main

def Ground (x1,y1,x2,y2,Character_Position_x):
    Graident = ((y2 - y1)*1.0/(x2 - x1)*1.0)
    Ground = Graident*(Character_Position_x - x1) + y1
    return (Graident,Ground)
