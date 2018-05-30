from ctypes import windll, Structure, c_long, byref
import time, os

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y}
def read():
    file = open("command.txt")
    numbers = file.read()
    file.close()
    return numbers

def main():
    can_click = 0
    countx = 0
    county = 0
    #os.startfile("server.py")
    while True:
        coordinates = read().split(" ")
        for n, i in enumerate(coordinates):
            try:
                coordinates[n] = float(i[2:])
            except:
                pass
        if type(coordinates[0]) != str:
            y = coordinates[0]
            x = coordinates[1]
            z = coordinates[2]
            t = int(coordinates[3])
            l = int(coordinates[4])
            r = int(coordinates[5])
            countx = countx + x/50
            county = county + y/50
            if can_click < 5000:
                can_click += 1
            if l == 1 and can_click == 5000:
                can_click = 0
                windll.user32.mouse_event(2, int(x), int(y), 0, 0)
                windll.user32.mouse_event(4, int(x), int(y), 0, 0)
            if t == 1:
                if countx >= 1:
                    countx -= 1
                    pos = queryMousePosition()
                    windll.user32.SetCursorPos(pos["x"]+1, pos["y"])
                if countx <= 1:
                    countx += 1
                    pos = queryMousePosition()
                    windll.user32.SetCursorPos(pos["x"]-1, pos["y"])
                if county >= 1:
                    county -= 1
                    pos = queryMousePosition()
                    windll.user32.SetCursorPos(pos["x"], pos["y"]+1)
                if county <= 1:
                    county += 1
                    pos = queryMousePosition()
                    windll.user32.SetCursorPos(pos["x"], pos["y"]-1)
            print(x,y)
main()
