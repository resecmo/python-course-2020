import numpy as np
import pandas as pd


file1 = input()
file2 = input()

games = pd.read_csv(file1, delimiter=";")
rates = pd.read_csv(file2, delimiter=";")

games["mark"] = 0
for game_id in games["id"]:
    game_rates = rates[rates["id"] == game_id]
    avg_mark = np.mean(game_rates["mark"])
    games.loc[games["id"] == game_id, "mark"] = avg_mark
games.sort_values(by="mark", inplace=True, ascending=False)

for name, mark in list(zip(games["name"].values, games["mark"].values))[:3]:
    print("{} {:.3f}".format(name, mark))

developers = pd.DataFrame(np.unique(games["company"].values), columns=["studio"])
developers["good_games"] = 0

good_game_developers = games.loc[games["mark"] > 8.0]["company"].to_numpy()
for dev in good_game_developers:
    developers.loc[developers["studio"] == dev, "good_games"] += 1
developers.sort_values(by="good_games", inplace=True, ascending=False)
print(*developers.to_numpy()[0])

"""
games001.csv
rates001.csv
"""