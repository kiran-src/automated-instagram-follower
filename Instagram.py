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
        print(f"Scroll Height: {self.driver.execute_script('return document.body.scrollHeight')}")
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
        element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/div/div/div[2]/ul')))
        time.sleep(1)
        to_follow = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]/ul').find_elements(By.TAG_NAME, 'li')
        i = 0
        follow_count = len(to_follow)
        print(f'to loop through {len(to_follow)}')
        followers_div = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div')
        while i < follow_count:
            if to_follow[i].find_element(By.CSS_SELECTOR, 'div button.sqdOP div').text == 'Follow':
                # require code to scroll appropriate amount
                print(to_follow[i].find_element(By.CSS_SELECTOR, "button.sqdOP").is_displayed())
                to_follow[i].find_element(By.CSS_SELECTOR, "button.sqdOP").click()
                time.sleep(2)
                print("Follow status is now " + to_follow[i].find_element(By.CSS_SELECTOR, 'div button.sqdOP div').text)
                self.driver.execute_script("arguments[0].scrollIntoView()", to_follow[i])
            else:
                print("Already Following")
            print(i)
            i += 1
            if i == len(to_follow):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)", followers_div)
                time.sleep(3)
                to_follow = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]/ul').find_elements(By.TAG_NAME, 'li')
                follow_count = len(to_follow)
                print(f"End of the line {len(to_follow)}")

    # def find_target(self):
    #     print("input name of target")
    #     name = input()
    #     self.driver.get()
    #     search_bar = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
    #     search_bar.send_keys(name)
    #     element = WebDriverWait(self.driver, 30).until(
    #         EC.presence_of_element_located(
    #             (By.CSS_SELECTOR, "div._01UL2 > div.fuqBx > div")))
    #     time.sleep(1)
    #     search_results = self.driver.find_elements(By.CSS_SELECTOR, "div._01UL2 > div.fuqBx > div")
    #     handle = search_results[0].find_element(By.TAG_NAME, 'a').get_attribute('href')