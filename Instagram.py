from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

DRIVER_PATH = "C:\Program Files\selenium_chromedriver_win32\chromedriver.exe"

class Instagram:
    def __init__(self):
        self.s = Service(DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.s)

    def login(self, email, passw):
        self.driver.get("https://www.instagram.com/accounts/login/")
        element = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, 'input')))
        input_tag = self.driver.find_elements(By.TAG_NAME, 'input')
        input_tag[0].send_keys(email)
        input_tag[1].send_keys(passw)
        input_tag[1].send_keys(Keys.ENTER)
        element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div').click()

    def followers(self, target):
        self.driver.get(target)
        element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div')))
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div').click()



