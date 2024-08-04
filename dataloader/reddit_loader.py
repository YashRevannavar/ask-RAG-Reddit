from dataloader.reddit_helper import PostInfo, Comment, QueryResult, get_reddit_client


def get_top_comments(post, limit):
    """
    Get the top comments for a given post
    :param post:
    :param limit:
    :return:
    """
    if limit == 0 or limit > 20:
        limit = 1
    post.comments.replace_more(limit=limit)
    comments = post.comments.list()
    top_comments = sorted(comments, key=lambda c: c.score, reverse=True)[:limit]
    comment_info = []
    for comment in top_comments:
        comment_info.append(Comment(
            author=str(comment.author) if comment.author else None,
            body=comment.body,
            score=comment.score
        ))
    return comment_info


def get_top_posts(query, limit):
    """
    Get the top posts for a given query
    :param query:
    :param limit:
    :return:
    """
    reddit = get_reddit_client()
    search_results = reddit.subreddit('all').search(query, sort='relevance', limit=limit)
    posts = []
    for post in search_results:
        post_info = PostInfo(
            title=post.title,
            url=post.url,
            subreddit=post.subreddit.display_name,
            posted_by=str(post.author) if post.author else None,
            comments=get_top_comments(post, limit//2)
        )
        posts.append(post_info)
    return QueryResult(query=query, posts=posts)
