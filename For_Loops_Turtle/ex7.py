# creates another spiral using a for loop

# imports turtle and random module
import turtle, random

# try increasing and decreasing the angle
angle = 61

# creates a list of colors
colors = ['red', 'purple']

turtle.showturtle()
turtle.shape("turtle")
turtle.pensize(6)

for x in range(150):
    # randomly changes color during drawing
    # selects color from the list of colors
    turtle.color(random.choice(colors)) # Can you see the pattern better if you only choose one color?
    turtle.forward(x)
    turtle.left(angle)

input('Press \'Enter\' to clear image.')
