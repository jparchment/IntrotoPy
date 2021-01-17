# draws a single square using turtle graphics

# imports turtle module
import turtle

# sets up turtle
turtle.showturtle()
turtle.shape('turtle')

# try changing the pensize number 
turtle.pensize(8)

# sets the fill color to purple and the border to green
turtle.color('green', 'purple')
turtle.begin_fill()

# draws square
turtle.forward(100)
turtle.right(90)

turtle.forward(100)
turtle.right(90)

turtle.forward(100)
turtle.right(90)

turtle.forward(100)
turtle.right(90)

turtle.end_fill()
input('This program can be written using a for loop. Check out ex2.py. Press Enter.')

