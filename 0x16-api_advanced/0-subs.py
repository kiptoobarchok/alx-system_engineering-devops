#!/usr/bin/python3
'''
function to querry reddit API and return number of subscribers
'''
import requests
import requests.exceptions


def number_of_subscribers(subreddit):
    'function to querry reddit API and return number of subscribers'
    #base url

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "My Reddit Subscriber Counter"}

    try:
        #Send request
        result = requests.get(url, headers=headers)
        #check for succesful response
        if result.status_code == 200:
            #store data
            data = result.json()

            #return subscriber count
            return data.get("data").get("subscribers")
        else:
            return 0
        
    except requests.exceptions.RequestException as e:
        print(f"Error!!: {e}")
        return 0
    
    