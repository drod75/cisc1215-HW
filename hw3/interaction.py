from graphics import *

num_rects = int(input('How many Rectangles would you like to draw today? '))

win = GraphWin(title='Interactive Window', width=700, height=700)
for x in range(num_rects):
    p1 = float(input('\nInput x value for point 1: '))
    p2 = float(input('Input y value for point 1: '))  
    pnt1 = Point(p1, p2)  

    p3 = float(input('\nInput x value for point 2: '))
    p4 = float(input('Input y value for point 2: '))  
    pnt2 = Point(p3, p4) 

    rect = Rectangle(pnt1, pnt2)
    rect.draw(win)
input('Press enter to end the window: ')