import json

from rich.console import Console
from langchain_community.chat_models import ChatOllama

console = Console()

MODEL_NAME = "llama3.1"

llm = ChatOllama(model=MODEL_NAME)
resp = llm.invoke("write hello world in python")
console.print(resp)
# print(colored(resp.content,'white','on_blue'))