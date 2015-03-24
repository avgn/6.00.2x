import random

def drawBalls():
    bucket = [0, 0, 0, 1, 1, 1]
    d1 = random.choice(bucket)
    bucket.pop(d1)
    d2 = random.choice(bucket)
    bucket.pop(d1)
    d3 = random.choice(bucket)
    bucket.pop(d3)
    if d1 + d2 + d3 == 0 or d1 + d2 + d3 == 3:
        return True
    else:
        return False

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    sameColor = 0
    for n in range(numTrials):
        if drawBalls():
            sameColor += 1
    return sameColor/float(numTrials)

print noReplacementSimulation(5000)