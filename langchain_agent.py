
import os
from langchain_openai import OpenAI
from openai_key import openapi_key
from langchain.agents import AgentType, initialize_agent, load_tools

os.environ['OPENAI_API_KEY'] = openapi_key
llm = OpenAI(temperature=0.7)

def test_lang_chain():
    tools= load_tools(["wikipedia","llm-math"],llm=llm)
    agent= initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    agent.run("when does elon mask born")



test_lang_chain();


