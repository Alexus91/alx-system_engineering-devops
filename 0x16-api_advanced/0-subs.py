#!/usr/bin/python3
"""Script that returns the numbers of
subscribers of a subreddit """

import requests as re


def number_of_subscribers(subreddit):

    apiUrl = "https://reddit.com/r/{}/about.json".format(subreddit)
    userAgent = "Mozilla/5.0"

    response = re.get(apiUrl, headers={"user-agent": userAgent})
    if not response:
        return 0
    result = response.json().get('data').get('subscribers')
    if result:
        return result
    else:
        return 0
