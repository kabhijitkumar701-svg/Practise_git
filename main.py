# talk to ai models that runing on external servers

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client=OpenAI()
response=client.response.create(
    model="gpt-4.1-mini",
    input="what is the capital of up?"
)

print(response)