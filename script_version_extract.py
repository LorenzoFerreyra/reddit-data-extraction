import praw
import json 

def get_comments(submission):

    comments=[]

    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        data={}
        data['body']=comment.body
        data['id']=comment.fullname

        try:
            data['author']=comment.author.name

        except AttributeError:
            data['author']=comment.author

        data['time']=comment.created_utc
        data['parent']=comment.parent_id

        comments.append(data)

    return comments


def get_metadata(submission):

    thread={}
    thread["title"]=submission.title
    thread["score"]=submission.score
    thread["id"]=submission.id
    thread["url"]=submission.url
    thread["comms_num"]=submission.num_comments
    thread["created"]=submission.created
    thread["body"]=submission.selftext
    
    thread['posts']= get_comments(submission)

    return thread



with open('reddit_credentials.json') as fin:
    
    creds = json.load(fin)
    

reddit = praw.Reddit(user_agent='Comment Extraction (by /u/{0})'.format(creds['username']),
                     client_id=creds['client_id'], client_secret=creds['client_secret'],
                     username=creds['username'], password=creds['password'])


subreddit = reddit.subreddit('devsarg')
query = "gpt OR ia OR chatgpt OR ia generativa OR vibe coding OR cursor OR llms OR va a dejarnos sin trabajo OR copilot OR github copilot OR chatgpt4 OR chatgpt-4 OR chat gpt 4 OR chat gpt4 OR chat gpt-4 OR chatgpt-4.0 OR chatgpt 4.0 OR chatgpt-4.0"


with open('devsarg_1.json', 'w') as fout:
    for submission in subreddit.search(query, sort="new", limit=1000):
        print("entered")
        thread = get_metadata(submission)
        json.dump(thread, fout)
        fout.write('\n')