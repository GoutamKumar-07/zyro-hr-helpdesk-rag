import streamlit as st
import streamlit as st

st.write("Secret exists:", "GROQ_API_KEY" in st.secrets)

st.set_page_config(
    page_title="Zyro Dynamics HR Help Desk",
    page_icon="💼",
    layout="centered"
)

st.markdown("""
<style>
.main {
    padding-top: 2rem;
}

.hero {
    background: linear-gradient(135deg, #1f2937, #111827);
    padding: 2rem;
    border-radius: 15px;
    color: white;
    text-align: center;
    margin-bottom: 2rem;
}

.feature-box {
    background-color: #262730;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>💼 Zyro Dynamics HR Help Desk</h1>
    <p>Instant answers from company HR policies</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-box">
    📄 Leave Policy
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-box">
    🏠 Work From Home
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-box">
    💰 Compensation & Benefits
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-box">
    📘 Employee Handbook
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-box">
    ⭐ Performance Reviews
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-box">
    🔒 IT & Data Security
    </div>
    """, unsafe_allow_html=True)

st.divider()

question = st.text_input(
    "Ask an HR Question",
    placeholder="e.g. What is the notice period for L5 employees?"
)

if question:
    st.success("Demo deployment for Zyro Dynamics RAG Challenge")
    st.info(
        "The complete RAG pipeline and retrieval system are implemented in the Kaggle notebook submission."
    )

st.caption("Built using Streamlit • LangChain • FAISS • Groq")
