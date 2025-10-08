

def repeatedspots(x,y,z):
    sharedspaces = 0

    for i in range(x):
        if y[i] == "C" and z[i] == "C":
            sharedspaces = sharedspaces+1
    print(f"You had {sharedspaces} spaces occupied on both days.")
repeatedspots(int(input("Enter your number of vehicles: ")), input("Enter occupied / unoccupied... C or a period for yesterday: "),input("Enter occupied / unoccupied... C or a period for today: "))
