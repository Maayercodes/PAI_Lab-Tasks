import streamlit as st
from utils.pdf_parser import extract_text_from_pdf
from utils.chunker import chunk_text
from utils.embedder import get_embeddings
from utils.faiss_index import build_faiss_index, search_faiss_index
from utils.rag_pipeline import generate_answer
import tempfile

st.set_page_config(page_title="Smart Syllabus Assistant", layout="centered")
st.title("📘 Smart Syllabus Assistant")

uploaded_file = st.file_uploader("Upload your syllabus PDF", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    text = extract_text_from_pdf(tmp_path)
    st.info("PDF content extracted. Chunking and embedding...")

    chunks = chunk_text(text)
    embeddings = get_embeddings(chunks)
    index = build_faiss_index(embeddings)

    st.success("PDF parsed and indexed! Now you can ask your question.")

    user_question = st.text_input("Ask a question about your syllabus:")

    if user_question:
        matched_chunks = search_faiss_index(user_question, chunks, embeddings, index)
        answer = generate_answer(user_question, matched_chunks)

        st.markdown("### 📌 Answer")
        st.write(answer)

        st.markdown("---")
        st.markdown("### 🧩 Retrieved Context")
        for chunk in matched_chunks:
            st.markdown(f"- {chunk}")
