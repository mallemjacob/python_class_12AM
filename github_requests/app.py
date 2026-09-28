import requests


# Resonds back with JSON data
response = requests.get(
    'https://api.github.com/search/repositories?q=language:python+sort:stars')


# Convert JSON to python dictionary
converted_response = response.json()


# print(converted_response["items"][0])


for i in converted_response["items"]:
    print(i["name"])


# response = requests.get('https://dummyjson.com/carts')

# convterted_resposen = response.json()

# print(convterted_resposen)
