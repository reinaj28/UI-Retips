import os, os.path
import shutil
import pathlib
import csv
import streamlit as st
#importing the RAG programs
import get_embeddings #This will get the documents 
import create_prompt # this program will create the question to go intp query_for_results
import query_for_results # This program will create the final output

st.title("Hospital Reports Analysis RAG Framework UI")

file = open('feedback.xlsx', 'w') #opening a file to save user feedback in
file =  csv.writer(file) #able to write to the file
file.writerow(['Satisfied', 'Comments'])

if 'selection' not in st.session_state:
    st.session_state.selection = ""
# activating selection box for user choice
options = False
emp = st.empty()
vari = emp.selectbox(
    key = "Options",
    label = "Please select the reference data for query running:",
    options = ("RETIPS", "Incident Report","Patient Feedabck")
)
#need to import data_set
get_embeddings(data_fixed.JSON) #Fix the dataset path

research_query = st.text_input(
    label="Please input what you want to search",
    max_chars=256
)
create_prompt(research_query) #create_prompt doesn't intake any values, so maybe the previous question is unnecesary

rag_output = query_for_results() #the output from query_for_results should be the output

#where is the data written in the output, then search for the index 
data_index = st.text_input(
    label="The data index that mentioned in the output",
    #max_chars=256
)

#We need to save the data somewhere
feed = st.empty()
vari = feed.selectbox(
    key = "Feedback",
    label = "Are you satisfied with the RAG output?",
    options = ("Yes", "No")
)

feedback = st.text_input(
    label="Please leave any comments about the RAG output",
    max_chars=256
)
file.writerow([vari, feedback])
