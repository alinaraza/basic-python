import random

randNumber = random.randint(1,100)

print("Welcome to the high-low game")

maxTries = 10


for guesses in range(1,maxTries+1) :
    guess = int(input("Guess a number between 1 and 100 \n"))

    if guess > randNumber:
        print("that's too high")
        print("you have {} tries left".format(maxTries-guesses))
    elif (guess < randNumber):
        print("that's too low")
        print("you have {} tries left".format(maxTries-guesses))
    else:
        print("you win! it took you {} tries".format(guesses))
        exit()
    
print("aw you lost")