import os, os.path
import shutil
import pathlib
import streamlit as st
import get_embeddings 
import create_prompt
import query_for_results 


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
vari = emp.selectbox(
    key = "Options",
    label = "Please select the file type:",
    options = ("CVS", "JSON")
)

if st.button("Select"):
    choice = vari
    options = True

#CVS File type choice
def csv_choice() -> str:
    with st.form(key="doc_upload", clear_on_submit=False):

        uploaded_doc = st.file_uploader(
            label="Please upload your document",
            accept_multiple_files = False,
            type=['csv']
        )
        get_embeddings.load_data_to_dataframe(uploaded_doc)

        create_prompt.main(uploaded_doc)

        submit_button1 = st.form_submit_button("Load Document")

    if submit_button1:
        with open(os.path.join(target_folder, uploaded_doc.name), 'wb') as f:
            f.write(uploaded_doc.getbuffer())
        return

#JSON File type choice
def json_choice() -> str:
    
    with st.form(key="doc_upload", clear_on_submit=False):

        uploaded_doc = st.file_uploader(
            label="Please upload your document",
            accept_multiple_files = False,
            type=['JSON']
        ) 
        get_embeddings.load_data_to_dataframe(uploaded_doc)

        create_prompt.main(uploaded_doc)

        submit_button1 = st.form_submit_button("Load Document")

    if submit_button1:
        with open(os.path.join(target_folder, uploaded_doc.name), 'wb') as f:
            f.write(uploaded_doc.getbuffer())
        return 

def main(selection):
    if selection == "CSV":
        csv_query = csv_choice()

        if csv_query is not None:
            with st.spinner("Processing your request..."):
                answer = query_for_results.main() 

                st.success("Data processing complete!")
                st.markdown(f"###### {answer['result']}")

    elif selection == "JSON":
        json_query = json_choice()

        if json_query is not None:
            with st.spinner("Processing your request..."):
                answer = query_for_results.main()

                st.success("Data processing complete!")
                st.write(answer['result'])

if __name__ == "__main__":
    if options:
        st.session_state.selection = choice

    main(st.session_state.selection)