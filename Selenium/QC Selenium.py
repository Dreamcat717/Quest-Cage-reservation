from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = 'P:\Dokumenty\Studia\WSB - Tester\chromedriver02.exe'
driver = webdriver.Chrome(PATH)

# Go to the website and print its name
driver.get("https://questcage.pl/")
print(driver.title)

driver.maximize_window()
time.sleep(3)

# Close cookies
search = driver.find_element_by_id("cn-accept-cookie")
search.send_keys(Keys.RETURN)

# Go to reservations on Dębowa
link = driver.find_element_by_link_text("Rezerwacja Quest Cage - Dębowa").click()

# Choose the room
WebDriverWait(driver, 10).until(
    EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@src='https://rezerwacja.questcage.pl']")))

driver.find_element_by_xpath("/html/body/div[1]/div[6]/a").click()
time.sleep(5)

# change month
button = driver.find_element_by_xpath("/html/body/div[2]/button[3]")
button.send_keys(Keys.END)
time.sleep(1)

button.click()
time.sleep(1)
button.click()
time.sleep(6)

# scroll the page down
driver.switch_to.default_content()

scroll_script = "window.scrollTo(0,400)"
driver.execute_script(scroll_script)

# book a room
WebDriverWait(driver, 10).until(
    EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@src='https://rezerwacja.questcage.pl']")))

room = driver.find_element_by_xpath("//*[@id='calendar']/div[2]/div[2]/div[4]/div/div/a[1]")
room.click()
time.sleep(3)

# fill the form, first incorrectly and then in a correct way
username = driver.find_element_by_id("first_name")
username.send_keys("888")

surname = driver.find_element_by_id("last_name")
surname.send_keys("777")

# not sure why but people = driver.find_element_by_id("people").clear() doesn't seem to be working
people = driver.find_element_by_id("people")
people.clear()
people.click()
people.send_keys("6")

email = driver.find_element_by_id("email")
email.send_keys("agata717")

phone = driver.find_element_by_id("phone")
phone.send_keys("iii")

comment = driver.find_element_by_id("comment")
comment.send_keys("Błędnie wypełniona rezerwacja.")

rules = driver.find_element_by_id("accept_tos").click()
time.sleep(5)

accept = driver.find_element_by_css_selector("button.btn.btn-success.book.has-spinner").click()
time.sleep(3)

username.clear()
surname.clear()
people.clear()
email.clear()
phone.clear()
comment.clear()

username.send_keys("Agata")
surname.send_keys("Rabenda")
people.send_keys("4")
email.send_keys("agata717@op.pl")
phone.send_keys("111777111")
comment.send_keys("Poprawnie wypełniona rezerwacja.")

accept = driver.find_element_by_css_selector("button.btn.btn-success.book.has-spinner").click()
time.sleep(3)

accept02 = driver.find_element_by_xpath("//*[@id='success']/div/div/div[3]/button").click()