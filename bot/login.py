from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class InstagramLogin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()  # Ensure chromedriver is installed

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        username_input = self.driver.find_element(By.NAME, "username")
        password_input = self.driver.find_element(By.NAME, "password")

        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.RETURN)

        time.sleep(5)  # Wait for login process
        print("✅ Login successful!")

    def logout(self):
        """Logs out from Instagram."""
        self.driver.get("https://www.instagram.com/")
        time.sleep(3)

        try:
            # Click on profile button
            profile_button = self.driver.find_element(By.XPATH, "//img[contains(@alt, 'profile picture')]")
            profile_button.click()
            time.sleep(2)

            # Click on logout button
            logout_button = self.driver.find_element(By.XPATH, "//div[text()='Log out']")
            logout_button.click()
            time.sleep(3)

            print("🚪 Successfully logged out!")
        except Exception as e:
            print(f"❌ Logout failed: {e}")

    def close(self):
        """Closes the browser."""
        self.driver.quit()