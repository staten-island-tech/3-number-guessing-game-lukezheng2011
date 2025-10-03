import random

###randomnum = random.randint(1,100)

randomnum = 1241241421






















guessed = 0
guesslist = []

while guessed == 0:
    inpoot = int(input("Enter a number: "))

    if inpoot > randomnum:
        guesslist.append(inpoot)
        print("The number is LESS than your input")
        print(f"You've guessed {guesslist}")

    elif inpoot < randomnum:
        guesslist.append(inpoot)
        print("The number is MORE than your input")
        print(f"You've guessed {guesslist}")

    else:
        print(f"You have found the number. It was {randomnum} Your guesses were {guesslist}")
        guessed = 1
















































