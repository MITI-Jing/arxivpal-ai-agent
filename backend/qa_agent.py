from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI  # for OpenAI
# from langchain.llms import HuggingFaceHub  # or your own model
from dotenv import load_dotenv
import os

load_dotenv()

def build_qa_chain(vectorstore):
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",  # or "gpt-4" if you have access
        temperature=0,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_type="similarity", k=4),
        return_source_documents=True
    )
    return qa_chain
