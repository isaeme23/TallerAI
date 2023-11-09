from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
from langchain.tools import tool
from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.chains import RetrievalQA
import os
import pinecone

@tool("SayHello", return_direct=True)
def say_hello(name:str) -> str:
    """Answer when someone says hello"""
    return f"Hello {name}! My name is Sainapsis"


@tool("SayDogName", return_direct=True)
def say_dog_name(name:str) -> str:
    """Answer when someone mentions a dog"""
    return f"Hey! Your dog is called {name}"

@tool("collegeProgramsInfo", return_direct=True)
def college_programs_info(query:str) -> str:
    """Responder cuando se este buscando informacion relacionada a programas universitarios
    o relacionados a la Escuela Colombiana de Ingenieria"""
    pinecone.init(
        api_key=os.getenv("PINECONE_API_KEY"),  # find at app.pinecone.io
        environment=os.getenv("PINECONE_ENV"),  # next to api key in console
    )
    embeddings = OpenAIEmbeddings()
    index_name = "sainapsis"
    docsearch = Pinecone.from_existing_index(index_name, embeddings)
    qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="refine",
                                     retriever=docsearch.as_retriever(type="similarity"))
    query = "Ingenieria de software esta acreditada?"

def main():
    llm = ChatOpenAI(temperature=0)
    tools = [
        say_hello,
        say_dog_name,
        college_programs_info
    ]
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        verbose=True
    )
    print(agent.run("El programa de Ingenieria de sistemas tiene acreditacion?"))


if __name__ == '__main__':
    main()
