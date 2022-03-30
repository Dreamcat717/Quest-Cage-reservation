from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = 'P:\Dokumenty\Studia\WSB - Tester\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get("https://questcage.pl/")
print(driver.title)

driver.maximize_window()
time.sleep(3)

# Close cookie
search = driver.find_element_by_id("cn-accept-cookie")
search.send_keys(Keys.RETURN)

link = driver.find_element_by_link_text("Rezerwacja Quest Cage - Dębowa").click()

driver.get("https://rezerwacja.questcage.pl/7/set")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "--------- Piekło Hazardzisty ---------- ( 70 min ) ceny od 160 zł do 220 zł "))
    )
finally:
    driver.click()

pieklo = driver.find_element_by_css_selector('[href^=https://rezerwacja.questcage.pl/7/set]').click()
