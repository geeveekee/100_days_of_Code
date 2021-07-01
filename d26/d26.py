import csv
import pandas as pd

data = pd.read_csv("100_days_of_Code\d26\/\/2018_Central_Park_Squirrel_Census_Squirrel_Data.csv")


grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinammon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinammon", "Black"],
    "Count": [grey_squirrels, red_squirrels, black_squirrels]
}

df = pd.DataFrame(data_dict)
df.to_csv("100_days_of_Code\d26/squirrel_count.csv")


