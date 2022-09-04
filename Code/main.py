from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

FB_EMAIL = "USER'S EMAIL ID"
FB_PASSWORD = "USER'S FACEBOOK PASSWORD"

chrome_driver_path_service = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path_service)

driver.get("https://tinder.com/")
driver.maximize_window()

sleep(2)
login_btn = driver.find_element(By.XPATH, '//*[@id="c-1560500889"]/div/div[1]/div/main/div['
                                          '1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
print(login_btn.text)
login_btn.click()

sleep(2)
more_opt = driver.find_element(By.XPATH, '//*[@id="c1006085331"]/main/div/div[1]/div/div/div[3]/span/button')
more_opt.click()

sleep(2)
login_fb = driver.find_element(By.XPATH, '//*[@id="c1006085331"]/main/div/div[1]/div/div/div[3]/span/div['
                                         '2]/button/span[2]')
print(login_fb.text)
login_fb.click()

sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element(By.XPATH, '//*[@id="email"]')
password = driver.find_element(By.XPATH, '//*[@id="pass"]')
email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)
sleep(5)

cookies = driver.find_element(By.XPATH, '//*[@id="c-1560500889"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
cookies.click()

allow_location_button = driver.find_element(By.XPATH, '//*[@id="c1006085331"]/main/div/div/div/div[3]/button[1]/span')
allow_location_button.click()

allow_loc_btn = driver.find_element(By.XPATH, '//*[@id="c1006085331"]/main/div/div/div/div[3]/button[1]/span')
allow_loc_btn.click()

sleep(10)
counter = 0
while counter < 100:
    sleep(3)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_RIGHT)
    # sleep(3)
    # driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_LEFT)
    counter += 1
