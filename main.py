import random

secret_num = random.randint(0, 10)
guesses = 0

while True:
    guesses += 1
    guess_number = input("Guess a number from 1 - 10? ")
    
    if guess_number.isdigit():
        guess_number = int(guess_number)
    else:
        print("Please type in a number next time")
        continue
        
    if guess_number <= 0:
        print("Try numbers above 0")
    elif guess_number == secret_num:
        print(f"You guessed right! Kudos")
        break
    else:
        print("Sorry!! Try again (Guess numbers btw 1-10)")
        
print(f"You got it, at {guesses} guesses, The secret number is {secret_num}")
