# user question 
# Read the coloumns names from the Table
# Read 5 sample rows from the Table
# pass column name  + sample rows LLM to generate schema
# pass user questions + context to LLM to generate sql
# Excute Sql


import sqlite3
import pandas as pd
import json 
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv
import ingestion

load_dotenv()

#user question

question = "Get me the number of users in Charlotte"
db_path = "csvchatbot.db"
 

 #Establish connection 

conn = sqlite3.connect(db_path)

#Read all the tables

tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';",conn)


#-- from here i need to do  -- 





# Read  5 sample from the database

conn = sqlite3.connect(db_path)

sample_data = pd.read_sql(f"select * from {Table_name} limit 5",conn)

print(sample_data.head())

# Read Column names

table_columns = sample_data.columns.to_list()
print(table_columns)


# Connecting to LLM
#openai_api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(temperature=0,model="gpt-4")


prompt_schema = PromptTemplate(
    input_variables=["columns","sample_row"],
    template=(
        """ You are a skilled  data analyst whos is expert in documenting database information
        belwo are the columns and some sample data row from my sqlite table
         
         columns: {columns}
         sample data :{sample_row}
        
        please create output with 
        give me list of
        Column name : column  dataype ,manatory or not,column description 

        donot give me any additional information or white spaces 
             """

    )
    
)

# Invoke the prompt

chain = prompt_schema|llm

response = chain.invoke(
    {
    "columns" : table_columns,
    "sample_row" : sample_data
    }
)

print(response.content)

first_response = response.content


prompt_query = PromptTemplate(
    input_variables=["first_response","question","table"],
    template=(
        """You are an expert in SQL and database management. Here are the descriptions for each column and their names. {first_response} and here is the table name {table}
        
        Generate a SQL query based on user question {question}
        give me only a sqlite syntax/query with no additional information
        """
    )
)
chain_2 = prompt_query|llm
response_2 = chain_2.invoke(
    {
        "first_response": first_response,
        "question": question,
        "table": Table_name
    }
)
print(response_2.content)