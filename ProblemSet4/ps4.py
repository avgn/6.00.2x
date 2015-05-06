# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False}
    mutProb = 0.005
    delays = [300, 150, 75, 0]
    f, axarr = pylab.subplots(2, 2)
    x_plot = []

    for delay in delays:
        FinalPopSize = [0.0 for x in range(numTrials)]
        for trial in range(numTrials):
            viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for n in range(numViruses)]
            patient = TreatedPatient(viruses, maxPop)
            for i in range(delay):
                patient.update()
            patient.addPrescription('guttagonol')
            for j in range(delay, delay+150):
                patient.update()
            FinalPopSize[trial] = patient.getTotalPop()
        x_plot.append(FinalPopSize)

    axarr[0, 0].hist(x_plot[0])
    axarr[0, 1].hist(x_plot[1])
    axarr[1, 0].hist(x_plot[2])
    axarr[1, 1].hist(x_plot[3])
    pylab.show()

    # pylab.plot(avgPopSize, label = 'avg pop size')
    # pylab.plot(avgGuttagonolResistantPop, label = 'avg pop size guttagonol-resistant')
    # pylab.xlabel("Time")
    # pylab.ylabel("Average Population Size")
    # pylab.title("Average Size of the Virus Populations")
    # pylab.legend(loc = 'best')
    # pylab.show()


#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = 0.005
    delays = [300, 150, 75, 0]
    f, axarr = pylab.subplots(2, 2)
    x_plot = []

    for delay in delays:
        FinalPopSize = [0.0 for x in range(numTrials)]
        for trial in range(numTrials):
            viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for n in range(numViruses)]
            patient = TreatedPatient(viruses, maxPop)
            for i in range(150):
                patient.update()
            patient.addPrescription('guttagonol')
            for j in range(150, 150+delay):
                patient.update()
            patient.addPrescription('grimpex')
            for k in range(150+delay, 300+delay):
                patient.update()
            FinalPopSize[trial] = patient.getTotalPop()
        x_plot.append(FinalPopSize)

    axarr[0, 0].hist(x_plot[0])
    axarr[0, 1].hist(x_plot[1])
    axarr[1, 0].hist(x_plot[2])
    axarr[1, 1].hist(x_plot[3])
    pylab.show()
    return x_plot
