import pandas as pd
import numpy as np

GAME_SCORE_MATRIX = np.array(
    ((3, 0, 6),
     (6, 3, 0),
     (0, 6, 3)))

GAME_RULE_SCORE = {"X": 0, "Y": 3, "Z": 6}
DRAW_INDEX = {"A": 0, "B": 1, "C": 2}

def getRoundScore(oppDraw, result):
    oppDrawIndex = DRAW_INDEX[oppDraw]
    resultScore = GAME_RULE_SCORE[result]
    myDrawIndex = np.where(GAME_SCORE_MATRIX[:,oppDrawIndex] == resultScore)[0][0]
    myDrawScore = myDrawIndex + 1
    
    return GAME_RULE_SCORE[result] + myDrawScore

data = pd.read_csv("input.txt", sep=" ", header=None, names=["opponent", "me"])

data.apply(lambda row: getRoundScore(row.opponent, row.result), axis=1).agg(sum)
