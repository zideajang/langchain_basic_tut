import json
import time

from rich.console import Console

from typing import List, Sequence, TypedDict,Annotated
from langchain_core.messages import BaseMessage, HumanMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser

base_information = "3 Unusual Use Cases for LLMs"

class AgentState(TypedDict):
    topic:str
    title:str
    sections:List[str]
    contents:List[str]


console = Console()


# 生成 title Agent
def generate_title():
    llm = ChatOllama(model="llama3.1",format="json")
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system","you are a helpful AI assistant"),
            ("human", "Generate a clickworthy title about this topic: '{base_information}'. Respond in JSON format {{title: 'title', topic: '{base_information}'}}"),
        ]
    )
    # prompt 
    return prompt | llm |StrOutputParser()

# 生成章节 Agent
def generate_sections():
    llm = ChatOllama(model="llama3.1",format="json")
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system","you are a helpful AI assistant"),
            ("human", """

Generate a compelling 3 section outline given this information: '{base_information}'. Respond in JSON format {{title: '<title>', topic: '<topic>', sections: ['<section1>', '<section2>', '<section3>']}}
"""),
        ]
    )
    return prompt | llm |StrOutputParser()

# 生成内容 Agent
def generate_contents():
    llm = ChatOllama(model="llama3.1",format="json")
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system","you are a helpful AI assistant"),
            ("human", """
Generate 1 paragraph of content for each section outline given this information: '{base_information}'. Respond in JSON format {{title: '<title>', topic: '<topic>', sections: ['<section1>', '<section2>', '<section3>'], content: ['<content1>', '<content2>', '<content3>']}}
"""),
        ]
    )
    return prompt | llm |StrOutputParser()

# generate title task
def generate_title_node(state: AgentState):
    console.print("gen title",style="white on blue")
    agent = generate_title()
    rsp = agent.invoke({"base_information":state["topic"]})
    state['title'] = json.loads(rsp)['title']
    return state
    
def generate_sections_node(state: AgentState):
    console.print("gen sections",style="white on blue")
    agent = generate_sections()
    rsp = agent.invoke({"base_information":f"topic:{state['topic']},title:{state['title']}"})
    state['sections'] = json.loads(rsp)['sections']
    # console.print(rsp)
    return state

def generate_contents_node(state: AgentState):
    console.print("gen sections",style="white on blue")
    agent = generate_contents()
    rsp = agent.invoke({"base_information":f"topic:{state['topic']},title:{state['title']},sections:{state['sections']}"})
    console.print(rsp)

    return state
agent_state = AgentState()
agent_state["topic"] = "write article about memory agent "

state = generate_title_node(agent_state)
console.print(state)
time.sleep(10)
state = generate_sections_node(state)
console.print(state)
time.sleep(10)
state = generate_contents_node(state)
console.print(state)