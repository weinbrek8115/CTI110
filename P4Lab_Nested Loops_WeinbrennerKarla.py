#CTI 110
#P4Lab: Nested Loops
#Karla Weinbrenner
#26March2018

#Create a turtle graphics progrm that draws a shape using a nested loop

import turtle
    
star=turtle.Turtle()
star.color ("hotpink")
star.pensize (3)
star.shape ("turtle")

for i in range (50):
    star.forward(50)
    star.right(144)


turtle.done()
