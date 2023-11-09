from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
from langchain.tools import tool


@tool("SayHello", return_direct=True)
def say_hello(name:str) -> str:
    """Answer when someone says hello"""
    return f"Hello {name}! My name is Sainapsis"


@tool("SayDogName", return_direct=True)
def say_dog_name(name:str) -> str:
    """Answer when someone mentions a dog"""
    return f"Hey! Your dog is called {name}"


def main():
    llm = ChatOpenAI(temperature=0)
    tools = [
        say_hello,
        say_dog_name
    ]
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        verbose=True
    )
    print(agent.run("The name of my dog is Sam"))


if __name__ == '__main__':
    main()
