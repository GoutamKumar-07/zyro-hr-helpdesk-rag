import streamlit as st

st.set_page_config(
    page_title="Zyro Dynamics HR Help Desk",
    page_icon="💼",
    layout="wide"
)

st.title("💼 Zyro Dynamics HR Help Desk")

st.markdown("""
Welcome to the HR Help Desk chatbot.

You can ask questions about:

- Leave Policy
- Work From Home Policy
- Compensation & Benefits
- Employee Handbook
- Performance Reviews
- Travel & Expense Policy
- IT & Data Security Policy
""")

question = st.text_input("Ask your HR question")

if question:
    st.success("This Streamlit app was deployed for the Zyro Dynamics RAG Challenge.")
    st.info(
        "The complete Retrieval-Augmented Generation (RAG) pipeline is implemented in the Kaggle notebook submission."
    )
