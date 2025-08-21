# app.py
import streamlit as st
from agent import NewsAgent

st.set_page_config(page_title="News Summarizer & Q&A Agent", layout="centered")

st.title("📰 News Summarizer & Q&A Agent")

url = st.text_input("Enter a news article URL:")

if url:
    agent = NewsAgent(model_name="llama2")
    with st.spinner("Fetching and analyzing article..."):
        try:
            article_text = agent.scrape_article(url)
            st.subheader("📄 Original Article (first 500 chars)")
            st.write(article_text[:500] + "...")

            summary = agent.summarize(article_text)
            st.subheader("📝 Summary")
            st.write(summary)

            st.subheader("❓ Ask Questions about the Article")
            question = st.text_input("Enter your question:")
            if question:
                answer = agent.ask_question(article_text, question)
                st.write("**Answer:**", answer)

        except Exception as e:
            st.error(f"Error: {e}")
