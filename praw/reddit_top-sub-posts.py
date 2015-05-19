#!/usr/bin/env python

import praw
r = praw.Reddit(user_agent='user')
submissions = r.get_subreddit('python').get_hot(limit=5)
print [str(x) for x in submissions]