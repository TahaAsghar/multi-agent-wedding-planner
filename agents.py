from langchain.agents import create_agent
from langchain.tools import tool
from langchain.messages import HumanMessage
from llm import llm
from tools import search_web
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Initializing subagent1")
subagent1 = create_agent(model=llm, tools=[search_web], name="SubAgent1")

logging.info("Initializing subagent2")
subagent2 = create_agent(model=llm, tools=[search_web], name="SubAgent2")


@tool
def assign_to_subagent1(query: str) -> str:
    """Delegate a research query to SubAgent1 and return its response."""

    logging.info(f"Assigning query to subagent1: {query}")
    response = subagent1.invoke({"messages" : [HumanMessage(content=query)]})
    return response["messages"][-1].content

@tool
def assign_to_subagent2(query: str) -> str:
    """Delegate a research query to SubAgent2 and return its response."""
    logging.info(f"Assigning query to subagent2: {query}")
    response = subagent2.invoke({"messages" : [HumanMessage(content=query)]})
    return response["messages"][-1].content