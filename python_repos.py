import requests


# Make an API call and check the response.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "?q=language:python+sort:stars+stars:>10000"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Convert the response object to a dictionary.
response_dict = r.json()

# Process rerults.
print(response_dict.keys())
