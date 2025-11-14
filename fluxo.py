import pandas as pd
from Preenchimento import Preenchimento
import time

# Carrega Excel
df = pd.read_excel('challenge.xlsx')

# Remove espaços extras nos nomes das colunas
df.columns = df.columns.str.strip()

print("Colunas detectadas:", df.columns.tolist())

# Loop linha por linha
for index, row in df.iterrows():

    print(f"Preenchendo linha {index+1}/{len(df)}...")

    Preenchimento(
        Nome=row['First Name'],
        Sobrenome=row['Last Name'],   # agora funciona sem erro
        RoleCompany=row['Role in Company'],
        CompanyName=row['Company Name'],
        PhoneNumber=row['Phone Number'],
        endeco=row['Address'],
        EmailAddress=row['Email']
    )
    
