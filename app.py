import os
import streamlit as st

from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

st.set_page_config(
    page_title="Zyro Dynamics HR Help Desk",
    page_icon="💼",
    layout="centered"
)

GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model="llama-3.3-70b-versatile",
    temperature=0
)

@st.cache_resource
def build_rag():

    loader = PyPDFDirectoryLoader("data")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2"
    )

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 6}
    )

    return retriever

retriever = build_rag()

RAG_PROMPT = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an HR assistant for Zyro Dynamics.

Answer ONLY from the provided context.

If information is unavailable respond exactly:

I cannot answer this based on the available HR policy documents.
"""
    ),
    (
        "human",
        "Context:\n{context}\n\nQuestion:\n{question}"
    )
])

st.title("💼 Zyro Dynamics HR Help Desk")

question = st.text_input(
    "Ask an HR Question"
)

if question:

    docs = retriever.invoke(question)

    context = "\n\n".join(
        d.page_content for d in docs
    )

    chain = (
        RAG_PROMPT
        | llm
        | StrOutputParser()
    )

    answer = chain.invoke({
        "context": context,
        "question": question
    })

    st.success(answer)

    with st.expander("Sources"):
        for d in docs:
            st.write(
                d.metadata.get("source", "")
            )
