import random
import pylab

class Location:

    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'


class Field:

    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc

    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        # use move method of location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)

    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]


class Drunk:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'This drunk is named ' + self.name

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0,1.0), (0.0,-1.0), (1.0,0.0), (-1.0,0.0)]
        return random.choice(stepChoices)

class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0, 1.0), (0.0, -2.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

class EWDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

class DrunkKinds(object):
    kinds = [UsualDrunk, ColdDrunk, EWDrunk]

class styleIterator(object):
    def __init__(self, styles):
        self.index = 0
        self.styles = styles

    def nextStyle(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) - 1:
            self.index = 0
        else:
            self.index += 1
        return result


def walk(f, d, numSteps):
    """Assumes: f a Field, d a Drunk in f, and numSteps an int > 0.
    Moves d numSteps step times, and returns the difference between
    the final location and the location at the start of the walk."""
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))

def simWalks(numSteps, numTrials, dClass):
    """Assumes numSteps, numTrials ints > 0. dClass subclass of Drunk
    Simulates numTrials walks of numSteps each.
    Returns a list of the final distances for each trial"""
    homer = dClass('Homer')
    origin = Location(0.0, 0.0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(homer, origin)
        distances.append(walk(f, homer, numSteps))
    return distances

def drunkTest(numTrials, dClass):
    """Assumes numTrials and int >=0, dClass a subclass of Drunk
    Runs some tests of simWalks"""
    for numSteps in [10, 100, 1000, 10000]:
        distances = simWalks(numSteps, numTrials, dClass)
        print (dClass.__name__ + ' random walk of '
            + str(numSteps) + ' steps')
        print ' Mean =', sum(distances)/len(distances),\
            'CV =', CV(distances)
        print ' Max =', max(distances), 'Min =', min(distances)

def simDrunk(numTrials, dClass, numStepsList):
    meanDistances = []
    cvDistances = []
    for numSteps in numStepsList:
        print 'Starting simulation of', numSteps, 'steps'
        trials = simWalks(numSteps, numTrials, dClass)
        mean = sum(trials)/float(len(trials))
        meanDistances.append(mean)
        cvDistances.append(stdDev(trials)/mean)
    return (meanDistances, cvDistances)

def simAll(numTrials):
    numStepsList = [10, 100, 1000, 10000, 100000]
    styleChoice = styleIterator(('b-', 'r:', 'm-.'))
    for dClass in DrunkKinds.kinds:
        curStyle = styleChoice.nextStyle()
        print 'Starting simulation of', dClass.__name__
        means, cvs = simDrunk(numTrials, dClass, numStepsList)
        cvSum = 0.0
        for cv in cvs:
            cvSum += cv
        cvMean = str(round(cvSum/len(cvs), 4))
        pylab.figure(1)
        pylab.plot(numStepsList, means, curStyle,
            label = dClass.__name__ + 
            '((CV = ' + cvMean + ')')
    pylab.figure(1)
    pylab.title('Average Distance from Origin ('
        + str(numTrials) + ' trials)')
    pylab.xlabel('Number of Steps')
    pylab.ylabel('Distance from Origin')
    pylab.legend(loc = 'best')
    pylab.semilogx()
    pylab.semilogy()



def stdDev(X):
    """Assumes that X is a list of numbers.
    Returns the standard deviation of X"""
    mean = float(sum(X))/len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5

def CV(X):
    mean = sum(X)/float(len(X))
    try:
        return stdDev(X)/mean
    except ZeroDivisionError:
        return float('NaN')


