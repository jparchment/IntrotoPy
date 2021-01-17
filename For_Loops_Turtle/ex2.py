# Draws a square using a for loop

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

# draws square usng a for loop

# WHAT NUMBER SHOULD BE INPUT FOR THE RANGE TO DRAW A SQUARE?
# CORRECT ANY SYNTAX ERRORS BELOW

for x in range(?)
turtle.forward(100)
turtle.right(90)

# not part of the loop.
print("Food for thought: Why doesn't this have to be part of the for loop? /U0001F914 /U0001F914 /U0001F914")
turtle.end_fill()

input('Hit /'Enter/' to clear image')
