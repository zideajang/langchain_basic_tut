from typing import Optional, Type
from langchain.pydantic_v1 import BaseModel, Field

from langchain.tools import BaseTool, StructuredTool, tool

from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)

class SearchInput(BaseModel):
    query: str = Field(description="should be a search query")


class CustomSearchTool(BaseTool):
    name = "custom_search"
    description = "useful for when you need to answer questions about current events"
    args_schema: Type[BaseModel] = SearchInput

    def _run(
        self,query:str, run_manager:Optional[CallbackManagerForToolRun] = None
    )->str:
        """Use the tool"""
        return "LangChain"
    
    async def _arun(
        self,query:str, run_manager:Optional[AsyncCallbackManagerForToolRun] = None
            
    )->str:
        """Use the tool asynchronouse"""
        raise NotImplementedError("custom_search does not support yet")
    

search = CustomSearchTool()
print(search.name)
print(search.description)
print(search.args)