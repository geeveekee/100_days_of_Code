import pandas as pd
from icecream import ic

data = pd.read_csv("100_days_of_Code\d28\/nato_phonetic_alphabet.csv")

name_dict = {row.letter: row.code for(index, row) in data.iterrows()}


your_name = input("Please enter your name")
phonetic_name = [name_dict[letter] for letter in your_name.upper()]
print(f"Your phonetic name is: {phonetic_name}")



