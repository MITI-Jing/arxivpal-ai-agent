from data_loader import get_sample_paper
from rag_pipeline import chunk_article, create_vectorstore
from qa_agent import build_qa_chain

article, _ = get_sample_paper()
chunks = chunk_article(article)
vectorstore = create_vectorstore(chunks)
qa = build_qa_chain(vectorstore)

question = "What is the novelty of this paper?"
response = qa.invoke({"query": question})

print("\n🤖 AI Agent's Answer:\n", response["result"])
