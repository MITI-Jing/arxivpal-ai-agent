# 🤖 ArxivPal AI Research Agent

**ArxivPal** is an AI-powered agent prototype that extracting key insights and answers natural language questions using Retrieval-Augmented Generation (RAG) on academic papers from the [arXiv](https://arxiv.org/).Built with OpenAI, LangChain, FastAPI, and Streamlit.

---

## 🚀 Features

- 🧠 **LLM-Powered QA** – Ask questions about academic papers using OpenAI models.
- 🔍 **RAG Pipeline** – Retrieves relevant chunks and grounds answers in the source.
- 📚 **Built on Real Papers** – Uses the [`ccdv/arxiv-summarization`](https://huggingface.co/datasets/ccdv/arxiv-summarization) dataset.
- 📂 **(Coming Soon)**: Upload and analyze any research paper.
- 🪄 Expandable source context with every answer.
- 💬 Persistent chat history per paper.
- 🐳 Docker-ready for easy deployment.

---

## 🏗️ Tech Stack

| Layer         | Tools Used                                                                 |
|---------------|-----------------------------------------------------------------------------|
| LLM & Embedding | `OpenAI GPT-3.5/4`, `text-embedding-ada-002`                              |
| RAG & Vector DB | `LangChain`, `FAISS`, `ccdv/arxiv-summarization`                         |
| Backend       | `FastAPI`                                                                  |
| Frontend      | `Streamlit`                                                                |
| Secrets       | `.env` with `python-dotenv`                                                |
| Containerization | `Docker` (in progress)                                                  |

---

## 🔧 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/arxivpal-ai-agent.git
cd arxivpal-ai-agent

2. Create Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # or `.\venv\Scripts\activate` on Windows

3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt

4. Set Up .env File
Create a .env file in the root folder:

env
Copy
Edit
OPENAI_API_KEY=your_openai_key_here
🔐 Make sure .env is in your .gitignore!

5. Run the App
Start Backend (FastAPI)
bash
Copy
Edit
uvicorn backend.app:app --reload
Start Frontend (Streamlit)
bash
Copy
Edit
streamlit run streamlit_app.py

🐳 Docker (Coming Soon)

📂 File Structure
bash
Copy
Edit
arxivpal-ai-agent/
├── backend/
│   ├── _init_.py               # Package initialization
│   ├── app.py                  # FastAPI app
│   ├── data_loader.py          # Loads and chunks documents
│   ├── qa_agent.py             # Question-answering agent logic
│   ├── rag_pipeline.py         # RAG pipeline logic
│   ├── test_rag_qa.py          # Unit tests for RAG QA pipeline
├── frontend/
│   ├── streamlit_app.py        # Streamlit UI and user interaction
├── .env                        # OpenAI key (not committed)
├── requirements.txt
├── README.md
└── Dockerfile (coming)         # Docker container setup

🙋‍♀️ Author
Built by Jing Li – a career changer passionate about AI for real-world use cases.

📜 License
MIT License

⭐️ Support
Star the repo if you found it helpful! Reach out or raise an issue for feature requests or bugs.