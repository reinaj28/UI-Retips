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
dataSet = st.text_input(
    label="Please input data path",
    max_chars=256
)

get_embeddings() <dataSet> #Fix the dataset path

create_prompt() #create_prompt doesn't intake any values, so maybe the previous question is unnecesary

rag_output = query_for_results() #the output from query_for_results should be the output


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
