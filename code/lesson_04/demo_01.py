from rich.console import Console
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser,DatetimeOutputParser
from langchain_community.chat_models import ChatOllama

console = Console()

output_parser = CommaSeparatedListOutputParser()
format_instructions = output_parser.get_format_instructions()
prompt = PromptTemplate(
    template="List five {subject}.\n{format_instructions}",
    input_variables=["subject"],
    partial_variables={"format_instructions": format_instructions}
)
llm = ChatOllama(model="mistral")
chain = prompt | llm | output_parser

output = chain.invoke({"subject" : "ice cream flavors"})
console.print(output)
