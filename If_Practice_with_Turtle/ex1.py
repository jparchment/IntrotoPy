# Define the variables x and y. In order to use a variable
# within our if block, we must first define it
# before the if block
x = int(input('Enter a number: '))
y = 0
if x <= 4:
    y = x ** 2
    print('The value of x squared is ', y)
print('The value of x is', x, 'which is not less than or equal to 4.')
print('Therefore, no code within the if block is executed.')
