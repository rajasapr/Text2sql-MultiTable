# Text2sql-MultiTable
Natural language to SQL on multi-table databases using LLMs with schema + sample data awareness.


# 🧠 Text2SQL-MultiTable

**Text2SQL-MultiTable** is a lightweight framework for converting natural language questions into accurate SQL queries over **multi-table relational databases**. It leverages large language models (LLMs) like GPT-4 or LLaMA with structured prompts that include schema metadata and sample rows.

### 🚀 Features

- 🗃️ Supports multi-table SQLite databases
- 🔍 Extracts schema and sample rows automatically
- 🤖 Uses LLMs (e.g., OpenAI, Groq) for text-to-SQL conversion
- 🧱 LangChain integration for flexible prompting
- 📤 Easily pluggable with UI or chatbot frontends

### 📦 Example Workflow

1. Load your SQLite DB
2. Extract schema and rows for each table
3. Format prompt using LangChain `PromptTemplate`
4. Query LLM with your natural language question
5. Execute the generated SQL safely

### ✅ Example Prompt Structure

```text
You are an expert in SQL generation.
Schema:
Table: users
Columns: user_id, name, email, signup_date
Sample Rows: {'user_id': 1, 'name': 'Alice', ...}

Question:
Show all users who signed up after March 2024.
