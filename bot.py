import os
import requests
from telegram import Bot
from datetime import datetime, timedelta, timezone

TOKEN = os.environ["TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

LAT = 40.1872
LNG = 44.5152


def get_sunset():
    url = f"https://api.sunrise-sunset.org/json?lat={LAT}&lng={LNG}&formatted=0"
    data = requests.get(url).json()

    sunset_utc = data["results"]["sunset"]
    sunset = datetime.fromisoformat(sunset_utc.replace("Z", "+00:00"))

    return sunset.astimezone()


def main():
    bot = Bot(token=TOKEN)

    sunset = get_sunset()

    # Ереван UTC+4
    notify_time = sunset - timedelta(minutes=30)

    now = datetime.now(timezone.utc).astimezone()

    # запускаем только если сейчас >= времени уведомления
    if now >= notify_time and now < notify_time + timedelta(minutes=10):
        bot.send_message(
            chat_id=int(CHAT_ID),
            text="джаны, закат через 30 минут!"
        )

    print("done")


if __name__ == "__main__":
    main()
