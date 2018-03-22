# P4T1a:  Shapes
# Karla Weinbrenner
# 22 March 2018

import turtle
win = turtle.Screen()
win.title ("Oscar & Zelda")

#Create Oscar
oscar=turtle.Turtle()
oscar.color ("blue")

#Create Zelda
zelda=turtle.Turtle()
zelda.shape ("turtle")

#Display options
oscar.pensize (3)
oscar.pencolor ("blue")
oscar.shape ("turtle")
zelda.pensize (3)


#Square
oscar.forward (40)
oscar.left (90)
oscar.forward (40)
oscar.left (90)
oscar.forward (40)
oscar.left (90)
oscar.forward (40)

#triangle
zelda.pencolor ("hotpink")
zelda.forward (120)
zelda.left(120)
zelda.forward (120)
zelda.left (120)
zelda.forward (120)

#end command
win.mainloop()

    
