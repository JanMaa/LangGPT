import variables
from langchain.llms import OpenAI


llm = OpenAI(openai_api_key=variables.API_KEY)

llm("Tell me a joke")