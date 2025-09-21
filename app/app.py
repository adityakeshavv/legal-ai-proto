# app/app.py
import streamlit as st
from extract import extract_text
from summarize import summarize_text
from explain import explain_clause
from qa import ask_question

st.title("Legal Document Simplifier")

uploaded_file = st.file_uploader("Upload a PDF or DOCX", type=["pdf", "docx"])

if uploaded_file:
    doc_text = extract_text(uploaded_file)
    st.text_area("Document Text", doc_text, height=300)

    if st.button("Summarize Document"):
        summary = summarize_text(doc_text)
        st.subheader("Summary")
        st.write(summary)

    st.subheader("Explain Clause")
    clause_input = st.text_area("Paste clause to explain")
    if st.button("Explain Clause"):
        explanation = explain_clause(clause_input)
        st.write(explanation)

    st.subheader("Ask a Question")
    user_question = st.text_input("Your Question")
    if st.button("Get Answer"):
        answer = ask_question(doc_text, user_question)
        st.write(answer)
