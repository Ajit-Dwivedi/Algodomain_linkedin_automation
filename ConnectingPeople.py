import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("C:\SeleniumDrivers\chromedriver.exe")

driver = webdriver.Chrome(options=chrome_options)
#driver.get("https://www.google.com")
driver.get("https://in.linkedin.com")
driver.maximize_window()
time.sleep(3)

#**************Log In********************************************************************

username = driver.find_element(By.XPATH,"//input[@name='session_key']")
password = driver.find_element(By.XPATH,"//input[@name='session_password']")

username.send_keys("dwivediajit91@gmail.com")
password.send_keys("Anshu_d1995@")
time.sleep(3)
submit = driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(3)
driver.get("https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH&page=2&sid=3F7")
time.sleep(3)
all_buttons = driver.find_elements(By.TAG_NAME,'button')
connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]
for btn in connect_buttons:
    print(btn.text)
    driver.execute_script("arguments[0].click();",btn)
    #btn.click()
    send_now = driver.find_element(By.XPATH,'//button[@aria-label="Send now"]')
    # send_now.click()
    driver.execute_script("arguments[0].click();", send_now)
    time.sleep(6)

driver.quit()