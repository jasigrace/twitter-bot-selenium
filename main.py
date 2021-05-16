import time
from selenium import webdriver

PROMISED_UP = 10
PROMISED_DOWN = 150
TWITTER_EMAIL = "YOUR_MAIL_ID"
TWITTER_PASSWORD = "YOUR_PASSWORD"
chrome_driver_path = "C:\Development\chromedriver.exe"


class InternetSpeedTwitterBot:
    def __init__(self, driver):
        self.driver = webdriver.Chrome(executable_path=driver)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        # time.sleep(2)
        go = self.driver.find_element_by_class_name('start-text')
        go.click()
        time.sleep(60)
        self.down = self.driver.find_element_by_css_selector('.download-speed').text
        self.up = self.driver.find_element_by_css_selector('.upload-speed').text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(2)
        user_name = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        user_name.send_keys(TWITTER_EMAIL)
        time.sleep(1)
        password = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(1)
        login = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div')
        login.click()
        time.sleep(3)
        tweet_message = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/'
            'div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet_message.send_keys(f"Hey Internet Service Provider, why is my internet speed {self.down}down/{self.up}up "
                                f"when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        time.sleep(3)
        tweet = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/'
            'div[2]/div[4]/div/div/div[2]/div[3]')
        tweet.click()


internet_speed_twitter_bot = InternetSpeedTwitterBot(chrome_driver_path)
internet_speed_twitter_bot.get_internet_speed()
time.sleep(2)
internet_speed_twitter_bot.tweet_at_provider()
