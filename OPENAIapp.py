from langchain_openai import ChatOpenAI # OpenAI LLM (different for open source models)
from langchain_core.prompts import ChatPromptTemplate # Used for giving intitial chat template
from langchain_core.output_parsers import StrOutputParser # Default output parser for getting response from LLM(custom parser also possible - discussed later)

import streamlit as st
import os
from dotenv import load_dotenv


os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY") # Get the LLM key from the environment
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


# Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

# Streamlit framework

st.title("LangChain Chatbot using OPENAI LLM")

user_input=st.text_input("Enter your question") # Taking the input from user

# Calling the OPENAI LLM
llm = ChatOpenAI(model="gpt-3.5-turbo") # Model Name
output_parser = StrOutputParser # Output response from LLM
chain = prompt|llm|output_parser # Combining the different components of the cycle together

if user_input: # User has given input
    st.write(chain.invoke({'question':input_text}))