def lang(x):
    numberS = 0
    numberT = 0
    for char in x:
        if char == "S" or char == "s":
            numberS = numberS+1
        if char == "T" or char == "t":
            numberT=numberT+1
    if numberT > numberS:
        print("Your input is likely English.")
    elif numberS >= numberT:
        print("Your text is likely French.")
lang(input("Enter your text: "))








