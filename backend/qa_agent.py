from langchain.chains import RetrievalQA
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def build_qa_chain(vectorstore):
    llm = ChatOpenAI(
        model_name="gpt-4.1",  # or "gpt-4" if you have access
        temperature=0,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_type="similarity", k=4),
        return_source_documents=True
    )
    return qa_chain
