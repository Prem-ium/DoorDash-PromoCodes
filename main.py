import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import traceback
from time import sleep
from dotenv import load_dotenv

# Load ENV
load_dotenv()

SIGNUP = False
if not os.environ["LOGIN"]:
    SIGNUP = True
    try:
        from random_words import RandomWords
    except ImportError:
        os.system("pip3 install RandomWords")
        from random_words import RandomWords
        pass
    finally:
        rw = RandomWords()
else:
    LOGIN = os.environ["LOGIN"]
    colonIndex = LOGIN.index(":")+1
    LOGIN_EMAIL = LOGIN[0:colonIndex-1]
    LOGIN_PASSWORD = LOGIN[colonIndex:len(LOGIN)]
    
if not os.environ["LOCAL_REST"] or not os.environ["LOCAL_ADDRESS"]:
    raise Exception("LOCAL_REST or LOCAL_ADDRESS env variables are not set/or not found. Please add them before running the program.")
else:
    RESTAURANT = os.environ["LOCAL_REST"]
    ADDY = os.environ["LOCAL_ADDRESS"]

def signUp(driver):
    driver.get("https://doordash.com/")
    print('Attempting to sign up...')
    sleep(5)
    EMAIL = rw.random_word() + rw.random_word() + rw.random_word() + '@gmail.com'
    PASSWORD = rw.random_word() + rw.random_word() + '!'
    try:
        driver.find_element(
            By.XPATH, value='/html/body/div[1]/div[1]/div[1]/header/div/div[2]/div[3]/a[2]/div/div/div/span/span').click()
    except:
        sleep(2)
    try:
        driver.find_element(
            By.XPATH, value='/html/body/div[1]/div[1]/div[1]/header/div/div[2]/div[3]/a[2]/div/div/div/span').click()
    except:
        sleep(2)
    try:
        driver.find_element(
            By.XPATH, value='/html/body/div[1]/div[1]/div[1]/header/div/div[2]/div[3]/a[2]').click()
    except:
        sleep(2)

    try:
        driver.find_element(By.ID, value='FieldWrapper-0').send_keys('John')
        sleep(3)
        driver.find_element(By.ID, value='FieldWrapper-1').send_keys('Doe')
        sleep(3)
        driver.find_element(
            By.ID, value='FieldWrapper-2').send_keys(f'{EMAIL}')
        sleep(3)
        driver.find_element(
            By.ID, value='FieldWrapper-4').send_keys('12345375984')
        sleep(2)
        driver.find_element(
            By.ID, value='FieldWrapper-5').send_keys(f'{PASSWORD}')
    except:
        pass
    try:
        driver.find_element(By.ID, value='sign-up-submit-button').click()
        print('Sign up successful!')
    except:
        try:
            driver.find_element(
                By.ID, value='FieldWrapper-5').send_keys(Keys.ENTER)
            print('Sign up successful!')
        except:
            print('Sign up may have failed...')
            raise Exception(f'Sign up failed...\n{traceback.format_exc()}')
        pass
    print(f'\nGenerated Account:\nEmail:\t{EMAIL}\nPassword:\t{PASSWORD}\n\n')
    return EMAIL, PASSWORD
def signin_doordash(driver):
    print('Attempting to sign in...')
    driver.get('https://www.doordash.com/consumer/login')
    sleep(10)
    try:
        driver.find_element(By.ID, value = 'IdentityLoginPageEmailField').send_keys(LOGIN_EMAIL)
    except:
        driver.find_element(By.ID, value = 'FieldWrapper-0').send_keys(LOGIN_EMAIL)
    try:
        driver.find_element(By.ID, value = 'IdentityLoginPagePasswordField').send_keys(LOGIN_PASSWORD)
    except:
        driver.find_element(By.ID, value = 'FieldWrapper-1').send_keys(LOGIN_PASSWORD)

    try:
        driver.find_element(By.XPATH, value = '/html/body/div[1]/div/div[1]/div/div/div/div/div/div/div/form/div/button/div/div/div/span').click()
    except:
        driver.find_element(By.ID, value = 'FieldWrapper-1').send_keys(Keys.ENTER)

def updateQuant(driver):
    print('Attempting to add quantity...')
    sleep(4)
    driver.get(f'{RESTAURANT}')
    sleep(5)
    try:
        driver.find_element(
            By.XPATH, value='/html/body/div[1]/main/div/div[1]/div[1]/div/div[3]/div/div/div/div[2]/div[1]/button').click()
    except:
        pass
    try:
        driver.find_element(
            By.XPATH, value='/html/body/div[1]/main/div/div[1]/div[1]/div/div[4]/div[3]/div[2]/div[3]/button').click()
    except Exception as e:
        pass
    try:
        col = driver.find_element(
            By.XPATH, value='//*[@id="__next"]/main/div/div[1]/div[1]/div/div[6]/div[2]')
        col = col.find_elements(By.XPATH, value='*')
        col[0].click()
    except:
        pass
    sleep(4)
    quant = driver.find_element(
        By.XPATH, value='//*[@id="prism-modal-footer"]/div/div/div/div[1]/div[3]/button')
    for i in range(8):
        quant.click()
        sleep(1)
    driver.find_element(
        By.XPATH, value='/html/body/div[1]/main/div/div[4]/div/div[2]/div/div[2]/div[3]/div/div/div/div/div/div[2]/button').click()
    sleep(10)
    print('Quantity Sucessfully Added')


chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_extension('honey.crx')
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.get('https://doordash.com/home')
sleep(5)
chwd = driver.window_handles
if (chwd[1]):
    driver._switch_to.window(chwd[1])
    driver.close()
    driver._switch_to.window(chwd[0])

if not SIGNUP:
    signin_doordash(driver)
    print('May have signed in sucessfully, possible verification required... Sleeping for 1 minute.')
    sleep(60)

    try:
        driver.find_element(By.XPATH, value='//*[@id="__next"]/main/div/div[1]/div/div[2]/div/div[3]/div/a/span').click()
    except:
        pass    
    try:
        driver.find_element(By.XPATH, value='/html/body/div[1]/main/div/div[1]/div/div[2]/div/div[3]/div/a/span').click()
    except:
        pass
    try:
        driver.find_element(By.XPATH, value = '//*[@id="__next"]/main/div/div[1]/div/div[1]/div/a[1]/div/div/div/span/span').click()
    except:
        pass
    sleep(7)

try:
    driver.find_element(By.TAG_NAME, value='input').send_keys(f'{ADDY}' + Keys.ENTER)
    sleep(2)
    driver.find_element(By.TAG_NAME, value='input').send_keys(Keys.ENTER)
except:
    print('Exception occured, hopefully you have already been signed in with existing address...')
    pass
sleep(5)
updateQuant(driver)
if SIGNUP:
    EMAIL, PASSWORD = signUp(driver)

driver.get('https://doordash.com/')

try:
    try:
        sleep(5)
        driver.find_element(
            By.XPATH, value='/html/body/div[1]/div[1]/div[4]/div/div[2]/div/div[2]/div/div[2]/div/div/div/button/div/div/div/span').click()
    except:
        pass
    driver.find_element(
        By.XPATH, value='/html/body/div[1]/div[1]/div[4]/div/div[2]/div/div[2]/div/div[2]/div/div/div/button').click()
except:
    pass
finally:
    sleep(3)

try:
    driver.find_element(
        By.XPATH, value='/html/body/div[1]/div[1]/div[1]/header/div/div[2]/div[2]/button/div/div/div/span/div/div').click()
except:
    sleep(2)
try:
    driver.find_element(
        By.XPATH, value='//*[@id="__next"]/main/div/div[1]/div/div[1]/header/div/div[2]/div[2]/button').click()
except:
    sleep(2)
try:
    driver.find_element(
        By.XPATH, value='/html/body/div[1]/main/div/div[1]/div/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/span/span/span/a').click()
except:
    sleep(5)
sleep(3)
try:
    driver.send_keys(Keys.TAB + Keys.TAB + Keys.ENTER)
except:
    pass
try:
    driver.find_element(
        By.XPATH, value='//*[@id="root"]/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/a/div/div/div/span/div/div[2]').click()
except:
    sleep(2)
try:
    driver.find_element(
        By.XPATH, value='/html/body/div[1]/main/div/div[1]/div/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/a').click()
except:
    sleep(2)
try:
    driver.find_element(
        By.XPATH, value='/html/body/div[1]/main/div/div[1]/div/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/a/div/div/div').click()
except:
    sleep(2)
try:
    driver.find_element(
        By.XPATH, value='/html/body/div[1]/main/div/div[1]/div/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/a/div/div/div/span/div/div[1]').click()
except:
    sleep(2)
try:
    driver.find_element(
        By.XPATH, value='//*[@id="__next"]/main/div/div[1]/div/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/a/div/div/div/span/div/div[1]').click()
except:
    pass
try:
    driver.find_element(
        By.XPATH, value='//*[@id="__next"]/main/div/div[1]/div/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/a/div/div/div/span').click()
except:
    pass
print('Arrived at Checkout')
sleep(10)

# TODO: Failsafe for if sign up still shows up in checkout

# PROMO (Cannot automate this, unfortunately)
try:
    sleep(4)
    driver.find_element(
        By.XPATH, value='/html/body/div[1]/div[1]/div[1]/div/div/div[1]/div[2]/div/div[1]/div[3]/div[3]/button/div/div[2]/span/span').click()
except:
    pass
finally:
    sleep(3)
try:
    driver.find_element(
        By.XPATH, value='/html/body/div[1]/div[1]/div[1]/div/div/div[1]/div[2]/div/div[1]/div[3]/div[3]/button').click()
except:
    pass
finally:
    sleep(3)
try:
    while True:

        try:
            driver.find_element(
                By.XPATH, value='/html/div//div[2]/div/div/div/div/div/div/div[1]/div[2]/div[3]/div/button/div/div').click()
        except:
            pass

        try:
            driver.find_element(By.CLASS_NAME, value='btnCopy-0-3-54').click()
        except:
            pass
        try:
            driver.find_element(By.XPATH, value='//*[@id="c1_g0"]').click()
        except:
            pass
        try:
            driver.find_element(By.XPATH, value='//*[@id="c1_g0"]/div').click()
        except:
            pass

        try:
            driver.find_element(
                By.XPATH, value='/html/div//div[2]/div/div/div/div/div/div/div[1]/div[2]/div[3]/div/button/div/div').click()
        except:
            pass
        try:
            driver.find_element(
                By.XPATH, value='/html/div//div[2]/div/div/div/div/div/div/div[1]/div[2]/div[3]/div/button').click()
        except:
            pass
        try:
            driver.find_element(
                By.XPATH, value='/html/div//div[2]/div/div/div/div/div/div/div[1]/div[2]/div[3]/div/button').click()
        except:
            pass
except:
    pass
