import pandas as pd
import sys


def splitLine(line):
    slidePoint = int(len(line)/2)
    return line[:slidePoint], line[slidePoint:]


def getPriorityFromType(objectType):
    asciiCode = ord(objectType)
    if (asciiCode >= 97):
        # Lowercase
        return asciiCode - 96
    else:
        # Uppercase
        return asciiCode - 38


def getCommonLetter(giftLists):
    return list(set(giftLists[0]).intersection(*giftLists[1:]))[0]


def computePriority(giftLists):
    commonLetter = getCommonLetter(giftLists)
    return getPriorityFromType(commonLetter)


def part1(data):
    data["compartment1"], data["compartment2"] = zip(
        *data.content.apply(lambda line: splitLine(line)))

    result = data\
        .apply(lambda line: computePriority([line.compartment1, line.compartment2]), axis=1)\
        .agg(sum)

    return result


def part2(data):
    deceptionList = data.content.values
    result = 0

    for i in range(0, len(deceptionList), 3):
        result += computePriority([deceptionList[i], deceptionList[i+1], deceptionList[i+2]])

    return result


if __name__ == "__main__":
    data = pd.read_csv("input.txt", header=None, names=["content"])

    match sys.argv[1]:
        case '1': print(part1(data))
        case '2': print(part2(data))
        case other: print("Type 1 or 2")
