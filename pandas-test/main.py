from itertools import count
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

print(data["Primary Fur Color"].value_counts())

gray = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

color_dict = {
    "color":["gray", "cinnamon", "black"],
    "number": [gray, cinnamon, black]
}

df = pandas.DataFrame(color_dict)
df.to_csv("count_color.csv")





