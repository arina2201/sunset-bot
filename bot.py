import os
import requests

TOKEN = os.environ["TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def main():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    r = requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": "test from GitHub Actions"
    })

    print(r.status_code)
    print(r.text)

if __name__ == "__main__":
    main()
