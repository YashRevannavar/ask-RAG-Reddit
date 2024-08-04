from langchain_mistralai import ChatMistralAI
from extras.constants import MISTRAL_MODEL


def get_mistral_model():
    llm = ChatMistralAI(
        model=MISTRAL_MODEL,
        temperature=0,
        max_retries=2
    )
    return llm


