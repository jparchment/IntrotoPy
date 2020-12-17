import random

secret_number =  random.randint(1,10)

my_guess = int(input("\nYou've got one chance. Guess the secret number between 1 and 10 >>> "))

count = 1

while my_guess != secret_number:   
    
  my_guess = int(input("\nYou've got another chance. Guess the secret number between 1 and 10 >>> "))

  count += 1

  if my_guess == secret_number:
    print("\nYou got it!")
        
  elif my_guess > secret_number:
    print('\nYour guess was too high!')

  else:
    print('\nYour guess was too low!')

print("\nWoo hoo! The secret number is:", secret_number, end = '. ')
print("You guessed", count,"times.")
