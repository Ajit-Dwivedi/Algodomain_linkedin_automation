import time
import os
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

username = driver.find_element(By.XPATH,"//input[@name='session_key']")
password = driver.find_element(By.XPATH,"//input[@name='session_password']")

username.send_keys("dwivediajit91@gmail.com")
password.send_keys("Anshu_d1995@")

time.sleep(3)

username = driver.find_element(By.XPATH,"//button[@type='submit']").click()

time.sleep(3)

driver.get("https://www.linkedin.com/search/results/people/?network=%5B%22F%22%5D&origin=FACETED_SEARCH&sid=qzj")
time.sleep(3)

all_buttons = driver.find_elements(By.TAG_NAME,'button')
message_buttons = [btn for btn in all_buttons if btn.text == "Message"]
message_buttons[0].click()
#driver.execute_script("argument[0].click();",message_buttons[0])

time.sleep(4)

main_div = driver.find_element(By.XPATH,'//div[starts-with(@class,"msg-form__msg-content-container")]')
main_div.click()
#driver.execute_script("argument[0].click();",main_div)

paragraphs = driver.find_elements(By.TAG_NAME,'p')
paragraphs[-5].send_keys("kisa hai bhai")
time.sleep(3)
#finding the  p tag to send message
# paragraphs = driver.find_elements(By.TAG_NAME,'p')
# counter = 0
# for p in paragraphs:
#     print(counter)
#     print(p.text)
#     counter+=1

send_message = driver.find_element(By.XPATH,"//button[@type='submit']").click()
#driver.execute_script("argument[0].click();",send_message)

time.sleep(3)

#close_message_box = driver.find_element(By.XPATH,'//button[starts-with(@class,"msg-overlay-bubble-header__control")]')
#close_message_box = driver.find_element(By.XPATH,'//button[contains(@id,"ember")]')
#close_message_box = driver.find_element(By.CSS_SELECTOR,'button.msg-overlay-bubble-header__control')
#close_message_box.click()
#driver.execute_script("argument[0].click();",close_message_box)
# button_xpath = "//button[contains(., 'Close your conversation with Ajit Dwivedi and Tejas Choughule')]"
# button = driver.find_element(By.XPATH,'button_xpath').click()

buttons = driver.find_elements(By.TAG_NAME,'button')
buttons[-11].click()
# counter = 0
# for b in buttons:
#     print(counter)
#     print(b.text)
#     counter+=1
time.sleep(30)
# driver.implicitly_wait(30)
driver.quit()
