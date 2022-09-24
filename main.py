import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import traceback
from time import sleep
from dotenv import load_dotenv

# Load ENV
load_dotenv()

AUTO_SIGNIN = os.environ.get('AUTO_SIGNIN', 'false')
if AUTO_SIGNIN.lower() == 'true':
    AUTO_SIGNIN = True
    if not os.environ["LOGIN"]:
        raise Exception('AUTO_SIGNIN set to true, however the LOGIN environment variable is not set!')
    else:
        LOGIN_EMAIL, LOGIN_PASSWORD = os.environ["LOGIN"].split(':')
        HANDLE_CART = os.environ.get('HANDLE_CART', 'true')
        if HANDLE_CART.lower() == 'true':
            HANDLE_CART = True
        else:
            HANDLE_CART = False
        print(
            f'Auto-sign in enabled with {LOGIN_EMAIL}.\nHandle Cart is set to {HANDLE_CART}\n')
else:
    AUTO_SIGNIN = False
    try:
        from random_words import RandomWords
    except ImportError:
        os.system("pip3 install RandomWords")
        from random_words import RandomWords
        pass
    finally:
        rw = RandomWords()
        HANDLE_CART = True
        print(f'Auto-sign in disabled.\nNew DoorDash login will be generated for new user test case.\nHandle Cart is set to {HANDLE_CART}\n')


if (not os.environ["LOCAL_REST"] or not os.environ["LOCAL_ADDRESS"]) and HANDLE_CART:
    raise Exception(
        f"LOCAL_REST or LOCAL_ADDRESS env variables are not set/or not found, while handle cart is set to {HANDLE_CART}.\nPlease set these variables and try again.")
else:
    RESTAURANT = os.environ["LOCAL_REST"]
    ADDY = os.environ["LOCAL_ADDRESS"]

def getDriver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_extension('honey.crx')
    try:
        driver = webdriver.Chrome(options=chrome_options)
    except:
        driver = webdriver.Chrome(
                service=Service(ChromeDriverManager(cache_valid_range=30).install()),
                options=chrome_options)
    driver.maximize_window()
    return driver
def signUp(driver):
    driver.get("https://doordash.com/")
    print('\nAttempting to sign up...\n')
    sleep(5)
    EMAIL = rw.random_word() + rw.random_word() + rw.random_word() + '@gmail.com'
    PASSWORD = rw.random_word() + rw.random_word() + '!'
    try:
        driver.find_element(By.XPATH, value='/html/body/div[1]/div[1]/div[1]/header/div/div[2]/div[3]/a[2]/div/div/div/span/span').click()
    except:
        sleep(2)
    try:
        driver.find_element(By.XPATH, value='/html/body/div[1]/div[1]/div[1]/header/div/div[2]/div[3]/a[2]/div/div/div/span').click()
    except:
        sleep(2)
    try:
        driver.find_element(By.XPATH, value='/html/body/div[1]/div[1]/div[1]/header/div/div[2]/div[3]/a[2]').click()
    except:
        sleep(2)

    try:
        driver.find_element(By.ID, value='FieldWrapper-0').send_keys('John')
        sleep(3)
        driver.find_element(By.ID, value='FieldWrapper-1').send_keys('Doe')
        sleep(3)
        driver.find_element(By.ID, value='FieldWrapper-2').send_keys(f'{EMAIL}')
        sleep(3)
        driver.find_element(By.ID, value='FieldWrapper-4').send_keys('12345375984')
        sleep(2)
        driver.find_element(By.ID, value='FieldWrapper-5').send_keys(f'{PASSWORD}')
    except:
        pass
    try:
        driver.find_element(By.ID, value='sign-up-submit-button').click()
        print('Sign up successful!')
    except:
        try:
            driver.find_element(By.ID, value='FieldWrapper-5').send_keys(Keys.ENTER)
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
        driver.find_element(By.ID, value='IdentityLoginPageEmailField').send_keys(LOGIN_EMAIL)
    except:
        driver.find_element(By.ID, value='FieldWrapper-0').send_keys(LOGIN_EMAIL)
    try:
        driver.find_element(By.ID, value='IdentityLoginPagePasswordField').send_keys(LOGIN_PASSWORD)
    except:
        driver.find_element(By.ID, value='FieldWrapper-1').send_keys(LOGIN_PASSWORD)

    try:
        driver.find_element(By.XPATH, value='/html/body/div[1]/div/div[1]/div/div/div/div/div/div/div/form/div/button/div/div/div/span').click()
    except:
        driver.find_element(By.ID, value='FieldWrapper-1').send_keys(Keys.ENTER)


def updateQuant(driver):
    print('Attempting to add quantity...')
    sleep(4)
    driver.get(f'{RESTAURANT}')
    sleep(5)
    try:
        driver.find_element(By.XPATH, value='/html/body/div[1]/main/div/div[1]/div[1]/div/div[3]/div/div/div/div[2]/div[1]/button').click()
    except:
        pass
    try:
        driver.find_element(By.XPATH, value='/html/body/div[1]/main/div/div[1]/div[1]/div/div[4]/div[3]/div[2]/div[3]/button').click()
    except Exception as e:
        pass
    try:
        col = driver.find_element(By.XPATH, value='//*[@id="__next"]/main/div/div[1]/div[1]/div/div[6]/div[2]')
        col = col.find_elements(By.XPATH, value='*')
        col[0].click()
    except:
        pass
    sleep(4)
    quant = driver.find_element(By.XPATH, value='//*[@id="prism-modal-footer"]/div/div/div/div[1]/div[3]/button')
    for i in range(8):
        quant.click()
        sleep(1)
    driver.find_element(By.XPATH, value='/html/body/div[1]/main/div/div[4]/div/div[2]/div/div[2]/div[3]/div/div/div/div/div/div[2]/button').click()
    sleep(10)
    print('Quantity Sucessfully Added')


