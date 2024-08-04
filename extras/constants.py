import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")
MISTRAL_MODEL= os.getenv("MISTRAL_MODEL")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")


# LLM prompt


final_answer_prompt = """
    You are a friendly AI Researcher. You are asked to provide a detailed explanation by only data provided below.
    Question: {query}
    Reddit Data: {reddit_data}
    This is format to be followed:
    {format_instructions}
    """

