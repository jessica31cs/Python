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
        
    
