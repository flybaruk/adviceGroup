from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--safebrowsing-disable-download-protection")
chrome_options.add_argument("--disable-signin-promo")
chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://rpachallenge.com/')

def Preenchimento(Nome, Sobrenome, RoleCompany, CompanyName, PhoneNumber, endeco, EmailAddress):

    # First Name
    Name = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//rpa1-field[@ng-reflect-dictionary-value='First Name']//input")
        )
    )
    Name.send_keys(Nome)

    # Last Name
    LastName = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//rpa1-field[@ng-reflect-dictionary-value='Last Name']//input")
        )
    )
    LastName.send_keys(Sobrenome)

    # Role in Company
    Role_in_Company = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//rpa1-field[@ng-reflect-dictionary-value='Role in Company']//input")
        )
    )
    Role_in_Company.send_keys(RoleCompany)

    # Company Name
    Company_Name = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//rpa1-field[@ng-reflect-dictionary-value='Company Name']//input")
        )
    )
    Company_Name.send_keys(CompanyName)

    # Phone Number
    Phone_Number = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//rpa1-field[@ng-reflect-dictionary-value='Phone Number']//input")
        )
    )
    Phone_Number.send_keys(PhoneNumber)

    # Address
    Address = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//rpa1-field[@ng-reflect-dictionary-value='Address']//input")
        )
    )
    Address.send_keys(endeco)

    # Email
    Email = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//rpa1-field[@ng-reflect-dictionary-value='Email']//input")
        )
    )
    Email.send_keys(EmailAddress)

    # Botão Submit
    SubmitButton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//input[@type='submit' and @value='Submit']")
        )
    )
    SubmitButton.click()
