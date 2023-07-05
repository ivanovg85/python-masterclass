import random

highest = 10
answer = random.randint(1, highest)

print("Please guess number between 1 and {}: ".format(highest))
guess = 0
guessCount = 0

while guess != answer:
    guess = int(input())
    guessCount += 1
    if guess == answer:
        print("Well done. You guessed in {} tries.".format(guessCount))
        break
    else:
        if guess == 0:
            print("You quit the game")
            break
        elif guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
