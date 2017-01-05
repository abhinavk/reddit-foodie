"""
Foodie
"""

import json
import string
import random
import requests
from reddit.post import RedditPost
from pprint import pprint


CLIENT_ID = 'sTUuJHP3q6HjPA'

URL = 'http://www.reddit.com/r/foodporn/.json'
HEADERS = {'User-Agent': 'abhnv.com\'s reddit-foodie app',}


def save(arg='random'):
    pass

def main():
    res = requests.get(URL, headers=HEADERS)
    foodDict = json.loads(res.text)
    postsList = foodDict['data']['children'] # It's a list of all posts as dict
    posts = [RedditPost(postDict['data']['name'],
                        postDict['data']['url']) for postDict in postsList]

    for post in posts:
        pprint(post.link)

if __name__ == '__main__':
    main()
