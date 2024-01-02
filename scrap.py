from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import json
import requests




SECURE_URL='https://core.jax-delivery.com/api/clients?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2NvcmUuamF4LWRlbGl2ZXJ5LmNvbS9hcGkvYXV0aC9sb2dpbiIsImlhdCI6MTcwNDIwNTI1MSwiZXhwIjoxNzA0MzQ5MjUxLCJuYmYiOjE3MDQyMDUyNTEsImp0aSI6IlVsUmgwaXp3QTJVVG1QQzciLCJzdWIiOiIyNzMiLCJwcnYiOiIyM2JkNWM4OTQ5ZjYwMGFkYjM5ZTcwMWM0MDA4NzJkYjdhNTk3NmY3In0.gncykAqwnvvy_lIqeRleTXk1llwQwsX48wFny6FGGpM&prenom=&name=&email=&tel=&actif=0&adresse=&civilite=&matriculeFiscale=&governorats=&delegation=&created_at=&id=0&nbr=25&page=1'
 
URL = 'https://admin.jax-delivery.com/#'
LOGIN_ROUTE=('https://core.jax-delivery.com/api/auth/login')

HEADERS={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36','origin':URL,'Referer':URL+LOGIN_ROUTE}




login_payload={'email': "mohameddhiabensaad@gmail.com",' password': "192587"}

# login_req= requests.post(LOGIN_ROUTE,data=login_payload)

# print(login_req)

# resp= requests.get(SECURE_URL)

with requests.session() as s :
    s.post(LOGIN_ROUTE,data=login_payload)
    r=s.get(SECURE_URL)
    # soup=BeautifulSoup(r.text)
    print(r.text)
    data = json.loads(r.text)["data"]

    with open("output.csv", "w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        
        # Write header
        header = data[0].keys()
        csv_writer.writerow(header)

        # Write data
        for entry in data:
            csv_writer.writerow(entry.values())