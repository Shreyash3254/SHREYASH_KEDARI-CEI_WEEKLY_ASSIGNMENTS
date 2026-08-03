import streamlit as st
import tempfile
import os

from config import GROQ_API_KEY
from rag_pipeline import RAGPipeline

st.set_page_config(
    page_title="Document Question Answering (RAG)",
    page_icon="📄",
    layout="wide"
)


st.title("📄 Document Question Answering System (RAG)")
st.markdown(
    """
Ask questions from any PDF using **Retrieval-Augmented Generation (RAG)** powered by **LangChain, FAISS, Sentence Transformers, and Groq Llama 3.3**.
"""
)

st.divider()

# Sidebar
st.sidebar.title("📂 Upload PDF")

uploaded_file = st.sidebar.file_uploader(
    "Choose a PDF",
    type="pdf"
)

st.sidebar.markdown("---")

st.sidebar.markdown("### ⚙ Tech Stack")

st.sidebar.success("✔ LangChain")
st.sidebar.success("✔ FAISS")
st.sidebar.success("✔ Sentence Transformers")
st.sidebar.success("✔ Groq Llama 3.3")
st.sidebar.success("✔ Streamlit")


if uploaded_file is not None:

    if st.sidebar.button("🚀 Process PDF"):

        with st.spinner("Processing document..."):

            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(uploaded_file.read())
                pdf_path = tmp.name

            pipeline = RAGPipeline(GROQ_API_KEY)

            total_chunks = pipeline.process_pdf(pdf_path)

            st.session_state.pipeline = pipeline

            os.remove(pdf_path)

        st.sidebar.success(f"✅ PDF processed successfully!")
        st.sidebar.info(f"Chunks Created: {total_chunks}")

# Ask Question
st.header("💬 Ask a Question")

question = st.text_input(
    "Enter your question"
)

if st.button("Ask"):

    if st.session_state.pipeline is None:
        st.warning("Please upload and process a PDF first.")

    else:

        with st.spinner("Generating answer..."):

            answer, docs = st.session_state.pipeline.ask(question)

        st.subheader("✅ Answer")

        st.success(answer)

        st.markdown("## 📚 Retrieved Context")

        for i, doc in enumerate(docs):

          with st.expander(f"📄 Source Chunk {i+1}"):

            st.write(doc.page_content)
st.divider()

st.caption(
    "Built using ❤️ Streamlit • LangChain • FAISS • Sentence Transformers • Groq"
)
