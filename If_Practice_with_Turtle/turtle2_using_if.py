import turtle

turtle.bgcolor('black')
turtle.delay(45)

x = int(input('enter a number: '))
if x <= 3:
    turtle.dot(400, 'purple')
   
if x > 3:
    turtle.dot(200, 'chartreuse')
# ------------------------------------------------

y = int(input('enter another number: '))
turtle.delay(45)
if y < 0:
    turtle.dot(250, 'blue')

if y > 0:
    turtle.dot(500, 'orange')

if y == 0:
    turtle.color('green')
    turtle.begin_fill()
    turtle.left(120)
    turtle.forward(50)
    turtle.left(120)
    turtle.forward(50)
    turtle.left(120)
    turtle.forward(50)
    turtle.end_fill()

# -----------------------------------------------------
z = float(input('Enter a decimal: '))
turtle.delay(10)
if z != 7.5:
    turtle.dot(200, 'red')
    turtle.color('yellow')
    turtle.pensize(3)
    turtle.begin_fill()
    turtle.circle(180)
    turtle.end_fill()
    turtle.begin_fill()
    turtle.color('green')
    turtle.circle(100)
    turtle.end_fill()
    turtle.begin_fill()
    turtle.color('black')
    turtle.circle(80)
    turtle.end_fill()
    turtle.dot(120, 'orange red')
    turtle.dot(100, 'DarkGreen')
    turtle.dot(75, 'dark turquoise')

turtle.color('violet red')
turtle.penup()
turtle.goto(0,200)
turtle.pendown()
style = ('Courier New', 20 , 'italic')

# ----------------------------------------------------
t = int(input("Please enter an integer greater than 100: "))
turtle.delay(20)
if t <= 100:
    print("Your number must be greater than 100!")
    t = int(input('Please try again. Enter another number >>> '))

if t < 200:
    turtle.pencolor('black')
    turtle.write('That\'s all folks!', align = 'center', font=style)

if t < 500:
    turtle.penup()
    turtle.goto(0,-250)
    turtle.pendown()
    turtle.color('light blue')
    turtle.write('See ya later!', font=style, align='left')

if t >= 500:
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.pencolor('white')
    turtle.write('That\'s all folks!', font=style, align='center')

# -----------------------------------------------------------

print('Your x value is: ", x)
print('Your y value is: ", y)
print('Your z value is: ", z)
print('Your t value is: ", t)

input()
