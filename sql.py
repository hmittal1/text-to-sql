from dotenv import load_dotenv

# load environment variables
load_dotenv() 

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

#configure genAi key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# func to load gen ai model
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

#func to retrieve query from the db
def read_sql_query(sql, db):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    connection.commit()
    connection.close()
    for row in rows:
        print(row)
    return rows

#define prompt
prompt = [
  """
 You are an expert in converting English questions to SQL query!
 The SQL database has the name STUDENT and has following columns - NAME,
 CLASS, SECTION \n\n For example 1 - how many entries of records are present ?,
 the sql command will be something like this SELECT * FROM STUDENT;
 \nExample 2 - Tell me all the students studying in data science class ?,
 the sql command will be something like this SEELCT * FROM STUDENT where CLASS ='Data science';
 also the sql code should not have ``` in begining or end and sql word in output
"""
]


#streamlit app
st.set_page_config(page_title="I can retreieve any Sql query")
st.header("Gemini app to retrieve Sql data")

question = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# if submit is clicked
if submit:
    ai_response = get_gemini_response(question, prompt)
    response = read_sql_query(ai_response, "student.db")
    st.subheader("The response is")
    for row in response:
        print(row)
        st.header(row)