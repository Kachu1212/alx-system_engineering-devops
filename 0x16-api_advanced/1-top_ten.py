#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
     url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    header = {"User-Agent": "Mozilla/5.0"}

    data = requests.get(url, headers=header, allow_redirects=False)

    if data.status_code == 200:
        data = data.json().get("data").get("children")
        for element in data:
            print(element.get("data").get("title"))
    else:
        print(None)
