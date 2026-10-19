from langchain.agents import create_agent
from langchain.messages import HumanMessage

from prompts import WEDDING_PLANNER_AGENT_PROMPT, USER_PROMPT_FOR_MAIN_AGENT
from agents import assign_to_subagent1, assign_to_subagent2
from llm import llm
import logging



logging.basicConfig(level=logging.INFO)


user_requirements = input("Enter your wedding planning requirements: ")

logging.info("initializing Main wedding planner agent...")
main_agent = create_agent(model=llm, tools=[assign_to_subagent1, assign_to_subagent2],
            name="MainAgent", system_prompt=WEDDING_PLANNER_AGENT_PROMPT.format(requirements=user_requirements))

logging.info("invoking Main wedding planner agent...")
response = main_agent.invoke({"messages" : [HumanMessage(content=USER_PROMPT_FOR_MAIN_AGENT)]})

print(response["messages"][-1].content)