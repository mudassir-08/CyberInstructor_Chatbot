import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Cyber Security Chatbot",
    page_icon="🛡️",
    layout="wide"
)

# ----------------------------
# Custom CSS Styling
# ----------------------------
st.markdown("""
<style>

.main {
    background-color: #0f172a;
}

.chat-user {
    background-color: #2563eb;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 10px;
    color: white;
}

.chat-bot {
    background-color: #1e293b;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 10px;
    color: #e2e8f0;
}

.title {
    text-align:center;
    font-size:40px;
    font-weight:bold;
    color:#38bdf8;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# Load API
# ----------------------------
load_dotenv()
api_key = os.getenv("groq_api_key")

# ----------------------------
# Model
# ----------------------------
model = ChatGroq(
    api_key=api_key,
    model="llama-3.1-8b-instant"
)

# ----------------------------
# Prompt
# ----------------------------
genral_prompt = """
Act as a cybersecurity instructor.
Answer the questions about attacks like SQL injection, XSS, brute force, and phishing conceptually.

Then provide defensive Python examples to detect, prevent, and log such attacks
in a controlled lab environment.

Do not generate exploit code.
Focus on mitigation and secure coding practices.
"""

prompt = ChatPromptTemplate.from_messages(
    [("system", genral_prompt), ("user", "{input}")]
)

parser = StrOutputParser()

chain = prompt | model | parser

# ----------------------------
# Sidebar
# ----------------------------
with st.sidebar:
    st.title("⚙️ Settings")
    st.markdown("### Model")
    st.write("Llama 3.1 8B Instant")

    st.markdown("---")
    st.markdown("### About")
    st.write(
        "This chatbot teaches **Cybersecurity concepts** "
        "and provides **defensive Python examples**."
    )

# ----------------------------
# Header
# ----------------------------
st.markdown('<p class="title">🛡️ Cybersecurity AI Instructor</p>', unsafe_allow_html=True)

# ----------------------------
# Chat History
# ----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="chat-user">👤 {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-bot">🤖 {msg["content"]}</div>', unsafe_allow_html=True)

# ----------------------------
# Input Box
# ----------------------------
user_input = st.chat_input("Ask about cybersecurity attacks...")

if user_input:

    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Analyzing security question..."):
        response = chain.invoke({"input": user_input})

    st.session_state.messages.append({"role": "assistant", "content": response})

    st.rerun()