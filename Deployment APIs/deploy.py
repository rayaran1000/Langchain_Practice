from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes # For adding all the routes via different LLMs
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# Defining the application
app = FastAPI(
    title="LangChain API with Ollama",
    description="A REST API for interacting with LangChain",
    version="1.0.0"
)

# Models for which routes need to be created
llama2_model = Ollama(model="llama2")
qwen2_model = Ollama(model="qwen2:1.5b")

#Prompts for the 2 models
prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words.")
prompt2 = ChatPromptTemplate.from_template("Write me a poem in Hindi about {topic} with 100 words.")

# Adding a route
add_routes(
    app,
    prompt1|llama2_model,
    path="/llama2"
)


add_routes(
    app,
    prompt2|qwen2_model,
    path="/qwen2"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
