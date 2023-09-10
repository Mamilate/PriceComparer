from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

input_person = input("What product do you want to compare? : ")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get("https://www.trendyol.com/")

WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"V8wbcUhU")))
trendyol_search = driver.find_element(By.CLASS_NAME,"V8wbcUhU")
trendyol_search.send_keys(f"{input_person}")
trendyol_search.send_keys(Keys.ENTER)

WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"prdct-desc-cntnr")))
product_desc = driver.find_elements(By.CLASS_NAME,"prdct-desc-cntnr")

WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"prc-box-dscntd")))
product_price = driver.find_elements(By.CLASS_NAME,"prc-box-dscntd")

for product, price in zip(product_desc,product_price):
    print(f"{product.text} : {price.text}")
