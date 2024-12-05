import os, os.path
import shutil
import pathlib
import csv
import streamlit as st
#importing the RAG programs
#import get_embeddings #This will get the documents 
#import create_prompt # this program will create the question to go intp query_for_results
#import query_for_results # This program will create the final output
import RETIPS

st.title("Hospital Reports Analysis RAG Framework UI")

file = open('feedback.xlsx', 'w') #opening a file to save user feedback in
file =  csv.writer(file) #able to write to the file
file.writerow(['Satisfied Rating', 'Comments'])

if 'selection' not in st.session_state:
    st.session_state.selection = ""
# activating selection box for user choice
options = False
emp = st.empty()
typeQuery = emp.selectbox(
    key = "Options",
    label = "Please select the reference data for query running:",
    options = ("Retips","Incident Report","Patient Feedback")
)

if typeQuery =="Incident Report":
    #need to import data_set
    dataSet = st.text_input(
        label="Please input data path",
        max_chars=256
    )

    columnVal = st.text_input(
        label="What column number is data in?",
    )

    query = st.text_input(
        label="Please input your question",
        max_chars=256
    )

    #get_embeddings(dataSet, column Value)  #Fix the dataset path

    exampleNum = st.text_input(
        label="Please input how many examples you would like in output",
    )
    #create_prompt(exampleNum, query, columnVal ) #create_prompt doesn't intake any values, so maybe the previous question is unnecesary

    #rag_output = query_for_results() #the output from query_for_results should be the output
    #st.text(rag_output)


if typeQuery =="Patient Feedback":
    #need to import data_set
    dataSet = st.text_input(
        label="Please input data path",
        max_chars=256
    )

    columnVal = st.text_input(
        label="What column number is data in?",
    )

    query = st.text_input(
        label="Please input your question",
        max_chars=256
    )

    #get_embeddings(dataSet, column Value)  #Fix the dataset path

    exampleNum = st.text_input(
        label="Please input how many examples you would like in output",
    )
    #create_prompt(exampleNum, query, columnVal ) #create_prompt doesn't intake any values, so maybe the previous question is unnecesary

    #rag_output = query_for_results() #the output from query_for_results should be the output
    #st.text(rag_output)

if typeQuery =="Retips":
    #need to import data_set
    dataSet = RETIPS.xlsx

    columnVal = st.text_input(
        label="What column number is data in?",
    )

    query = st.text_input(
        label="Please input your question",
        max_chars=256
    )

    #get_embeddings(dataSet, column Value)  #Fix the dataset path

    exampleNum = st.text_input(
        label="Please input how many examples you would like in output",
    )
    #create_prompt(exampleNum, query, columnVal ) #create_prompt doesn't intake any values, so maybe the previous question is unnecesary

    #rag_output = query_for_results() #the output from query_for_results should be the output
    #st.text(rag_output)

