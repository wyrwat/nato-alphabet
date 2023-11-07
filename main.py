import pandas as pd

user_input = input("Enter your name: ").upper()
nato_alphabet_df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dic = {row["letter"]: row["code"] for (index, row) in nato_alphabet_df.iterrows()}

phonetic_code = [nato_alphabet_dic[letter] for letter in user_input]

print(phonetic_code)
