import os

from vocode import AgentUpdateParams, PromptUpdateParams

from .vocode import vocode_client


PHONE_NUMBER = os.getenv("PHONE_NUMBER")

def update_prompt():
    yoda_prompt = PromptUpdateParams(content="I want you to act as Yoda. Respond as Yoda would.")
    number = vocode_client.numbers.update_number(
        phone_number=PHONE_NUMBER, inbound_agent=AgentUpdateParams(prompt=yoda_prompt)
    )
    print(number)


def add_initial_message():
    number = vocode_client.numbers.update_number(
        phone_number=PHONE_NUMBER, inbound_agent=AgentUpdateParams(initial_message="Hello, I am Yoda.")
    )
