import os
from pydoc import doc, text
from urllib import response

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from groq import Groq


class RAGPipeline:

    def __init__(self, api_key):

        self.client = Groq(api_key=api_key)

        self.embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        self.vector_store = None

    def process_pdf(self, pdf_path):

        loader = PyPDFLoader(pdf_path)

        documents = loader.load()
        
        for doc in documents:
            text = doc.page_content

            text = text.replace("�", "")
            text = text.replace("\n", " ")
            text = " ".join(text.split())

            doc.page_content = text

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        chunks = splitter.split_documents(documents)

        self.vector_store = FAISS.from_documents(
            chunks,
            self.embedding_model
        )

        return len(chunks)

    def ask(self, question):

      docs = self.vector_store.similarity_search(
         question,
          k=5
      )

      context = "\n\n".join([doc.page_content for doc in docs])

      prompt = f"""
You are an intelligent Document Question Answering assistant.

Rules:
1. Answer ONLY using the provided context.
2. Do NOT use outside knowledge.
3. If the answer is not present in the context, reply:
   "I couldn't find that information in the document."
4. Give a clean, well-formatted answer.
5. Do NOT repeat the context.

---------------------
Context:
{context}
---------------------

Question:
{question}

Answer:
"""

      response = self.client.chat.completions.create(
          model="llama-3.3-70b-versatile",
          temperature=0,
          max_tokens=512,
          messages=[
            {
                "role": "system",
                "content": "You answer questions strictly from the provided document context."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
      )

      answer = response.choices[0].message.content.strip()

      return answer, docs
    