import requests
import streamlit as st

def get_llama2_response(input_text):
    response = requests.post("http://localhost:8000/llama2/invoke",
    json = {'input':{'topic':input_text}})# 'topic' written because we were using this 'topic' name while mentioning the prompts

    return response.json()['output']

def get_qwen2_response(input_text):
    response = requests.post("http://localhost:8000/qwen2/invoke",
    json = {'input':{'topic':input_text}})# 'topic' written because we were using this 'topic' name while mentioning the prompts

    return response.json()['output']

st.title("Langchain API with LLAMA2 and QWEN2 Models from Ollama")
input_text1 = st.text_input("Write an essay on") # Input text for llama2
input_text2 = st.text_input("Write a poem in Hindi on") # Input text for qwen2

# Returning the output from the models if input was given to the models
if input_text1:
    st.write(get_llama2_response(input_text1))

if input_text2:
    st.write(get_qwen2_response(input_text2))
