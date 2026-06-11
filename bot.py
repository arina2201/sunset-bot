from telegram import Bot

TOKEN = "8947973799:AAEPRDmCpotghvbKhLdJyvU-p0SNMneP5Ts"

bot = Bot(token=TOKEN)

updates = bot.get_updates()

for u in updates:
    try:
        print(u.message.chat.id, u.message.chat.title)
    except:
        pass
