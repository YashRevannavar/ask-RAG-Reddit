# ask-RAG-Reddit

A Retrieval-Augmented Generation (RAG) system that leverages Reddit content and Mistral AI to provide informative answers to user queries. The system searches across all of Reddit for relevant posts and comments, processes them using LangChain and LangGraph, and generates comprehensive answers using the Mistral AI language model.

## Features

- Reddit content retrieval from all subreddits
- Smart comment selection based on relevance and score
- AI-powered answer generation using Mistral AI
- Structured workflow using LangGraph
- Source attribution with Reddit post URLs and usernames

## Requirements

- praw
- langchain
- python-dotenv~=1.0.1
- langgraph~=0.1.19
- langchain_mistralai

## Project Structure

```
dataloader/              # Reddit data loading functionality
  reddit_helper.py     # Helper functions for Reddit API
  reddit_loader.py     # Core Reddit post/comment loader
extras/
  constants.py         # Configuration constants
llm/                     # LLM integration
  llm_connector.py     # Mistral AI and LangGraph setup
  llm_helper.py        # LLM utilities and state management
main.py                  # Main application entry point
requirements.txt         # Project dependencies
```

## How It Works

1. Query Processing: The system takes a user query as input
2. Reddit Search: Searches across all subreddits for relevant posts and comments
3. Content Filtering: Selects top posts and comments based on relevance and score
4. Answer Generation: Uses Mistral AI to generate a comprehensive answer
5. Source Attribution: Provides URLs and Reddit usernames for reference

## Usage

Example code:

```python
from llm.llm_connector import get_responses, get_final_answer_llm, get_graph

# Set up the components
limit = 3  # Number of Reddit posts to retrieve
query = "How to learn Machine learning?"
model = get_final_answer_llm()
graph = get_graph()

# Get the response
response = get_responses(graph, limit, query, model)

# Access the results
print(f"Answer: {response['final_answer']['answer']}")
print(f"Sources: {response['final_answer']['url']}")
print(f"Reddit Users: {response['final_answer']['reddit_users']}")