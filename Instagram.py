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
        self.driver.maximize_window()
        element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div')))
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div').click()
        to_follow = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]/ul').find_elements(By.TAG_NAME, 'li')
        i = 0
        follow_count = len(to_follow)
        print(f'to loop through {to_follow}')
        while i < follow_count:
            print(EC.visibility_of_element_located(to_follow[i])) # To be tested if EC can take a selenium object in this manner
            print(to_follow[i].find_elements(By.CSS_SELECTOR, "button.sqdOP").text) #Text to check if the correct button has been accessed. Will be replaced by clicking on button
            #Require code to check if the person has already been followed
            print("A")
            i += 1
            print(i)
            if i == len(to_follow):
                time.sleep(1)
                to_follow = self.driver.find_elements(By.CSS_SELECTOR, "ul.jjbaz div li")
                follow_count = len(to_follow)

    def find_target(self):
        print("input name of target")
        name = input()
        self.driver.get()
        search_bar = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_bar.send_keys(name)
        element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div._01UL2 > div.fuqBx > div")))
        time.sleep(1)
        search_results = self.driver.find_elements(By.CSS_SELECTOR, "div._01UL2 > div.fuqBx > div")
        handle = search_results[0].find_element(By.TAG_NAME, 'a').get_attribute('href')



