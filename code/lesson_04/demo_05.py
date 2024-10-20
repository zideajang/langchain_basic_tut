from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama

from langchain_core.pydantic_v1 import BaseModel, Field

class PetName(BaseModel):
    name: str = Field(description="name of cat")
    reason: str = Field(description="answer to resolve the name of cat")


user_query = "我有一个小猫，想给它起个可爱中文名字,给出名字背后理由"

# Set up a parser + inject instructions into the prompt template.
parser = JsonOutputParser(pydantic_object=PetName)

prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)
llm = ChatOllama(model="mistral")
chain = prompt | llm | parser

resp = chain.invoke({"query": user_query})
print(resp)

