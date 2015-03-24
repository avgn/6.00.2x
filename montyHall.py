import random

def montyChoose(guessDoor, prizeDoor):
    if guessDoor != 1 and prizeDoor1 != 1 and prizeDoor2 != 1:
        return 1
    if guessDoor != 2 and prizeDoor1 != 2 and prizeDoor2 != 2:
        return 2
    if guessDoor != 3 and prizeDoor1 != 3 and prizeDoor2 != 3:
        return 3
    return 4

def simMontyAll(numTrials, chooseFcn):
    stickWins, switchWins, noWin = (0, 0, 0)
    prizeDoorChoices = [1, 2, 3, 4]
    guessChoices = [1, 2, 3, 4]
    for t in range(numTrials):
        prizeDoor1 = random.choice([1, 2, 3, 4])
        prizeDoor2 = random.choice([1, 2, 3, 4].pop(prizeDoor(1)))
        guess = random.choice([1, 2, 3, 4])
        toOpen = chooseFcn(guess, prizeDoor)
        if toOpen == prizeDoor:
            no