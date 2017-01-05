"""
Foodie
"""

import json
import os
import random
import requests
from reddit.post import RedditPost
from pprint import pprint

CLIENT_ID = 'sTUuJHP3q6HjPA'
URL = 'http://www.reddit.com/r/foodporn/.json'
HEADERS = {'User-Agent': 'abhnv.com\'s reddit-foodie app',}


def getSavedLinks():
    list_files = []
    if os.path.exists('saves'):
        list_files = {i.split('.')[0] for i in os.listdir('saves')}
    return list_files


def save(arg='random'):
    pass


def downloadLink(post):
    # pprint(os.listdir('.'))
    response = requests.get(post.link)
    if response.status_code == 200:
        with open('./saves/' + post.name + '.jpg', 'wb') as f:
            f.write(response.content)


def main():
    response = requests.get(URL, headers=HEADERS)
    foodDict = json.loads(response.text)
    postsList = foodDict['data']['children'] # It's a list of all posts as dict
    posts = [RedditPost(postDict['data']['name'],
                        postDict['data']['preview']['images'][0]['source']['url'])
             for postDict in postsList
             if postDict['data']['stickied'] is False]

    existing_links = getSavedLinks() # Set of names of already saved files

    for post in posts:
        serial = str(post.serialno + 1)
        if post.name in existing_links:
            pprint('Downloading image ' + serial + '...Found cached copy')
        else:
            pprint('Downloading image ' + serial)
            downloadLink(post)


if __name__ == '__main__':
    main()
