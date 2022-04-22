from selenium import webdriver
import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

browser = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME)
browser.get("http://naver.com")
print(browser.title)
browser.close()