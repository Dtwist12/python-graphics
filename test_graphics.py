###
### http://anh.cs.luc.edu/handsonPythonTutorial/index.html
###

###
### http://anh.cs.luc.edu/python/hands-on/3.1/examples.zip
###

from graphics import *

### Instantiate Graphics Window
win = GraphWin('my window', 1000,1000)
import random

for i in range(3):
  r = random.random()
  g = random.random()
  b = random.random()
  rgb = [r,g,b]



### Start your nested loops here
for x in range(10):

  for y in range(15):

        ### First pick a center point for the circle
       pt = Point(30 + 100 * x/2, y * 50)
       rect = Rectangle(Point(20, 10), pt)


        # Then draw the circle
      #cir = Circle(pt, 25)
               
        # Set the color
     # cir.setOutline('red')
     # cir.setFill('blue')
  rect.setFill(rgb)
  rect.setOutline('green')
        # Then render
     # cir.draw(win)
  rect.draw(win)
### end your loop here

# Wait for a mouse click to close the Graphics window
win.getMouse()
