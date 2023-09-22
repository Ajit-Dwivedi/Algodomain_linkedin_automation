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
driver.get("https://linkedin.com")
driver.maximize_window()
time.sleep(3)

#**************Log In********************************************************************

username = driver.find_element(By.XPATH,"//input[@name='session_key']")
password = driver.find_element(By.XPATH,"//input[@name='session_password']")

username.send_keys("dwivediajit91@gmail.com")
password.send_keys("Anshu_d1995@")
time.sleep(3)
submit = driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(20)

#*******************My Network******************************************************************

all_anchor_tag = driver.find_elements(By.TAG_NAME,'a')
# print(all_anchor_tag[1].text)
anchor_tag = driver.find_element(By.CSS_SELECTOR,"a.app-aware-link.global-nav__primary-link > span.t-12.block.t-black--light.t-normal.global-nav__primary-link-text[title='My Network']")
# anchor_tag.click()
driver.execute_script("arguments[0].click();",anchor_tag)
# print(all_anchor_tag[2].text)
time.sleep(10)

#************************************Minimise messaging overlay******************************

# try:
#
#     button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='You are on the messaging overlay. Press enter to minimize it.']]"))
#     )
#  button.click()
# except Exception as e:
#     print(f"Error: {str(e)}")

minimise_message_overlay = driver.find_element(By.XPATH,"//button[.//span[text()='You are on the messaging overlay. Press enter to minimize it.']]")
minimise_message_overlay.click()

time.sleep(5)

#**********************************Accept/ignore invitations**************************************
#*************Accept********************
# Accept_invitation = driver.find_elements(By.XPATH,"//button[.//span[text()='Accept']]")
# Accept_invitation[0].click()
# # for ai in range(Accept_invitation):
# #     Accept_invitation[ai].click()
# time.sleep(10)

#**********************ignore********************************

Ignore_invitation = driver.find_elements(By.XPATH,"//button[.//span[text()='Ignore']]")
Ignore_invitation[0].click()
# for ii in range(Ignore_invitation):
#     Accept_invitation[ii].click()
time.sleep(5)

#************************************************

driver.quit()
