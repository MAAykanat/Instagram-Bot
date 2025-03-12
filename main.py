from bot.login import InstagramLogin
from config import * 
from time import sleep

bot = InstagramLogin(USERNAME, PASSWORD)

print("🔑 Logging in...")
bot.login()

sleep(50)


print("🚪 Logging out...")
bot.logout()
#bot.close()
