import random
s = True
# start
while s:
    start = str(input("In this game, you have to guess the number between 1 and 1200. OK TO START"))
    if start == "OK":
        print("Let's go !")
        s = False
    elif start != "OK":
        s = False
        s = True


#game
def res():
    prix = random.randint(1, 1200)
    running = True
    while running:
    
        nombre = int(input("Your guess: "))
        if nombre == prix:
            print("That's right !")
            running = False
        elif nombre < prix:
            print("Higher.")
        elif nombre > prix:
            print("Lower.")
#restart
    relancer = int(input("End of the game. Restart ? 1 = YES , 2 = NO"))
    if relancer == 1:
        running = True
        res()

    elif relancer == 2:
        print("Goodbye")  
        return  

res()