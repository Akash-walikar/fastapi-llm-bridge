from fastapi import FastApi
from langcahin.chat_models import ChatOpenAI
from langchain.prompt import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"]=OS.getenv("OPENAI_API_KEY")

app=FastApi(
    Title="Langchain with Ollama API",
    version="0.1",
    description="This is a simple API using Langchain with Ollama LLM"
)

add_routes(
    app,
    ChatOpenAI(),
    Path="/OpenAI"
    )

model=ChatOpenAI()
ollama=Ollama(model="llama2")

prompt1=ChartPromptTemplate.from_messages("write me an essay {topic} with 100 words")
prompt2=ChartPrompttemplate.from_messages("write me an essay {topic} wit 100 words")
add_routes(
    app,
    prompt1|model,
    Path="/essay"
    
)

add_routes(
    app,
    prompt2|ollama,
    Path="/poem"
)
if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8000)


    #to run just use python app.py