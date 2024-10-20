from rich.console import Console
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool, StructuredTool, tool
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper


console = Console()

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
class WikiInputs(BaseModel):
    """Inputs to the wikipedia tool"""
    query:str = Field(
        description="query to look up Wikipedia should be 3 or less words"
    )

tool = WikipediaQueryRun(
    name="wiki-tool",
    description="look up things in wikipedia",
    args_schema=WikiInputs,
    api_wrapper=api_wrapper,
    return_direct=True,
)

console.log(tool.name)
console.log(tool.description)
console.log(tool.args)