import os
from langchain.tools import Tool, tool
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


@tool
def search_web(query: str) -> str:
    """Search the web for the given query"""
    results = tavily_client.search(query)
    return results