import pylab
import random

def getData(fileName):
    dataFile = open(fileName, 'r')
    distances = []
    masses = []
    discardHeader = dataFile.readline()
    for line in dataFile:
        d, m = line.split()
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return (masses, distances)

def plotData(fileName):
    xVals, yVals = getData(fileName)
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals*9.81
    pylab.plot(xVals, yVals, 'bo', label = 'Measured displacements')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('Force (Newton)')
    pylab.ylabel('Distance (meters)')

#plotData('springData.txt')
#pylab.show()

def testErrors(ntrials=100000, npts=100):
    results = [0] * ntrials
    for i in xrange(ntrials):
        s = 0
        for j in xrange(npts):
            s += random.uniform(-1,1)
        results[i] = s
    # plot results in a histogram
    pylab.hist(results, bins=50)
    pylab.title('Sum of 100 random points -- Triangular PDF (10,000 trials)')
    pylab.xlabel('Sum')
    pylab.ylabel('Number of trials')

#testErrors()
#pylab.show()

def rSquare(measured, estimate):
    """measured: one dimensional array of measured values
       estimate: one dimensional array of predicted values"""
    SEE = ((estimate - measured)**2).sum()
    mMean = measured.sum()/float(len(measured))
    MV = ((mMean - measured)**2).sum()
    return 1 - SEE/MV

def fitData(fileName):
    xVals, yVals = getData(fileName)
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals*9.81
    pylab.plot(xVals, yVals, 'bo', label = 'Measured points')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('Force (Newton)')
    pylab.ylabel('Distance (meters)')
    a, b = pylab.polyfit(xVals, yVals, 1)
    estYVals = a*xVals + b
    k = 1/a
    pylab.plot(xVals, estYVals, label = 'Linear fit, k = ' 
        + str(round(k, 5)) + ', R2 = '
        + str(round(rSquare(yVals, estYVals), 4)))
    pylab.legend(loc = 'best')

#fitData('springData.txt')
#pylab.show()

def fitData1(fileName):
    xVals, yVals = getData(fileName)
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals*9.81
    pylab.plot(xVals, yVals, 'bo', label = 'Measured points')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('|Force| (Newton)')
    pylab.ylabel('Distance (meters)')
    a, b = pylab.polyfit(xVals, yVals, 1)
    estYVals = a*xVals + b
    pylab.plot(xVals, estYVals, label = 'Linear fit')
    a, b, c, d = pylab.polyfit(xVals, yVals, 3)
    estYVals = a*(xVals**3) + b*(xVals**2) + c*xVals + d
    pylab.plot(xVals, estYVals, label = 'Cubic fit')
    pylab.legend(loc = 'best')

#fitData1('springData.txt')
#pylab.show()

def fitData2(fileName):
    xVals, yVals = getData(fileName)
    extX = pylab.array(xVals + [1.05, 1.1, 1.15, 1.2, 1.25])
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals*9.81
    extX = extX*9.81
    pylab.plot(xVals, yVals, 'bo', label = 'Measured points')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('|Force| (Newton)')
    pylab.ylabel('Distance (meters)')
    a, b = pylab.polyfit(xVals, yVals, 1)
    estYVals = a*extX + b
    pylab.plot(extX, estYVals, label = 'Linear fit')
    a, b, c, d = pylab.polyfit(xVals, yVals, 3)
    estYVals = a*(extX**3) + b*(extX**2) + c*extX + d
    pylab.plot(extX, estYVals, label = 'Cubic fit')
    pylab.legend(loc = 'best')

#fitData2('springData.txt')
#pylab.show()

def fitData3(fileName):
    xVals, yVals = getData(fileName)
    xVals = pylab.array(xVals[:-6])
    yVals = pylab.array(yVals[:-6])
    xVals = xVals*9.81
    pylab.plot(xVals, yVals, 'bo', label = 'Measured points')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('|Force| (Newton)')
    pylab.ylabel('Distance (meters)')
    a, b = pylab.polyfit(xVals, yVals, 1)
    estYVals = a*xVals + b
    k = 1/a
    pylab.plot(xVals, estYVals, label = 'Linear fit, k = ' 
        + str(round(k, 5)) + ', R2 = '
        + str(round(rSquare(yVals, estYVals), 4)))
    pylab.legend(loc = 'best')

fitData3('springData.txt')
pylab.show()