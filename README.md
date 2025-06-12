
# ArxivPal AI Agent

**ArxivPal** is an AI-powered assistant designed to summarize and answer questions on academic papers from the [arXiv](https://arxiv.org/) repository using state-of-the-art natural language processing techniques.

---

## Features

- Summarizes academic papers automatically
- Supports natural language queries about paper content
- Retrieval-Augmented Generation (RAG) for contextual answers
- Modular FastAPI backend with Streamlit frontend


## Getting Started

### Prerequisites

- Python 3.8+
- Git


### Installation

1. Clone the repository:

   git clone https://github.com/MITI-Jing/arxivpal-ai-agent.git
   cd arxivpal-ai-agent
(Optional) Create and activate a Python virtual environment:

python -m venv venv
source venv/bin/activate   # Linux/macOS
.\venv\Scripts\activate    # Windows PowerShell

2. Install dependencies:

pip install -r requirements.txt

3. Running locally
Start the FastAPI backend:

uvicorn backend.app:app --reload

4. Start the Streamlit frontend:

streamlit run app.py

Project Structure

arxivpal-ai-agent/
├── backend/                  # FastAPI backend and core logic
│   ├── __init__.py           # Package initialization
│   ├── app.py                # FastAPI application entry point
│   ├── data_loader.py        # Data loading utilities
│   ├── qa_agent.py           # Question-answering agent logic
│   ├── rag_pipeline.py       # Retrieval-Augmented Generation pipeline
│   └── test_rag_qa.py        # Unit tests for RAG QA pipeline
├── frontend/                 # Streamlit frontend app
│   └── streamlit_app.py      # Streamlit UI and user interaction
├── data/                     # Dataset and resource files
├── Dockerfile                # Docker container setup
├── README.md                 # Project documentation
└── requirements.txt          # Python dependencies


License
This project is licensed under the MIT License.

Contact
Created by Jing MITI.
GitHub: MITI-Jing
Linkedin: https://www.linkedin.com/in/jingliaideveloper/