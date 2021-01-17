# creates a zigzag pattern

# imports turtle module
import turtle

# sets up turtle
turtle.showturtle()
turtle.shape('circle')

# try changing the pensize number 
turtle.pensize(8)

# sets the color to orange and the background to red
turtle.color('orange')
turtle.bgcolor('red')

# draws zigzag

length = 25
angle = 45
turtle.showturtle()
turtle.shape("turtle")
turtle.forward(length)
turtle.right(angle)
turtle.forward(length)
turtle.left(angle)
turtle.forward(length)
turtle.right(angle)
turtle.forward(length)
turtle.left(angle)
turtle.forward(length)
turtle.right(angle)
turtle.forward(length)
turtle.left(angle)
turtle.forward(length)
turtle.right(angle)
turtle.forward(length)

input()
