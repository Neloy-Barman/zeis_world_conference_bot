import pandas as pd

folder_path = "Content_Sheets/Mannually_Processed_For_Fallback"

# # About Us
# data_path = "About_Us.csv"

# # Conference Info
# data_path = "Conference_Info.csv"

# # Contact Info
# data_path = "Contact_Info.csv"

# # Founder Info
# data_path = "Founder_Info.csv"

# # Guest of Honour 
# data_path = "Guest_of_Honour.csv"

# # Keynote Speakers 
# data_path = "Keynote_Speakers.csv"

# # Location Timings
# data_path = "Location_Timings.csv"

# # Services 
# data_path = "Services.csv"

# # Sponsors Or Partners 
# data_path = "Sponsors_Or_Partners.csv"

# df = pd.read_csv(f"{folder_path}/{data_path}")

# # Columns
# columns = df.columns
# print(f"Columns: {columns}")

# # Dataframe Shape
# shape = df.shape
# print(f"Dataframe Shape: {shape}")

# # TB Report 2024
# columns_to_be_removed = ['Topic']

# # Removing columns
# df = df.drop(columns_to_be_removed, axis=1)

# # Columns
# columns = df.columns
# print(f"Columns: {columns}, {len(columns)}")

# QA_Pairs = []

# for row in df.iterrows():
#     # print(row[columns[0]])
#     # print(row[0], row[1][columns[0]])
    
#     for i in range(len(columns)-1):
#         # print(row[1][columns[i]])
#         question = row[1][columns[i]]
#         temp = {
#             "questions": question,
#             "answers": row[1][columns[len(columns)-1]]
#         }
#         QA_Pairs.append(temp)
        
#         # print(QA_Pairs)
    
#     faq_df = pd.DataFrame(
#         columns=["questions", "answers"],
#         data=QA_Pairs
#     )
    
#     folder_path = "Content_Sheets/Unified_Sheets"
#     faq_df.to_csv(f"{folder_path}/{data_path}", index=False)
    
#     print(f"{row[0]}---------------------------------------------------")
    
    

"""
    Powershell Command: - python Script_Files/fallback_content_merge.py
"""

import os

def create_unified_sheet(
        dir_name: str,
        file_name: str
):
    """
        params:
            dir_name: Directory containing csv files.
            file_name: To be exported csv file name.
    """
    os.chdir(dir_name)
    files = os.listdir()
    print(f"All the files: {files}")

    unified_df = pd.concat([pd.read_csv(file) for file in files], ignore_index=True)
    print(f"Unified Dataframe shape: {unified_df.shape}")

    unified_df.to_csv(f"{file_name}.csv", index=False)
    print("Exported to CSV file.....!!!")


create_unified_sheet(
    dir_name="Content_Sheets/Unified_Sheets/",
    file_name="ZIES_Fallback_FAQs"
)





