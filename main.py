from bot.login import InstagramLogin
from bot.search import InstagramSearch
from config import * 
from time import sleep
import instaloader

bot = InstagramLogin(USERNAME, PASSWORD)

print("🔑 Logging in...")
bot.login()

sleep(10)

L = instaloader.Instaloader()
profile = instaloader.Profile.from_username(L.context, '_ahmetibrahimpolat_')
print(profile.biography)

# sleep(10)

searcher = InstagramSearch(bot.driver)
searcher.search_by_url("https://www.instagram.com/gooddesignawards/?hl=en")
# searcher.search(KEYWORD)

sleep(10)

print("🚪 Logging out...")
bot.logout()
bot.close()
