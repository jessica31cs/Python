#dictionary: keys are the words of song lyrics and the values are a list of the list number it appears on
#hint: line 0 is the first line
def lineIndex(fName):
    inF = open(fName)
    d = {}
    lines = inF.readlines()
    for index in range(len(lines)):
        words = lines[index].split()
        for word in words:
            if word not in d:
                d[word] = [index]
            else:
                if index not in d[word]:
                    d[word].append(index)
    inF.close()
    return d
print(lineIndex("song.txt"))
        
    
