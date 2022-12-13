import pandas as pd
from pandas import DataFrame
import sys


def createCrateStack(crateSerie: pd.Series) -> list[str]:
    stack: list[str] = []

    # Scan the crate serie in reverse order to fill the stack
    for i in range(len(crateSerie)-1, -1, -1):
        crate = crateSerie[i]
        if (crate != ''):
            stack.append(crate)

    return stack


def createAColumnPerStack(line: str) -> list[str]:
    NUMBER_OF_CHAR_BETWEEN_EACH_STACK: int = 4
    return [line[index:index+3] for index in range(0, len(line), NUMBER_OF_CHAR_BETWEEN_EACH_STACK)]


def getStacksRepresentationOfSupplies(drawing: list[str]) -> list[list[str]]:
    stacks: list[list[str]] = []

    cleanedDrawing = [createAColumnPerStack(line) for line in drawing]
    pd.DataFrame(cleanedDrawing) \
        .apply(lambda crateSerie: crateSerie.str.replace(r"[\[\]\s]", "", regex=True)) \
        .apply(lambda crateSerie: stacks.append(createCrateStack(crateSerie)))

    return stacks


def isLastLineOfSchema(line: str) -> bool:
    return line[1] == "1"


def parseInputDataAsStacks(filePath: str) -> tuple[list[list[str]], int]:
    stacks: list[list[str]] = []
    schema: list[str] = []
    numberOfDrawingLines: int = 0

    with open(filePath, 'r') as f:
        inputFileLines = f.readlines()

    for line in inputFileLines:
        numberOfDrawingLines += 1

        if (isLastLineOfSchema(line)):
            stacks = getStacksRepresentationOfSupplies(schema)
            return stacks, numberOfDrawingLines
        else:
            schema.append(line)

    return stacks, numberOfDrawingLines


def applyCrateOperationWithCrane9000(stacks: list[list[str]], operation: list[int]) -> list[list[str]]:
    numberOfCratesToMove: int = operation[0]
    fromStack: int = operation[1]
    toStack: int = operation[2]

    for _ in range(numberOfCratesToMove):
        crateMoved = stacks[fromStack - 1].pop()
        stacks[toStack - 1].append(crateMoved)

    return stacks


def applyCrateOperationWithCrane9001(stacks: list[list[str]], operation: list[int]) -> list[list[str]]:
    numberOfCratesToMove: int = operation[0]
    fromStack: int = operation[1]
    toStack: int = operation[2]

    cratesMoved = stacks[fromStack - 1][-numberOfCratesToMove:]
    for _ in range(numberOfCratesToMove):
        stacks[fromStack - 1].pop()
    stacks[toStack - 1].extend(cratesMoved)

    return stacks


def part1(inputDf: DataFrame, stacks: list[list[str]]) -> str:
    for operation in inputDf.values:
        stacks = applyCrateOperationWithCrane9000(stacks, operation)

    result: str = ""
    for stack in stacks:
        result += stack.pop()

    return result


def part2(inputDf: DataFrame, stacks: list[list[str]]) -> str:
    for operation in inputDf.values:
        stacks = applyCrateOperationWithCrane9001(stacks, operation)

    result: str = ""
    for stack in stacks:
        result += stack.pop()

    return result


if __name__ == "__main__":
    filePath: str = "input"

    stacks, numberOfRowsToSkip = parseInputDataAsStacks(filePath)

    inputDf: DataFrame = pd.read_csv(filePath, sep=' ', header=None, skiprows=numberOfRowsToSkip)
    inputDf.drop(inputDf.columns[[0, 4, 2]], axis=1, inplace=True)
    inputDf.astype("int64")

    match sys.argv[1]:
        case '1': print(part1(inputDf, stacks))
        case '2': print(part2(inputDf, stacks))
        case other: print("Type 1 or 2")
