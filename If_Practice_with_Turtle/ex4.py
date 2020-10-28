x = int(input('Enter a number: '))

if x <= 4:
    x += 2 # this is equivalent to x = x + 2
    print('\nThe value of x + 2 is', x, '\n')

# What is the value of x at this point?
input('Is the new value of x greater than 4? Y or N? ')

if x > 4:
    x *= 4 # what is this equivalent to?
    print('\nThe value of x times 4 is', x)

print("All done.")
