from graphics import *

win = GraphWin('Drawing Window', width=500, height=500)
c1 = Circle(Point(100, 100), radius=10)
c2 = Circle(Point(300, 100), radius=10)
rect = Rectangle(Point(200,200), Point(250,250))
c1.draw(win)
c2.draw(win)
rect.draw(win)

win.close()