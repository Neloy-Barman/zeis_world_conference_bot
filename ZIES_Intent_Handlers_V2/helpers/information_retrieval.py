import pandas as pd
from fuzzywuzzy import fuzz

# Fuzzy-Wuzzy Performing
def perform_fuzzywuzzy(result, slot, column):

    # A list to store scores
    score_list = []
    string_1 = str(slot).lower() 

    print(f"String 1: {string_1}")

    # Iterating through csv file 
    for i, row in result.iterrows():
        print(f"Index, Row: {i}, {row}")

        string_2 = str(row[column]).lower()
        print(f"String 2: {string_2}")
        
        # Score Finding using Fuzzy-wuzzy 
        scores = [
            fuzz.ratio(string_1, string_2),
            fuzz.partial_ratio(string_1, string_2),
            fuzz.token_sort_ratio(string_1, string_2),
            fuzz.token_set_ratio(string_1, string_2)
        ]
        print(f"Scores: {scores}")
        score = max(scores)
        print(f"Max Score: {score}")

        # Appending score to the list
        score_list.append(score)
        print(f"Score List: {score_list}")
        print("---------------------")
    # Finding Maximum value from list
    maxScore = max(score_list)
    print(f"Max Score: {maxScore}")

    # If maximum score is greater than 65
    if maxScore>65:
        # Finding index of the score
        indexOf = score_list.index(maxScore)
        print(f"Index: {indexOf}")

        # Fetching row of the index 
        answer = result.iloc[indexOf]
        print(f"Fetched Row: {answer}")
    else:
        indexOf = None
        answer = None
    
    return indexOf, answer


