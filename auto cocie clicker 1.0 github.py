from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument("user-data-dir=C:\\Users\\Alice\\AppData\\Local\\Google\\Chrome\\User Data")
#You can find your user data by searching chrome://version/
driver = webdriver.Chrome(options=options)

driver.refresh
driver.get('https://orteil.dashnet.org/cookieclicker/')
time.sleep(1)
button = driver.find_element(By.ID,"bigCookie")
time.sleep(1)
while True:
    button.click()
    html_code=driver.page_source
    if "<div class=\"shimmer\" alt=\"Golden cookie\""  in html_code:
        golden_cookie = driver.find_element(By.CLASS_NAME,"shimmer")
        golden_cookie.click()



    
