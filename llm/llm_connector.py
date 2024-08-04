from langchain_mistralai import ChatMistralAI
from extras.constants import MISTRAL_MODEL, final_answer_prompt
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from llm.llm_helper import FinalAnswer, AgentState, reddit_node, llm_node
from langgraph.graph import END, StateGraph, START


def get_mistral_model():
    llm = ChatMistralAI(
        model=MISTRAL_MODEL,
        temperature=0,
        max_retries=2
    )
    return llm


def get_final_answer_llm():
    model = get_mistral_model()
    parser = JsonOutputParser(pydantic_object=FinalAnswer)
    final_answer_prompt_template = PromptTemplate(
        template=final_answer_prompt,
        input_variables=["query", "reddit_data"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )
    final_answer_llm = final_answer_prompt_template | model | parser
    return final_answer_llm


def get_graph():
    workflow = StateGraph(AgentState)
    workflow.add_node("reddit_node", reddit_node)
    workflow.add_node("llm_node", llm_node)
    workflow.add_edge(START, "reddit_node")
    workflow.add_edge("reddit_node", "llm_node")
    workflow.add_edge("llm_node", END)
    graph = workflow.compile()
    return graph


def get_responses(graph, limit, query, model):
    response = graph.invoke(
        {"limit": limit,
         "query": query,
         "final_answer_llm": model})
    return response
