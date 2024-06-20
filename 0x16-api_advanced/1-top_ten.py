#!/usr/bin/python3
"""
prints the titles of the first 10 hot posts listed for a given subreddit
"""


import requests


def top_ten(subreddit):
    # defining the limit
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    # setting user-agent
    headers = {'User-Agent': 'My Reddit API Client'}

    try:
        # Making request with no redirects allowed
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Check for a 200 OK status code
        if response.status_code == 200:
            data = response.json()
            # check if data contains posts
            if 'data' in data and 'children' in data['data']:
                # Extract and print the titles of the first 10 posts
                for post in data['data']['children']:
                    print(post['data']['title'])
            else:
                print("None")
        else:
            print("None")
    except requests.exceptions.RequestException:
        print("None")
    except KeyError:
        print("None")
