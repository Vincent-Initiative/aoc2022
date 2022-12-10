import pandas as pd


def splitLine(line):
    slidePoint=int(len(line)/2)
    return line[:slidePoint], line[slidePoint:]


def getPriorityFromType(objectType):
    asciiCode = ord(objectType)
    if(asciiCode >= 97):
        # Lowercase
        return asciiCode - 96
    else:
        # Uppercase
        return asciiCode - 38


def getCommonLetter(str1, str2):
    return list(set(str1).intersection(str2))[0]


def computePriority(c1, c2):
    commonLetter = getCommonLetter(c1, c2)
    return getPriorityFromType(commonLetter)


data = pd.read_csv("input.txt", sep=" ", header=None, names=["content"])

data.apply(lambda line: computePriority(line.compartment1, line.compartment2), axis=1).agg(sum)
