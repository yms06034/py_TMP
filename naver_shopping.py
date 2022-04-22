from selenium import webdriver
from selenium.webdriver.common.by import By # element 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time #py을 잠시 멈춰주는 용도
 
options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox")
# options.add_argument("headless") # 출력을 하지 않고 인코딩할 때 사용

chrome = webdriver.Chrome("./chromedriver.exe", options=options)
chrome.get("http://naver.com")
chrome.get("http://shopping.naver.com")
wait = WebDriverWait(chrome, 10)

def find(wait, css_selector):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

search = find(wait, "input[name=query]")
search.send_keys("강아지 가방 견체공학\n")

time.sleep(3)

chrome.close()