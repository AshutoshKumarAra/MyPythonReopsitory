import random
num = random.randint(1,56)
tries = 0

while True:   #Infinite loop.
    guess = int(input(f"Please guess your number between 1 and 10"))

    if num == guess:
        tries += 1
        print(f"You have guess the number correctly.")
        break
    elif num > guess:
        print(f"The number you have guessed is slighlty lower.")
        tries += 1
    elif num < guess:
        print(f"The number you have guessed in slighlty higher.")
        tries += 1
    else:
        tries += 1
        print(f"The number you have guessed is wrong.")