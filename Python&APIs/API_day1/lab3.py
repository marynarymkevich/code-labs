import os
import requests
from dotenv import load_dotenv
from api_client import get_json

load_dotenv()
token = os.getenv("GITHUB_TOKEN")

headers = {
    "Authorization": f"Bearer {token}"
}

username = input("Enter GitHub username: ").strip()

url = f"https://api.github.com/users/{username}/repos"
params = {
    "sort": "pushed",
    "per_page": 5
}

repos = get_json(url, params=params, headers=headers)

if repos:
    print(f"\n5 latest pushed repositories for {username}:")
    for repo in repos:
        print(f"- {repo['name']}")


response_without_token = requests.get(url, timeout=5)
limit_without = response_without_token.headers.get("X-RateLimit-Limit")
print(f"X-RateLimit-Limit without token: {limit_without}")


response_with_token = requests.get(url, headers=headers, timeout=5)
limit_with = response_with_token.headers.get("X-RateLimit-Limit")
print(f"X-RateLimit-Limit with token: {limit_with}")