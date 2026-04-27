import streamlit as st
import openai
from tools import search_tool

openai.api_key = "YOUR_API_KEY"

st.title("🔍 Agentic Research Assistant")

query = st.text_input("Enter research topic:")

if query:
    
    # Step 1: Agent decides to search
    search_result = search_tool(query)

    # Step 2: LLM processes info
    prompt = f"""
    You are an AI research assistant.

    Topic: {query}

    Use this information:
    {search_result}

    Generate:
    - Summary
    - Key insights
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    result = response["choices"][0]["message"]["content"]

    st.write(result)