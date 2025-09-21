# app/app.py
import streamlit as st
from extract import extract_text
from summarize import summarize_text
from explain import explain_clause
from qa import ask_question

# Page configuration
st.set_page_config(
    page_title="Legal AI Simplifier",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for sunset-orange theme
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

    /* App-wide styles */
    .stApp {
        background: linear-gradient(135deg, #ff7e5f, #feb47b);  /* Sunset orange gradient */
        font-family: 'Inter', sans-serif;
        color: #1f1f1f;
    }

    /* Title styling */
    h1, .css-1d391kg {
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        font-size: 48px !important;
        color: #fff;  /* white for contrast */
        margin-bottom: 20px;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.4);
    }

    /* Subheaders */
    h2 {
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        font-size: 24px !important;
        color: #fff8f0;  /* light cream for contrast */
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }

    /* Text areas styling */
    textarea {
        border: 2px solid #fff;
        border-radius: 16px;
        padding: 12px;
        font-size: 16px;
        color: #1f1f1f;
        background-color: #fffbea;
    }

    /* Buttons styling */
    div.stButton > button {
        background: linear-gradient(90deg, #ff6a00, #ff9966);
        color: white;
        font-weight: 600;
        border-radius: 16px;
        height: 50px;
        width: 220px;
        font-size: 16px;
        transition: all 0.3s ease;
    }

    /* Hover effect for buttons */
    div.stButton > button:hover {
        background: linear-gradient(90deg, #ff9966, #ff6a00);
        color: white;
    }

    /* Output cards */
    .output-card {
        background: #fff3e0;
        border-radius: 16px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.15);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# App title
st.title("⚖️ Legal Document Simplifier")

# Upload section
st.markdown("### 📄 Upload Your Legal Document")
uploaded_file = st.file_uploader("Choose a PDF or DOCX", type=["pdf", "docx"])

if uploaded_file:
    doc_text = extract_text(uploaded_file)
    st.text_area("Document Text", doc_text, height=300, key="doc_text_area")

    st.markdown("---")  # separator

    # Columns for buttons
    col1, col2 = st.columns(2)

    with col1:
        if st.button("📝 Summarize Document"):
            summary = summarize_text(doc_text)
            st.markdown(f"<div class='output-card'><h2>Summary ✨</h2>{summary}</div>", unsafe_allow_html=True)

    with col2:
        st.subheader("🔍 Explain Clause")
        clause_input = st.text_area("Paste clause to explain", key="clause_text")
        if st.button("💡 Explain Clause"):
            explanation = explain_clause(clause_input)
            st.markdown(f"<div class='output-card'><h2>Explanation 💡</h2>{explanation}</div>", unsafe_allow_html=True)

    st.markdown("---")  # separator

    st.subheader("❓ Ask a Question")
    user_question = st.text_input("Your Question", key="user_question")
    if st.button("🧠 Get Answer"):
        answer = ask_question(doc_text, user_question)
        st.markdown(f"<div class='output-card'><h2>Answer 🧠</h2>{answer}</div>", unsafe_allow_html=True)
