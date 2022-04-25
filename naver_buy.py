from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import pyperclip

os.environ['PW'] = 'itthere1!2@' # 비밀번호 설정

chrome = webdriver.Chrome("./chromedriver.exe") #browser
wait = WebDriverWait(chrome, 10) # wait
short_wait = WebDriverWait(chrome, 3) # short_wait

chrome.get("https://shopping.naver.com") #url 
# login_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a#gnb_login_button"))) - 요소가 생기기 전에 클릭
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a#gnb_login_button"))).click() # - 요소가 생긴 이후 클릭

input_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#id"))) # wait variable(ID)
input_pw = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#pw"))) # wait variable(PW)


pyperclip.copy("itthere2") # Copy - Control + c
input_id.send_keys(Keys.CONTROL, "v") # Paste - Control + v

pyperclip.copy(os.getenv("PW")) # Copy - Control + c
input_pw.send_keys(Keys.CONTROL, "v") # Paste - Control + v
input_pw.send_keys("\n") # Enter

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a#gnb_logout_button"))) # loginout btn search

search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name=query]"))) # naver input window
search.send_keys("강아지 가방") # search word
time.sleep(1) # 1`s waiting
search.send_keys("\n") # Enter

# wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class^=basicList_info_area__]")))

# # Scroll
# for i in range(8):
#     chrome.execute_script("window.scrollBy(0, " + str((i+1) * 1000) + ")")
#     time.sleep(0.5)

# items = chrome.find_elements_by_css_selector("div[class^=basicList_info_area__]")
# for item in items:
#     try:
#         # Ad Except
#         item.find_element_by_css_selector("button[class^=ad_]")
#         continue
#     except:
#         pass
#     print(item.find_element_by_css_selector("a[class^=basicList_link__]").text)

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[class^=basicList_link__]"))).click() # 첫번째 상품 클릭
time.sleep(2)

chrome.switch_to.window(chrome.window_handles[1]) # New Tap으로 이동

# Product Deteil Page
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[aria-haspopup='listbox']")))
options = chrome.find_elements_by_css_selector("a[aria-haspopup='listbox']")

# first option
options[0].click()
time.sleep(0.2)
chrome.find_element_by_css_selector("ul[role=listbox] li:nth-child(2) a[role=option]").click()
# chrome.find_element_by_css_selector("ul[role=listbox] a[role=option]")[1].click()

# second option
options[1].click()
time.sleep(0.2)
chrome.find_element_by_css_selector("ul[role=listbox] li:nth-child(1) a[role=option]").click()

# third option
options[2].click()
time.sleep(0.2)
chrome.find_element_by_css_selector("ul[role=listbox] li:nth-child(3) a[role=option]").click()

chrome.find_element_by_css_selector("div[class='OgETmrvExa N=a:pcs.buy'] a").click()
time.sleep(5)

chrome.quit() # All Close