from typing import List, Optional

from rich.console import Console

from langchain_core.pydantic_v1 import BaseModel, Field, validator
from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama

console = Console()

class Tut(BaseModel):
    """Information about a tut"""
    title:str = Field(...,description="The title of the tut")
    introduction:str = Field(...,description="The introduction fo the tut")
    price:float = Field(...,description="The price of the tut")


class TutList(BaseModel):
    """all tuts in a blog"""
    tuts:List[Tut]


parser = PydanticOutputParser(pydantic_object=TutList)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Answer the user query. Wrap the output in `json` tags\n{format_instructions}",
        ),
        ("human", "{query}"),
    ]
).partial(format_instructions=parser.get_format_instructions())
# console.print(parser.get_format_instructions())
# exit(0)


# console.print(prompt)
llm = ChatOllama(model="mistral")
query = "The basic machin learning of Tut is about all algorithm in machine learning ,ande its price is about 29.9"
chain = prompt | llm | parser

resp = chain.invoke({"query": query})
console.print(resp)