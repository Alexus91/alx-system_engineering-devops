#!/usr/bin/python3
"""queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit."""

import requests


def top_ten(subreddit):

    Urlapi = "https://reddit.com/r/{}/hot.json".format(subreddit)
    userAgent = "Mozilla/5.0"
    lims = 10

    response = requests.get(
        Urlapi, headers={"user-agent": userAgent}, params={"limit": lims})
    if not response:
        print('None')
        return
    response = response.json()
    lis_obj = response['data']['children']
    for obj in lis_obj:
        print(obj['data']['title'])
    return
