from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='/Users/gomes/Documents/Bot/chromedriver')
driver.get('https://web.whatsapp.com/') 
time.sleep(10)

driver.find_elements('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys("Pretinha")
driver.find_elements('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(Keys.ENTER)

for c in range(1, 21):
    driver.find_elements('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys("Te amo")
    driver.find_elements('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(Keys.ENTER)
