import pylab

# You may have to change this path
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    proportions = []
    for word in wordList:
        for letter in word:
            nwords = 0
            if letter in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
                nwords += 1
        proportions.append(nwords/float(len(word)))
    pylab.hist(proportions, numBins)
    pylab.title('Proportion of vowels in each word of a list of words')
    pylab.xlabel('Proportion of vowels in a word')
    pylab.ylabel('Numer of words')
    pylab.show()

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
