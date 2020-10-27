# Define the variables x and y. In order to use a variable
# within our if block, we must first define it
# before the if block
x = int(input('Enter a number: '))
y = 0

# code which will be executed if the given condition is True.
if x <= 4:
    y = x ** 2
    print('The value of x squared is ', y)
 
# This statement is outdented and is not part of the if block.
# It will always be executed.
print('The value of x is', x)
