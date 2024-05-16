import requests;


def get(url, Headers):
    return requests.get(url, headers=Headers);