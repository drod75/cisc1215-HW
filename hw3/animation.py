from graphics import *
import time

p = Point(10, 10)
win = GraphWin(title='Animation', width=500, height=500)
p.draw(win)

for x in range(2, 10):
    p.move(dx=10*x, dy=10*x)
    time.sleep(.2)

input('Press enter to exit: ')
