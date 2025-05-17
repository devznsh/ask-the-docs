import streamlit as st
from rag_pipeline import answer_question_from_file

st.set_page_config(page_title="Ask the Docs")
st.title("📄 Ask the Docs - RAG App (Hugging Face)")

uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])
question = st.text_input("Ask a question based on the document:")

if uploaded_file and question:
    with st.spinner("Processing..."):
        try:
            answer = answer_question_from_file(uploaded_file, question)
            st.success("Answer:")
            st.write(answer)
        except Exception as e:
            st.error(f"Error: {str(e)}")
