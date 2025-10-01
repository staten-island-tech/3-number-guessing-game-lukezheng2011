import random

randomnum = random.randint(1,10)



guessed = 0
guesslist = []

while guessed == 0:
    inpoot = input("Enter a number: ")

    if inpoot > randomnum:
        guesslist.append(f"")
        print("The number is LESS than your input")

    elif inpoot < randomnum:
        guesslist.append(inpoot)
        print("The number is MORE than your input")

    else:
        print(f"You have found the number. It was {randomnum}")

















































