def main():
    from llm.llm_connector import get_responses, get_final_answer_llm, get_graph
    from pprint import pprint

    limit = 3
    query = "How to learn Machine learning?"
    model = get_final_answer_llm()
    graph = get_graph()
    response = get_responses(graph, limit, query, model)
    pprint(f"Response : {response['final_answer']['answer']}")
    pprint(f"Sources : {response['final_answer']['url']}")
    pprint(f"Reddit Users : {response['final_answer']['reddit_users']}")


if __name__ == '__main__':
    main()
