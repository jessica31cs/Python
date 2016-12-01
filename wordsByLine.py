#output: a word followed by a colon followed by the number of times it appears in the specific line
#ex: line: one fish two fish ---> output: one:1 fish:2 two:1

#First way
def wordsByLine(inFile, outFile):
    inF = open(inFile, 'r')
    outF = open(outFile, 'w')
    for line in inF:
        wordsList= line.split()
        d = {}
        for word in wordsList:
            d[word] = wordsList.count(word)
        for key in d:
            outF.write(key + ':' + str(d[key]) + ' ')
        outF.write("\n")
    inF.close()
    outF.close()
wordsByLine("words.txt","out.txt")
    
#Second way
def wordsByLine(inFile, outFile):
    inF = open(inFile, 'r')
    outF = open(outFile, 'w')
    for line in inF:
        originalList = line.split()
        uniqueWords = list(set(line.split()))
        for word in uniqueWords:
            outF.write(word + ":" + str(originalList.count(word)) + " ")
        outF.write("\n")
    inF.close()
    outF.close()
#wordsByLine("words.txt","out.txt")  
