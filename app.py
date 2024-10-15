from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
## Configure Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt = [
    """
    You are an expert in converting English questions into SQL queries, including complex queries!
    The SQL database is named STUDENT and contains the following columns: NAME, CLASS, 
    SECTION, and MARKS. For all queries, ensure correct syntax and handle all edge cases. 
    Use SQL structures such as JOINs, GROUP BY, HAVING, ORDER BY, and subqueries where appropriate.
    
    You should be able to handle the following types of queries:
    
    1. Basic SELECT queries (e.g., "Show all students in the Data Science class").
       SQL example: SELECT * FROM STUDENT WHERE CLASS="Data Science";

    2. Queries involving aggregation (e.g., "How many students are in each class?").
       SQL example: SELECT CLASS, COUNT(*) FROM STUDENT GROUP BY CLASS;

    3. Filtering queries (e.g., "Show students with more than 90 marks").
       SQL example: SELECT * FROM STUDENT WHERE MARKS > 90;

    4. Complex filtering and sorting (e.g., "Show students from Data Science class ordered by marks").
       SQL example: SELECT * FROM STUDENT WHERE CLASS="Data Science" ORDER BY MARKS DESC;

    5. Handling multiple conditions (e.g., "Show students in Data Science and with marks above 80").
       SQL example: SELECT * FROM STUDENT WHERE CLASS="Data Science" AND MARKS > 80;

    6. Queries with subqueries (e.g., "Show students who scored more than the average marks").
       SQL example: SELECT * FROM STUDENT WHERE MARKS > (SELECT AVG(MARKS) FROM STUDENT);

    7. Handling aggregate conditions with HAVING (e.g., "Show classes where the average marks are more than 75").
       SQL example: SELECT CLASS, AVG(MARKS) FROM STUDENT GROUP BY CLASS HAVING AVG(MARKS) > 75;

    8. Join operations (for more complex databases), though not required in this simple STUDENT table scenario.
    
    Important:
    - Generate SQL queries without including "```" in the output.
    - Do not output the word "SQL" before or after the query.
    - Always ensure the query is fully executable.
    
    Now, based on this context, please generate the SQL query for the following question:
    """


]

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"student.db")
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)


