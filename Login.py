import random, string
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

# generate random string
def randompassword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

base_url="https://www.populix.co/login"
driver=webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(base_url)
email = driver.find_element_by_id("input_email")
password = driver.find_element_by_id("input_password")
email.send_keys("miaw.miaw@gmail.com")
password.send_keys(randompassword(10))
driver.find_element_by_id("submit_login").click()
sleep(5)
print("Login Failed")

email.click()
email.send_keys(Keys.CONTROL,"a")
email.send_keys(Keys.DELETE)
email.send_keys("nvindah.lestari29@gmail.com")
password.click()
password.send_keys(Keys.CONTROL,"a")
password.send_keys(Keys.DELETE)
password.send_keys(randompassword(10))
driver.find_element_by_id("submit_login").click()
sleep(5)
print("Login Failed")

email.click()
email.send_keys(Keys.CONTROL + "a")
email.send_keys(Keys.DELETE)
password.click()
password.send_keys(Keys.CONTROL + "a")
password.send_keys(Keys.DELETE)
email.send_keys("nvindah.lestari29@gmail.com")
password.send_keys("testQA123")
driver.find_element_by_id("submit_login").click()
sleep(2)
print("Login Success")
sleep(5)
driver.close()