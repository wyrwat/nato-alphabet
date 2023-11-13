import pandas as pd

nato_alphabet_df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dic = {row["letter"]: row["code"] for (index, row) in nato_alphabet_df.iterrows()}


def generate_phonetic():
    user_input = input("Enter your name: ").upper()
    try:
        phonetic_code = [nato_alphabet_dic[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_code)


generate_phonetic()
