from typing import TypedDict
from pydantic.v1 import BaseModel, Field

from dataloader.reddit_helper import QueryResult
from dataloader.reddit_loader import get_top_posts


class FinalAnswer(BaseModel):
    answer: str = Field(..., description="The final answer to the question.")
    url: list[str] = Field(..., description="The list of urls that are used to generate the answer.")
    reddit_users: list[str] = Field(..., description="The list of reddit users that are used to generate the answer.")


# State
class AgentState(TypedDict):
    final_answer_llm: object
    limit: int
    query: str
    reddit_data: QueryResult
    final_answer: FinalAnswer


# Nodes
def reddit_node(agent_state: AgentState):
    print(f"{'=' * 10} Reddit Node {'=' * 10}")
    agent_state["reddit_data"] = get_top_posts(agent_state["query"], agent_state["limit"])
    return {"reddit_data": agent_state["reddit_data"]}


def llm_node(agent_state: AgentState):
    print(f"{'=' * 10} LLM Node {'=' * 10}")
    model = agent_state["final_answer_llm"]
    query = agent_state["query"]
    reddit_data = agent_state["reddit_data"]
    response = model.invoke({"query": query, "reddit_data": reddit_data})
    agent_state["final_answer"] = response
    return {"final_answer": response}
