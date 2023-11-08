#!/usr/bin/python3
""" recursive function that queries the Reddit API """
from requests import get


def recurse(subreddit, hot_list=[], after=""):

    Headers = {'user-agent': 'my-app/0.0.1'}

    if after is None:
        return hot_list

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    params = {
        'limit': 100,
        'after': after
    }

    xx = get(url, headers=Headers, params=params, allow_redirects=False)

    if xx.status_code != 200:
        return None

    try:
        js = xx.json()

    except ValueError:
        return None

    try:

        data = js.get("data")
        after = data.get("after")
        children = data.get("children")
        for child in children:
            post = child.get("data")
            hot_list.append(post.get("title"))

    except Exception:
        return None

    return recurse(subreddit, hot_list, after)
