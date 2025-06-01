# 1. Read all the csv files 
#  2. Insert into  to a database


import pandas as pd
import sqlite3
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()


# Read Base Path

BASE_DIR = Path(__file__).resolve().parent       # Portable base
DATA_DIR = BASE_DIR / "Data"                     # Path to /Data folder

# This works across Windows, Linux, Mac
csv_files_path = list(DATA_DIR.rglob("*.csv"))
 

#  #Now read each csv name and data frame and store it in dictiory
# csv_dict ={}
# for path in csv_files_path:
#      name = path.stem  # filename without extension
#      csv_dict[name]= path
     

# # convert CSV list to dataframe
# df = pd.DataFrame()
# for doc,path in csv_dict.items():
#      df[doc]= pd.read_csv(path)

#  #Now read each csv name and data frame and store it in dictiory
dict_name_df = {}
df = pd.DataFrame()
for path in csv_files_path:
    file_name = path.stem
    dict_name_df[file_name]=  pd.read_csv(path)

print(f" Total CSV files loaded: {len(dict_name_df)}")

print(dict_name_df['food_delivery_users'].head())

#Establish sqllite connection

conn = sqlite3.Connection("csvchatbot.db")
print(conn)

#use the connection and loop to insert to table if not exit 

for table_name , df in dict_name_df.items():
    try:
        df.to_sql(name=table_name, con=conn, if_exists='replace', index=False)
        print(f"Inserted {table_name} → {df.shape}")
    except Exception as e:
        print(f" Failed to insert {table_name}: {e}")
    
