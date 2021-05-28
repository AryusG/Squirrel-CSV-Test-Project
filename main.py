# TODO Dataframe: Fur Color, Count

import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
colors = ['Gray', 'Cinnamon', 'Black']
s_count = []

for color in colors:
    color_squirrels = data["Primary Fur Color"] == color
    true_amount = []
    for squirrel in color_squirrels:
        if squirrel:
            true_amount.append(squirrel)
    s_count.append(len(true_amount))

squirrel_count_dict = {
    "Primary Fur Color": colors,
    "Count": s_count
}

df = pd.DataFrame(squirrel_count_dict)
df.to_csv("squirrel_count.csv")