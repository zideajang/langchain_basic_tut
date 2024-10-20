from langchain_core.prompts import PromptTemplate
from langchain_ollama.llms import OllamaLLM

template = """Question: {question}
Answer: Let's think step by step."""

MODEL_NAME = "mistral"

prompt = PromptTemplate.from_template(template)
llm = OllamaLLM(model=MODEL_NAME)
chain = prompt | llm
chain.invoke({"question":"write hello world"})