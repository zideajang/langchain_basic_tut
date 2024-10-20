from langchain_core.prompts import PromptTemplate
from termcolor import colored


prompt_template = PromptTemplate.from_template(
    "写一篇关于 {topic} 的博客"
)

resp = prompt_template.format(topic="agent")
print(colored(resp,'white','on_blue'))