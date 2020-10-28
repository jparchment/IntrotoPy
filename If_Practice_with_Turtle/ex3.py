import turtle
# sets the background colour for the GUI
turtle.bgcolor('green')

# acceps both integers and floats as input
x = float(input('Enter any number for x: '))

# executes the following block(s) if the condition is True
if x == 100:
    turtle.color('purple')
    turtle.pensize(10)
    turtle.forward(200)
  
if x <= 0:
    # delay slows the turtle (or drawing) down
    turtle.delay(20)

    turtle.dot(150,'orange')

    # lifts pen from paper so as not to create unnecessary lines
    turtle.penup()
    turtle.goto(0,75)
    # puts pen back down when ready to draw the next image
    turtle.pendown()
    turtle.dot(125, 'blue')

    turtle.penup()
    turtle.goto(0,-75)
    turtle.pendown()
    turtle.dot(125, 'magenta')

    turtle.penup()
    turtle.goto(-75,0)
    turtle.pendown()
    turtle.dot(125, 'purple')

    turtle.penup()
    turtle.goto(75,0)
    turtle.pendown()
    turtle.dot(125, 'red')
  
if x > 0:
    turtle.dot(100, 'cyan')
  

# -------------------------------

# asks user for another input which will be saved to the variable y
y = int(input('Please enter an integer greater than 0 for y: '))

# executes the following block(s) of code if the condition is True.
if y <= 0:
    y = int(input('Invalid input. You must enter an integer greater than 0. Try again >> '))

if y > 10:
    turtle.dot(80, 'blue')
    turtle.dot(50, 'dark green')
    turtle.dot(30, 'magenta')

    turtle.penup()
    turtle.goto(0-75,0)
    turtle.pendown()
    turtle.dot(80, 'blue')
    turtle.dot(50, 'dark green')
    turtle.dot(30, 'magenta')

print('Nothing more to do.')
print('\nThe value for x is', x)
print('\nThe value for y is', y)
print('\nWhat is the result if the input for x is 100?')

input()  
