News Summarizer & Q&A Agent
🔹 What it does

User enters a news URL.

The agent scrapes the article text.

Summarizes the article in simple points.

User can ask questions about the article (e.g., "Who is mentioned?" / "What is the main issue?").

Runs fully with Python + Streamlit, easy to test in VS Code.

🔹 Why this project?

Practical for students, researchers, journalists.

End-to-end flow: input → process → summarize → interact.

Uses an agent structure (tool for web scraping + tool for summarization + Q&A).

Can be extended with multiple articles, topic clustering, or daily digest.

📰 News Summarizer & Q&A Agent
1. 📦 Install Requirements

Run in terminal (VS Code):

pip install streamlit newspaper3k langchain ollama


(If you don’t want Ollama, we can swap in HuggingFace’s transformers.) 
5. ▶️ Run the App

In VS Code terminal:

streamlit run app.py

🔎 Explanation of Flow

Input: User enters a news URL.

Scraping Tool: newspaper3k downloads and extracts text.

Agent Logic:

summarize() → Calls LLM with summary prompt.

ask_question() → Calls LLM with article + user question.

UI: Streamlit displays article snippet, summary, and answers.
