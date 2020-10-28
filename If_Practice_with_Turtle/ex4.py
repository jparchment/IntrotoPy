import turtle

# sets the background colour 
turtle.bgcolor('black')

# asks the user to input an integer for x
x = int(input('Enter an integer: '))

# executes the following block(s) of code if the condition is True
if x <= 3:
    turtle.dot(500, 'purple')
   
if x > 3:
    turtle.dot(500, 'chartreuse')
# ------------------------------------------------
#
# asks the user to input another integer for y
y = int(input('enter another integer: '))

# slows the drawing down
turtle.delay(45)

# executes the following block(s) of code if the condition is True.
if y < 0:
    turtle.dot(250, 'blue')

if y > 0:
    turtle.dot(400, 'orange')

if y == 0:
    turtle.color('green')
    # draws a shape and fills it with the color green
    turtle.begin_fill()
    turtle.left(120)
    turtle.forward(50)
    turtle.left(120)
    turtle.forward(50)
    turtle.left(120)
    turtle.forward(50)
    turtle.end_fill()

# -----------------------------------------------------

# asks the user for a decimal number for z
z = float(input('Enter a decimal: '))

turtle.delay(10)

# executes the following block(s) of code if the condition is True
if z != 7.5:
    turtle.dot(200, 'red')

    # Placing input() in my code pauses the program 
    # I have to hit 'enter' in order to for the code to move to the next block
    input()
    turtle.color('yellow')
    turtle.pensize(3)
    turtle.begin_fill()
    turtle.circle(180)
    turtle.end_fill()

    input()
    turtle.begin_fill()
    turtle.color('green')
    turtle.circle(100)
    turtle.end_fill()

    input()
    turtle.begin_fill()
    turtle.color('black')
    turtle.circle(80)
    turtle.end_fill()
    
    input()
    turtle.dot(120, 'orange red')
    
    input()
    turtle.dot(100, 'DarkGreen')
    
    input()
    turtle.dot(75, 'dark turquoise')

# This outdented block of code is always executed.
# Did the turtle move to another location?
turtle.penup()
turtle.goto(0,200)
turtle.pendown()

# creats a variable called style which I will use to set a font, a font size, and a style (italics)
style = ('Courier New', 20 , 'italic')

# ----------------------------------------------------

# asks user for another integer
t = int(input("Please enter an integer greater than 100: "))

turtle.delay(20)

if t <= 100:
    print("Your number must be greater than 100!")
    t = int(input('Please try again. Enter another number >>> '))

if t < 200:
    turtle.pencolor('violet red')
    # prints the string, centered, using the style variable I created on line 90
    turtle.write('That\'s all folks!', align='center', font=style)

if t < 500:
    turtle.penup()
    turtle.goto(0,-250)
    turtle.pendown()
    turtle.color('blue')
    turtle.write('See ya later!', font=style, align='left')

if t >= 500:
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.pencolor('white')
    turtle.write('That\'s all folks!', font=style, align='center')

# -----------------------------------------------------------

# prints the values of x, y, z, and t.
print('Your x value is: ', x)
print('Your y value is: ', y)
print('Your z value is: ', z)
print('Your t value is: ', t)

input()
