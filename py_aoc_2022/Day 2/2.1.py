import pandas as pd

GAME_RULE_SCORE = {
    "AX" : 3,
    "AY" : 6,
    "AZ" : 0,
    "BX" : 0,
    "BY" : 3,
    "BZ" : 6,
    "CX" : 6,
    "CY" : 0,
    "CZ" : 3,
}
DRAW_SCORE = {"X": 1, "Y": 2, "Z": 3}


def getRoundScore(opp, me):
    gameRuleScore = GAME_RULE_SCORE[opp + me]
    drawScore = DRAW_SCORE[me]
    
    return gameRuleScore + drawScore


data = pd.read_csv("input.txt", sep=" ", header=None, names=["opponent", "me"])

data.apply(lambda row: getRoundScore(row.opponent, row.me), axis=1).agg(sum)
