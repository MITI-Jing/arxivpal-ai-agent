import streamlit as st
import requests

st.set_page_config(page_title="🧠 ArxivPal AI Agent", layout="centered")

st.title("🧠 ArxivPal")
st.write("Ask me anything about an academic paper!")

# User input
question = st.text_input("Enter your question")

if st.button("Ask"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            response = requests.post("http://localhost:8000/ask", json={"question": question})
            if response.status_code == 200:
                answer = response.json().get("answer", "")
                st.success("Answer:")
                st.write(answer)
            else:
                st.error("❌ Something went wrong. Try again.")
