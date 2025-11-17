import pandas as pd
from Preenchimento import Preenchimento
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
import time # ESSENCIAL para o retry loop

SELENIUM_HUB_URL = "http://selenium-hub:4444/wd/hub"

chrome_options = Options()
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--safebrowsing-disable-download-protection")
chrome_options.add_argument("--disable-signin-promo")
chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")

driver = None
MAX_RETRIES = 10
RETRY_DELAY = 5

for attempt in range(MAX_RETRIES):
    try:
        print(f"Tentativa {attempt + 1} de {MAX_RETRIES}: Conectando ao Hub...")
        driver = WebDriver(
            command_executor=SELENIUM_HUB_URL,
            options=chrome_options
        )
        print("Conexão estabelecida com sucesso!")
        break
    except Exception:
        if attempt < MAX_RETRIES - 1:
            time.sleep(RETRY_DELAY)
        else:
            print("ERRO CRÍTICO: Falha ao conectar ao Hub.")
            exit() # Sai do script se falhar

# 2. Execução da Automação (Se o driver foi conectado)
if driver:
    driver.get('https://rpachallenge.com/')

    # Carrega Excel
    df = pd.read_excel('challenge.xlsx')
    df.columns = df.columns.str.strip()

# Loop linha por linha
for index, row in df.iterrows():

    print(f"Preenchendo linha {index+1}/{len(df)}...")

    Preenchimento(
        driver=driver,
        Nome=row['First Name'],
        Sobrenome=row['Last Name'],   # agora funciona sem erro
        RoleCompany=row['Role in Company'],
        CompanyName=row['Company Name'],
        PhoneNumber=row['Phone Number'],
        endeco=row['Address'],
        EmailAddress=row['Email']
    )
    
