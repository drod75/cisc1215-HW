from graphics import *

num_rects = int(input('How many Rectangles would you like to draw today? '))

win = GraphWin(title='Interactive Window', width=700, height=700)
for x in range(num_rects):
    pnt1 = win.getMouse()
    pnt2 = win.getMouse()
    rect = Rectangle(pnt1, pnt2)
    rect.draw(win)
input('Press enter to end the window: ')
