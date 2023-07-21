
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
#Go to the login page
driver.get("https://www.saucedemo.com/")
#driver.fullscreen_window()
driver.maximize_window()
time.sleep(5)

#Adding the username
driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys("standard_user")
time.sleep(1)

#Adding the password
driver.find_element(By.XPATH,'//input[@id="password"]').send_keys("secret_sauce")
time.sleep(1)

#Login into the dashboard
driver.find_element("xpath", "//input[@id='login-button']").click()
time.sleep(2)

#Click the item into the cart
driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
time.sleep(2)

#Click the cart to proceed ahead
driver.find_element("xpath", "//a[@class='shopping_cart_link']").click()
time.sleep(2)

#Click to remove product 
driver.find_element("xpath", "//button[@id='remove-sauce-labs-bike-light']").click()
time.sleep(2)

#Click the item into the cart
driver.find_element("xpath", "//button[@id='continue-shopping']").click()
time.sleep(2)

#Click the item into the cart
driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
time.sleep(2)

#Click the cart to proceed ahead
driver.find_element("xpath", "//a[@class='shopping_cart_link']").click()
time.sleep(2)

#Click the item into the cart
driver.find_element("xpath", "//button[@id='continue-shopping']").click()
time.sleep(2)

#Click the cart to proceed ahead
driver.find_element("xpath", "//a[@class='shopping_cart_link']").click()
time.sleep(2)

#Click the Checkout Button
driver.find_element("xpath", "//button[@id='checkout']").click()
time.sleep(2)

#Checkout: Your Information
#Adding the FirstName
driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys("Raj")
time.sleep(1)

#Adding the LastName
driver.find_element(By.XPATH,"//input[@id='last-name']").send_keys("Singh")
time.sleep(1)

#Adding the Postal Code
driver.find_element(By.XPATH,"//input[@id='postal-code']").send_keys("829107")
time.sleep(1)

#Click the Checkout Button
driver.find_element("xpath", "//input[@id='continue']").click()
time.sleep(2)

#Checkout: Overview


driver.find_element("xpath", "//button[@id='finish']").click()
time.sleep(2)

#Checkout: Complete!
driver.find_element("xpath", "//button[@id='back-to-products']").click()
time.sleep(2)

#Logout
driver.find_element("xpath", "//button[@id='react-burger-menu-btn']").click()
time.sleep(2)

driver.find_element("xpath", "//a[@id='logout_sidebar_link']").click()
time.sleep(2)
driver.quit()
#login_and_add_items_to_cart.robot

