from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import pyperclip

os.environ['PW'] = 'itthere1!2@'

chrome = webdriver.Chrome("./chromedriver.exe")
wait = WebDriverWait(chrome, 10)
short_wait = WebDriverWait(chrome, 3)

chrome.get("https://shopping.naver.com")
# login_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a#gnb_login_button"))) - 요소가 생기기 전에 클릭
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a#gnb_login_button"))).click() # - 요소가 생긴 이후 클릭

input_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#id")))
input_pw = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#pw")))


pyperclip.copy("itthere2")
input_id.send_keys(Keys.CONTROL, "v")

pyperclip.copy(os.getenv("PW"))
input_pw.send_keys(Keys.CONTROL, "v")
input_pw.send_keys("\n")

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a#gnb_logout_button")))

search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name=query]")))
search.send_keys("강아지 가방")
time.sleep(1)
search.send_keys("\n")

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class^=basicList_info_area__]")))

# Scroll
for i in range(8):
    chrome.execute_script("window.scrollBy(0, " + str((i+1) * 1000) + ")")
    time.sleep(0.5)

items = chrome.find_elements_by_css_selector("div[class^=basicList_info_area__]")
for item in items:
    try:
        # Ad Except
        item.find_element_by_css_selector("button[class^=ad_]")
        continue
    except:
        pass
    print(item.find_element_by_css_selector("a[class^=basicList_link__]").text)

chrome.close()