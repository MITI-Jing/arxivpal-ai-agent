from fastapi import FastAPI, Request
from pydantic import BaseModel
from data_loader import get_sample_paper
from rag_pipeline import chunk_article, create_vectorstore
from qa_agent import build_qa_chain
from dotenv import load_dotenv
import uvicorn

load_dotenv()

app = FastAPI()

# Global QA chain
qa_chain = None

class QuestionRequest(BaseModel):
    question: str

@app.on_event("startup")
def startup_event():
    global qa_chain
    article, _ = get_sample_paper()
    chunks = chunk_article(article)
    vectorstore = create_vectorstore(chunks)
    qa_chain = build_qa_chain(vectorstore)

@app.get("/")
def read_root():
    return {"message": "Welcome to ArxivPal API"}

@app.post("/ask")
def ask_question(req: QuestionRequest):
    global qa_chain
    response = qa_chain.invoke({"query": req.question})
    return {"question": req.question, "answer": response["result"]}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
