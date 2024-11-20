import os, os.path
import shutil
import pathlib
import streamlit as st
import get_embeddings.py
import create_prompt.py
import query_for_results.py


st.title("Hospital Incident Reports")
st.header("AI summarizer")

if 'selection' not in st.session_state:
    st.session_state.selection = ""

# clearing previously loaded pool of docs
target_folder = pathlib.Path().absolute()  / "docs/"

if target_folder.exists():
    shutil.rmtree(target_folder)
target_folder.mkdir(parents=True, exist_ok=True)

# activating selection box for user choice 
options = False
emp = st.empty()
vari = "Hospital Reports"
)

if st.button("Select"):
    choice = vari
    options = True

def research_choice() -> str:
    
    with st.form(key="doc_upload", clear_on_submit=False):

        doc_key = st.text_innput(
            label="Please detail specific columns or key to answer query",
            max_chars = 256
        )
        
        research_query = st.text_input(
            label = "Enter Question",
            max_chars = 256
        )
        submit_button1 = st.form_submit_button("Load Document")

    if submit_button1: #We dont have a file to upload just a key to look through every file
        with open(os.path.join(target_folder, uploaded_doc.name), 'wb') as f:
            f.write(uploaded_doc.getbuffer())
        return research_query


def main(selection):
        research_query = research_choice()

        if research_query is not None:
            with st.spinner("Processing your request..."):
                answer = generate_answer(selection, research_query)

                st.success("Data processing complete!")
                st.write(answer['result'])

if __name__ == "__main__":
    if options:
        st.session_state.selection = choice

    main(st.session_state.selection)
