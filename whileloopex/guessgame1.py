import random

secret_number =  random.randint(1,10)

my_guess = int(input("You've got one chance. Guess the secret number between 1 and 10 >>> "))

count = 0

while my_guess != secret_number:   
    
  my_guess = int(input("You've got another chance. Guess the secret number between 1 and 10 >>> "))

  count += 1

  if my_guess == secret_number:
    print("You got it!")
        
  elif my_guess > secret_number:
    print('Your guess was too high!')

  else:
    print('Your guess was too low!')

print("Woo hoo! The secret number is:", secret_number, end = '. ')
print("You guessed", count,"times.")
