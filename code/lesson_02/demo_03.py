from rich.console import Console

from langchain_core.prompts.chat import ChatPromptTemplate,AIMessagePromptTemplate
from langchain_community.chat_models import ChatOllama

console = Console()

chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a help AI bot Your name is {name}"),
        ("human","hello, how are you doing?"),
        ("ai","I'm doing well,thanks!"),
        ("human","{user_input}")
    ]
)

# messages = chat_template.format_messages(name="Bob",user_input="what is your name")

chat_model = ChatOllama(model="llama3.1")
chain = chat_prompt | chat_model 

resp = chain.invoke({
    "name":"Bob",
    "user_input":"what is your name?",
})

console.print(resp.content)
