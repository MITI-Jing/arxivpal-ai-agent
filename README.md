✅ Project Goal
Build an AI Agent that:

Loads full-text scientific papers from the ccdv/arxiv-summarization dataset

Summarizes them using an LLM

Answers user questions about the paper


# 🧠 ArxivPal – AI Research Assistant

**ArxivPal** is an AI-powered agent that helps you understand academic papers. Ask natural language questions and get insightful, LLM-generated answers, with traceable context from the source paper.

---

## 🚀 Features

- 🔍 Summarizes and answers questions from research papers
- 🧠 Retrieval-Augmented Generation (RAG) with GPT
- 📚 Local vector store for document chunking and semantic search
- 📦 FastAPI backend with Streamlit frontend
- ✅ Clean architecture for easy extension

---

## 📁 Project Structure
arxivpal-ai-agent/
├── backend/
│ ├── app.py # FastAPI app
│ ├── data_loader.py # Load sample or uploaded papers
│ ├── rag_pipeline.py # Chunking and vector store
│ ├── qa_agent.py # LLM + Retrieval QA logic
│ ├── test_rag_qa.py # CLI test script
├── frontend/
│ └── streamlit_app.py # Streamlit UI
├── .env # Environment variables (not committed)
├── .gitignore
├── requirements.txt
└── README.md

