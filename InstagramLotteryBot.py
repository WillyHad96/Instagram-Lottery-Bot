# IMPORTING LIBRARIES
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from string import ascii_lowercase as alphabet
import time

# CONSTANTS
#home_page_url = "https://www.instagram.com/p/C9ShpZcKd0S/"
home_page_url = "https://www.instagram.com/p/C9ON403qy2DmTONc5q_Aj9tS3yakjjvCDSKTyk0/"
driver = None
alphabet = 'abcdefghijklmnopqrstuvwxy'
options = Options()
options.add_experimental_option("detach", True)
textarea = None

# FUNCTIONS
def open_chrome():
    global driver
    # OPEN CHROME
    driver = webdriver.Chrome()
    driver.get(home_page_url)
    driver.maximize_window()
    time.sleep(3)


def allow_cookies():
    # ALLOW COOKIES BUTTON
    #allow_cookies_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]'))).click()
    allow_cookies_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]'))).click()
    time.sleep(1)


def click_login_button():
    # CLICK LOGIN BUTTON
    log_in_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='_acum'] div[class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1'] div:nth-child(1) a:nth-child(1)"))).click()
    time.sleep(3)


def log_in():
    # ENTER CREDENTIALS AND CLICK LOGIN BUTTON
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

    username.clear()
    password.clear()
    username.send_keys("guillermoteniasmoron@hotmail.com")
    password.send_keys("84264325gtm")
    time.sleep(1)
    sign_in_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='loginForm']/div/div[3]/button"))).click()
    time.sleep(8)


def save_login_info():
    # SAFE INFO BUTTON
    save_info_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='button']"))).click()
    time.sleep(5)

def click_photo():
        click_photo_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/div[2]/div/div/div[1]/a'))).click()
        time.sleep(5)

def add_comment(letter):
    global textarea

    try:
        # Locate and interact with the textarea
        #textarea = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/textarea")))
        textarea = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea")))
        textarea.clear()
        textarea.send_keys(Keys.SHIFT, '2')  # SHIFT + 2 is "@" symbol
        textarea.send_keys(letter)
        time.sleep(2)
    except (StaleElementReferenceException, TimeoutException, NoSuchElementException) as e:
        print(f"Error interacting with the textarea: {e}")
        # Retry locating and interacting with the element
        try:
            #textarea = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/textarea")))
            textarea = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea")))
            textarea.clear()
            textarea.send_keys(Keys.SHIFT, '2')  # SHIFT + 2 is "@" symbol
            textarea.send_keys(letter)
            time.sleep(2)
        except Exception as e:
            print(f"Retry failed: {e}")


def select_name():
    global textarea

    try:
        #textarea = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/textarea")))
        textarea = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea")))
        textarea.send_keys(Keys.ENTER)
        time.sleep(1)
    except (StaleElementReferenceException, TimeoutException, NoSuchElementException) as e:
        print(f"Error sending the comment: {e}")
        # Retry locating and interacting with the element
        try:
            #textarea = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/textarea')))
            textarea = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea")))           
            textarea.send_keys(Keys.ENTER)
            time.sleep(1)

        except Exception as e:
            print(f"Retry failed: {e}")


def click_name():
    global textarea

    try:
        #textarea = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/textarea")))
        textarea = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea")))
        textarea.send_keys(Keys.ENTER)
        time.sleep(1)
    except (StaleElementReferenceException, TimeoutException, NoSuchElementException) as e:
        print(f"Error sending the comment: {e}")
        # Retry locating and interacting with the element
        try:
            #textarea = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/textarea')))
            textarea = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea")))           
            textarea.send_keys(Keys.ENTER)
            time.sleep(1)

        except Exception as e:
            print(f"Retry failed: {e}")


def publish_comment():
    global textarea

    try:
        #textarea = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/textarea")))
        textarea = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea")))
        textarea.send_keys(Keys.ENTER)
        time.sleep(2)
    except (StaleElementReferenceException, TimeoutException, NoSuchElementException) as e:
        print(f"Error sending the comment: {e}")
        # Retry locating and interacting with the element
        try:
            #textarea = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/textarea')))
            textarea = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea")))           
            textarea.send_keys(Keys.ENTER)
            time.sleep(2)

        except Exception as e:
            print(f"Retry failed: {e}")


def finish_program():
    # FINISH PROGRAM
    driver.quit()


# MAIN PROGRAM
open_chrome()
time.sleep(15)
allow_cookies()
click_login_button()
log_in()
save_login_info()
click_photo()
for letter in alphabet:
  for i in range(1,4):
    add_comment(letter)
    select_name()
    for j in range(1,i):
      textarea.send_keys(Keys.ARROW_DOWN)
    click_name()
    publish_comment() 
finish_program()