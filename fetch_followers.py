import requests
import json

HANDLE = 'romerogames.bsky.social'  # replace with your handle

url = f"https://public.api.bsky.app/xrpc/app.bsky.actor.getProfile?actor={HANDLE}"
response = requests.get(url)
followers = response.json().get("followersCount", 0)

with open("followers.json", "w") as f:
    json.dump({"number": followers}, f)

