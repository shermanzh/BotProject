import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = uc.Chrome()
driver.set_window_size(900, 1200)
driver.get("https://www.amazon.com/hz/wishlist/ls/2IQ7SMGX6C9PZ?ref_=wl_share")

time.sleep(5)

items = driver.find_elements(By.CSS_SELECTOR, "li.g-item-sortable")

print(f"Items detected: {len(items)}")

for item in items:
    try:
        nameElement = item.find_element(By.CSS_SELECTOR, "h2 a.a-link-normal[title]")
        name = nameElement.get_attribute("title")

        priceElement = item.find_element(By.CLASS_NAME, "a-price-whole")
        price = priceElement.text.strip()
    except Exception:
        price = "N/A"

    print(f"{name}\nPrice: ${price}")


# allItems = driver.find_elements(By.CSS_SELECTOR, "h2 a.a-link-normal[title]")
# itemNames = [item.get_attribute("title") for item in allItems]
#
# print(f"Items detected: {len(itemNames)}")
#
# for item in itemNames:
#     print(f"Detected item: {item}")
#
# allPrices = driver.find_elements(By.CLASS_NAME, "a-price-whole")
#
# for price in allPrices:
#     print(f"Detected price: {price.text}")

time.sleep(5)
driver.quit()