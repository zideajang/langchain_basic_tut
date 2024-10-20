from rich.console import Console

from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool, StructuredTool, tool

console = Console()

@tool
def get_current_weather(city_name:str)->float:
    """get the temperature of city name"""
    return 30.0


console.print(get_current_weather.name,style="white on blue")
console.print(get_current_weather.description,style="white on blue")
console.print(get_current_weather.args)
