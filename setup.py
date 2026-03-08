from setuptools import setup, find_packages

setup(
    name="cyberinstructor",        # package name
    version="0.1",                  # initial version
    packages=find_packages(),       # automatically include all Python packages
    install_requires=[
        "streamlit",
        "langchain",
        "langchain-core",
        "langchain-groq",
        "python-dotenv"
    ],
    description="LLM-powered Cybersecurity Chatbot",
    author="Muhammad Mudassir",
)