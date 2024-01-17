import os

from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langserve import add_routes
from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)

add_routes(
    app,
    ChatOpenAI(openai_api_key=os.environ.get("OPENAI_API_KEY")),
    path="/openai",
)

model = ChatOpenAI(openai_api_key=os.environ.get("OPENAI_API_KEY"))
prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
add_routes(
    app,
    prompt | model,
    path="/joke",
)

llm = ChatOpenAI(openai_api_key=os.environ.get("OPENAI_API_KEY"))

loader = WebBaseLoader("https://www.billtrust.com/about")
docs = loader.load()

embeddings = OpenAIEmbeddings()
text_splitter = RecursiveCharacterTextSplitter()
documents = [doc.page_content for doc in docs]


prompt_chain = ChatPromptTemplate.from_template("""Question: {input}

Answer the following question based only on the provided context:

""" + " ".join(documents))


add_routes(
    app,
    prompt_chain | llm,
   path="/billtrust",
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)