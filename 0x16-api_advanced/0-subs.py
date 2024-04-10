#!/usr/bin/python3
'''
function to querry reddit API and return number of subscribers
'''
import requests
from requests import get


def number_of_subscribers(subreddit):
    'function to querry reddit API and return number of subscribers'

    req = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0
