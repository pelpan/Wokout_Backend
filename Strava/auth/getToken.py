import requests
import os
from dotenv import load_dotenv
import json


def getToken(client_id, client_secret, code):
    load_dotenv()
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    code = os.getenv("CODE")

    url = "https://www.strava.com/oauth/token"
    payload = {
        "client_id": client_id,
        "client_secret": f"{client_secret}",
        "code": f"{code}",
        "grant_type": "authorization_code",
    }

    r = requests.post(url, data=payload)

    res = r.json()
    if r.status_code == 200:
        access_token = res["access_token"]
        refresh_token = res["refresh_token"]
        avatar = res["athlete"]["profile"]

        with open(".env", "a") as f:
            f.write(f"ACCESS_TOKEN={access_token}\n")
            f.write(f"REFRESH_TOKEN={refresh_token}\n")
            f.write(f"AVATAR={avatar}\n")

    print(r.json())


if __name__ == "__main__":
    load_dotenv()
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    code = os.getenv("CODE")
    getToken(client_id, client_secret, code)
