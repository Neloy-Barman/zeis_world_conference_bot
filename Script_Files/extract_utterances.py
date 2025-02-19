"""
    We are going to use this file to fetch the utterances from the mannually processed content sheets.
    Although this file will help to extract all the utterances, but still mannual checks are needed to ensure everything is done properly.
"""

import pandas as pd
from tqdm import tqdm

# Reading CSV file

# Dynamic
# df = pd.read_csv("Content_Sheets/Mannually_Processed/Keynote_Speakers.csv")
df = pd.read_csv("Content_Sheets/Mannually_Processed/Guest_of_Honour.csv")


columns = df.columns
print(f"Columns: {columns}")

df = df.drop(columns=['Topic', 'Answer'])
print(f"After dropping redundant columns: {df.columns}")

# English Utterances Column
eng_utt_columns = ['Question', 'English Version 1', 'English Version 2'] 

# Hinglish Utterances Column
hingish_utt_columns = ['Hinglish Version 1', 'Hinglish Version 2', 'Hinglish Version 3'] 


def create_utter_df(
  df,
  utt_columns
):
    utterances = []
    for i,row in tqdm(df.iterrows(), desc="Utterances Extraction going on...", total=len(df)):
        for col in utt_columns:
            temp = row[col]
            if temp not in utterances:
                utterances.append(temp)
                
    print(f"Number of extracted utterances: {len(utterances)}")
    # print(f"All the extracted utterances: {utterances}")

    new_df = pd.DataFrame(
        columns=['Utterances'], 
        data={
            'Utterances': utterances
        }
    )
    return new_df


# Static
file_path = "Utterances/"
eng_file_name = "English_Utt.csv"
hinglish_file_name = "Hinglish_Utt.csv"

# Dynamic
# topic = "Keynote_Speakers"

topic = "Guest_of_Honour"


# English Utterances
new_df = create_utter_df(
    df=df,
    utt_columns=eng_utt_columns
)
new_df.to_csv(f"{file_path}/{topic}/{eng_file_name}", index=False)
print("English Utterances processed successfully........!!\n")

# Hinglish Utterances
new_df = create_utter_df(
    df=df,
    utt_columns=hingish_utt_columns
)
new_df.to_csv(f"{file_path}/{topic}/{hinglish_file_name}", index=False)
print("Hinglish Utterances processed successfully........!!\n")



"""
    Powershell Command: - python Script_Files/extract_utterances.py
"""