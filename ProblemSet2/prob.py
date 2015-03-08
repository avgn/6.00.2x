import random

def rollDie():
    """Return a randomly chosen int between 1 and 6."""
    return random.choice([1, 2, 3, 4, 5, 6])

def rollN(n):
    result = ""
    for i in range(n):
        result = result + str(random.choice([1, 2, 3, 4, 5, 6]))
    return result

def flipCoin():
    return random.choice([0, 1])

def flipN(n):
    result = ''
    for i in range(n):
        result = result + str(flipCoin())
    return result

def flip(numFlips):
    heads = 0.0
    for i in range(numFlips):
        if random.random() < 0.5:
            heads += 1
    return heads/numFlips
    
def flipSim(numFlipsPerTrial, numTrials):
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean = sum(fracHeads)/len(fracHeads)
    sd = stdDev(fracHeads)
    return (fracHeads, mean, sd)

def labelPlot(numFlips, numTrials, mean, sd):
    pylab.title(str(numTrials) + ' trials of ' +
    str(numFlips) + ' flips each')
    pylab.xlabel('Fraction of Heads')
    pylab.ylabel('Number of Trials')
    xmin, xmax = pylab.xlim()
    ymin, ymax = pylab.ylim()
    pylab.text(xmin + (xmax-xmin)*0.02, (ymax-ymin)/2,
    'Mean = ' + str(round(mean, 4))
    + '\nSD = ' + str(round(sd, 4)))
    
def makePlots(numFlips1, numFlips2, numTrials):
    val1, mean1, sd1 = flipSim(numFlips1, numTrials)
    pylab.hist(val1, bins = 20)
    xmin, xmax = pylab.xlim()
    ymin, ymax = pylab.ylim()
    labelPlot(numFlips1, numTrials, mean1, sd1)
    pylab.figure()
    val2, mean2, sd2 = flipSim(numFlips2, numTrials)
    pylab.hist(val2, bins = 20)
    pylab.xlim(xmin, xmax)
    ymin, ymax = pylab.ylim()
    labelPlot(numFlips2, numTrials, mean2, sd2)
    pylab.show()
    
def stdDev(X):
    """Assumes that X is a list of numbers.
    Returns the standard deviation of X"""
    mean = float(sum(X))/len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5
    
def showErrorBars(minFlips, maxExp, numTrials):
    means, sds = [], []
    xVals, yVals = [], []
    exp = minFlips
    while exp <= maxExp:
        xVals.append(2**exp)
        fracHeads, mean, sd = flipSim(2**exp, numTrials)
        means.append(mean)
        sds.append(sd)
        exp += 1
    pylab.errorbar(xVals, means, yerr = 2*pylab.array(sds))
    pylab.semilogx()
    pylab.title('Mean Fraction of Heads (' +
    str(numTrials) + ')')
    pylab.xlabel('Number of flips')
    pylab.ylabel('Fraction of heads & 95% confidence')
def clear(n, p, steps):
    """Assumes n & steps positive ints, p a float.
    n: the initial number of a molecule being cleared
    p: the probability of a molecule being cleared
    steps: the length of the simulation"""
    numRemaining = [n]
    for t in range(steps):
        numRemaining.append(n*((1-p)**t))
    pylab.plot(numRemaining)
    pylab.xlabel('Time')
    pylab.ylabel('Molecules Remaining')
    pylab.title('Clearance of Drug')
def collisionProb(n, k):
    prob = 1.0
    for i in range(1, k):
        prob = prob * ((n-i)/float(n))
    return 1 - prob
def simInsertions(numIndices, numInsertions):
    #Returns 1 if there is a collision in numInsertions
    #0 otherwise.
    choices = range(numIndices) #list of possible indices
    used = []
    for i in range(numInsertions):
        hashVal = random.choice(choices)
        if hashVal in used: #there is a collision
            return 1
        else:
            used.append(hashVal)
    return 0
def findProb(numIndices, numInsertions, numTrials):
    collisions = 0.0
    for t in range(numTrials):
        collisions += simInsertions(numIndices, numInsertions)
    return collisions/numTrials
