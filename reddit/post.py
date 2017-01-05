"""
Post class for Reddit
Reinventing the wheel
"""

class RedditPost(object):
    """
    ClassDoc
    """
    post_counter = 0

    def __init__(self,name,link):
        self.serialno = RedditPost.post_counter
        RedditPost.post_counter += 1
        self.link = link
        self.name = name

