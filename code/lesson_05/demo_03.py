from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field, validator
class PetNameList(BaseModel):
    pet_name_list:list[str] = Field(...,description="name of pet list")

def generate_pet_name_with_parser(animal_type):
    parser = PydanticOutputParser(pydantic_object=PetNameList)

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "Answer the user query. Wrap the output in `json` tags\n{format_instructions}",
            ),
            ("human", "我有一个 {animal_type}  想给它起个可爱中文名字。 给我 5 候选的名字"),
        ]
    ).partial(format_instructions=parser.get_format_instructions())

    llm = ChatOllama(model="mistral")
    chain = prompt | llm | parser
    name = chain.invoke({"animal_type":animal_type})
    return name
    

def generate_pet_name(animal_type):

    # template = "I have a dog pet and I want a cool name for it. Suggest me five cool names for my pet."

    prompt_template_name = PromptTemplate(
        input_variables=['animal_type'],
        template="我有一个 {animal_type}  想给它起个可爱名字。 给我 5 候选的名字"
    )

    llm = ChatOllama(model="llama3.1")

    chain = prompt_template_name | llm
    name = chain.invoke({"animal_type":animal_type}).content

    return name


if __name__ == "__main__":
    print(generate_pet_name("dog"))