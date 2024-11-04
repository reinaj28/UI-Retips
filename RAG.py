"This will hold a copy of the rag, although cannot run because so big"
"This is just to see how it connects to our app"
"This is a basic structure"

import os
import re
from langchain_community.llms import Ollama
from langchain_core.chat_history import BaseChatMessageHistory

def create_context_aware_chain(retriever, model_name):
    llm = Ollama(model=model_name, temperature=0.0)
    contextual_prompt = (
        "Given a chat history and user question, reformulate a standalone question "
        "without referencing chat history.")
    return retriever.with_contextual_prompt(llm, contextual_prompt)

def create_answering_chain(model_name, retriever):
    llm = Ollama(model=model_name, temperature=0.5)
    answering_prompt = (
        "Answer as a Star Wars expert based on provided Wikipedia info. "
        "If information is insufficient, respond: 'Not enough info to answer.'")
    return retriever.with_answering_prompt(llm, answering_prompt)

def chunk_docs(docs, chunk_size=800, chunk_overlap=100):
    # Split documents based on defined headers and content
    headers = [("h1", "Header 1"), ("h2", "Header 2"), ("h3", "Header 3")]
    params = {"chunk_size": chunk_size, "chunk_overlap": chunk_overlap, "headers": headers}
    return retriever.chunk_documents(docs, params)
