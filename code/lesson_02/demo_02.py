from rich.console import Console

from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama

console = Console()

template = "You are a helpful assistant that translates {input_language} to {output_language}."
human_template = "{text}"

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
])


MODEL_NAME  = "llama3.1"

chat_model = ChatOllama(model=MODEL_NAME)
chain = chat_prompt | chat_model 

resp = chain.invoke({
    "input_language":"chinese",
    "output_language":"english",
    "text":"我喜欢编程."
})

console.print(resp.content)