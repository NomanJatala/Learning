import random
number = random.randint(1, 100)
count = 0
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    count += 1
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! guess again")
    elif guess == number:
        print("You win the game")
        break
    else:
        print("Plese Enter a valid input")

print(f"Attempts : {count}")