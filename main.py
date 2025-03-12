from bot.login import InstagramLogin
from bot.search import InstagramSearch
from config import * 
from time import sleep

bot = InstagramLogin(USERNAME, PASSWORD)

print("🔑 Logging in...")
bot.login()

sleep(10)

searcher = InstagramSearch(bot.driver)
searcher.search(KEYWORD)

sleep(10)

print("🚪 Logging out...")
bot.logout()
bot.close()
