import praw
from pydantic import BaseModel
from typing import List, Optional

from extras.constants import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT


def get_reddit_client():
    return praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT
    )


class Comment(BaseModel):
    author: Optional[str] = None
    body: str
    score: int


class PostInfo(BaseModel):
    title: str
    url: str
    subreddit: str
    posted_by: Optional[str] = None
    comments: List[Comment]


class QueryResult(BaseModel):
    query: str
    posts: List[PostInfo]
