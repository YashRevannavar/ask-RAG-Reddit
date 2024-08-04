from pydantic.v1 import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser


class FinalAnswer(BaseModel):
    answer: str = Field(..., description="The final answer to the question.")
    url: list[str] = Field(..., description="The list of urls that are used to generate the answer.")
    reddit_users: list[str] = Field(..., description="The list of reddit users that are used to generate the answer.")


def get_final_answer_llm(final_answer_prompt: str, model: object):
    parser = JsonOutputParser(pydantic_object=FinalAnswer)
    final_answer_prompt_template = PromptTemplate(
        template=final_answer_prompt,
        input_variables=["query", "reddit_data"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )
    final_answer_llm = final_answer_prompt_template | model | parser
    return final_answer_llm
