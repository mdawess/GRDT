import praw
import pandas as pd

client_id = 'W3su_ylhX1sHOg'
client_secret = '2nuNtAGM85ZGtBvWt45VwVNKdDzg2g'
user_agent = 'wsb_scraper'

# Creating a reddit instance
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret, user_agent=user_agent)

# Create a subreddit instance
wsb = 'wallstreetbets'
subreddit = reddit.subreddit(wsb)

query = ['$']

for item in query:
    post_dict = {
        "title": [],
        "body": []
    }
    comments_dict = {
        "comment_body": [],
    }
    for submission in subreddit.search(query, sort="top", limit=100):
        post_dict["title"].append(submission.title)
        post_dict["body"].append(submission.title)

        # Acessing comments on the post
        submission.comments.replace_more(limit=100)
        for comment in submission.comments.list():
            comments_dict["comment_body"].append(comment.body)

    post_comments = pd.DataFrame(comments_dict)

    post_comments.to_csv("_comments_" + item + "subreddit.csv")
    post_data = pd.DataFrame(post_dict)
    post_data.to_csv("_" + item + "subreddit.csv")