driver = getDriver()

driver.get('https://doordash.com/home')
sleep(5)
chwd = driver.window_handles
if (chwd[1]):
    driver._switch_to.window(chwd[1])
    driver.close()
    driver._switch_to.window(chwd[0])

if AUTO_SIGNIN:
    signin_doordash(driver)
    print(driver.title)
    if "food" not in driver.title.lower() or "login" in driver.title.lower():
        print('May have signed in sucessfully, possible phone/email verification required... Sleeping for 1 minute.')
        sleep(60)
    print(driver.title)
    try:
        driver.find_element(By.XPATH, value='//*[@id="__next"]/main/div/div[1]/div/div[2]/div/div[3]/div/a/span').click()
    except:
        try:
            driver.find_element(By.XPATH, value='/html/body/div[1]/main/div/div[1]/div/div[2]/div/div[3]/div/a/span').click()
        except:
            try:
                driver.find_element(By.XPATH, value='//*[@id="__next"]/main/div/div[1]/div/div[1]/div/a[1]/div/div/div/span/span').click()
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

if HANDLE_CART:
    updateQuant(driver)

if not AUTO_SIGNIN:
    EMAIL, PASSWORD = signUp(driver)
    print(f'Signed up with the following generated credentials:\nEMAIL: {EMAIL}\nPASSWORD: {PASSWORD}')

driver.get('https://doordash.com/')

try:
    try:
        sleep(5)
        driver.find_element(By.XPATH, value='/html/body/div[1]/div[1]/div[4]/div/div[2]/div/div[2]/div/div[2]/div/div/div/button/div/div/div/span').click()
    except:
        pass
    driver.find_element(By.XPATH, value='/html/body/div[1]/div[1]/div[4]/div/div[2]/div/div[2]/div/div[2]/div/div/div/button').click()
except:
    pass
finally:
    sleep(3)

try:
    driver.find_element(By.XPATH, value='/html/body/div[1]/div[1]/div[1]/header/div/div[2]/div[2]/button/div/div/div/span/div/div').click()
except:
    sleep(2)
try:
    driver.find_element(By.XPATH, value='//*[@id="__next"]/main/div/div[1]/div/div[1]/header/div/div[2]/div[2]/button').click()
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
    driver.find_element(By.XPATH, value='//*[@id="root"]/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/a/div/div/div/span/div/div[2]').click()
except:
    sleep(2)
try:
    driver.find_element(By.XPATH, value='/html/body/div[1]/main/div/div[1]/div/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/a').click()
except:
    sleep(2)
try:
    driver.find_element(By.XPATH, value='/html/body/div[1]/main/div/div[1]/div/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/a/div/div/div').click()
except:
    sleep(2)
try:
    driver.find_element(By.XPATH, value='/html/body/div[1]/main/div/div[1]/div/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/a/div/div/div/span/div/div[1]').click()
except:
    sleep(2)
try:
    driver.find_element(By.XPATH, value='//*[@id="__next"]/main/div/div[1]/div/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/a/div/div/div/span/div/div[1]').click()
except:
    pass
try:
    driver.find_element(By.XPATH, value='//*[@id="__next"]/main/div/div[1]/div/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/a/div/div/div/span').click()
except:
    pass

print("Arrived at Checkout\nProgram has finished. Manually intervention needed. Please click the 'Apply Coupons' button to allow honey to find the best discounts available in this account.")

# PROMO (Cannot automate this, unfortunately)
# try:
#     sleep(4)
#     driver.find_element(By.XPATH, value='/html/body/div[1]/div[1]/div[1]/div/div/div[1]/div[2]/div/div[1]/div[3]/div[3]/button/div/div[2]/span/span').click()
# except:
#     try:
#         driver.find_element(By.XPATH, value='/html/body/div[1]/div[1]/div[1]/div/div/div[1]/div[2]/div/div[1]/div[3]/div[3]/button').click()
#     except:
#         pass
#     finally:
#         sleep(3)
# try:
#     try:
#         driver.find_element(By.XPATH, value='/html/div//div[2]/div/div/div/div/div/div/div[1]/div[2]/div[3]/div/button/div/div').click()
#     except:
#         pass

#     try:
#         driver.find_element(By.CLASS_NAME, value='btnCopy-0-3-54').click()
#     except:
#         pass
#     try:
#         driver.find_element(By.XPATH, value='//*[@id="c1_g0"]').click()
#     except:
#         pass
#     try:
#         driver.find_element(By.XPATH, value='//*[@id="c1_g0"]/div').click()
#     except:
#         pass

#     try:
#         driver.find_element(By.XPATH, value='/html/div//div[2]/div/div/div/div/div/div/div[1]/div[2]/div[3]/div/button/div/div').click()
#     except:
#         pass
#     try:
#         driver.find_element(By.XPATH, value='/html/div//div[2]/div/div/div/div/div/div/div[1]/div[2]/div[3]/div/button').click()
#     except:
#         pass
#     try:
#         driver.find_element(By.XPATH, value='/html/div//div[2]/div/div/div/div/div/div/div[1]/div[2]/div[3]/div/button').click()
#     except:
#         pass
# except:
#     pass
# finally:
#     print("Program has finished. Manually intervention needed. Please click the 'Apply Coupons' button to allow honey to find the best discounts available in this account.")
