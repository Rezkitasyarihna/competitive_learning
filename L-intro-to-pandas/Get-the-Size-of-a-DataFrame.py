# DataFrame players:
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | player_id   | int    |
# | name        | object |
# | age         | int    |
# | position    | object |
# | ...         | ...    |
# +-------------+--------+
# Write a solution to calculate and display the number of rows and columns of players.

# Return the result as an array:

# [number of rows, number of columns]

# The result format is in the following example.

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    # return [players.shape[0],players.shape[1]]
    # return list(players.shape)
    return [len(players), len(players.columns)]
