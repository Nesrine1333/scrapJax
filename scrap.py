from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import json
import requests




SECURE_URL='https://core.jax-delivery.com/api/clients?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2NvcmUuamF4LWRlbGl2ZXJ5LmNvbS9hcGkvYXV0aC9sb2dpbiIsImlhdCI6MTcwNDIzMDIzMSwiZXhwIjoxNzA0Mzc0MjMxLCJuYmYiOjE3MDQyMzAyMzEsImp0aSI6InVyemcwNjRleFl2M1RQSTQiLCJzdWIiOiIyNzMiLCJwcnYiOiIyM2JkNWM4OTQ5ZjYwMGFkYjM5ZTcwMWM0MDA4NzJkYjdhNTk3NmY3In0.BuzcjXe6C_4CrB40ukKZ2sfdOffSbYyQzWwB4c_0phE&prenom=&name=&email=&tel=&actif=0&adresse=&civilite=&matriculeFiscale=&governorats=&delegation=&created_at=&id=0&nbr=25&page='
 
URL = 'https://admin.jax-delivery.com/#'
LOGIN_ROUTE=('https://core.jax-delivery.com/api/auth/login')

HEADERS={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36','origin':URL,'Referer':URL+LOGIN_ROUTE}




login_payload={'email': "mohameddhiabensaad@gmail.com",' password': "192587"}

# login_req= requests.post(LOGIN_ROUTE,data=login_payload)

# print(login_req)

# resp= requests.get(SECURE_URL)

with requests.session() as s :
    s.post(LOGIN_ROUTE,data=login_payload)
    page = 1
    while True:
        r = s.get(SECURE_URL + str(page))
        data = json.loads(r.text)["data"]
        
        if not data:
            break  # No more data, exit the loop

        header = list(data[0].keys())
        index = [header.index(i) for i in ['code', 'prenom', 'matriculeFiscale', 'frais_liv', 'frais_retour']]
        

        with open("output.csv", "a", newline="", encoding="utf-8") as csv_file:  # Use "a" to append to the file
            Lheader = ['code', 'prenom', 'matriculeFiscale', 'frais_liv', 'frais_retour']
            csv_writer = csv.DictWriter(csv_file, fieldnames=Lheader)
            if page ==1:
                csv_writer.writeheader()  # Write header only for the first page
            for entry in data:
                l = list(entry.values())
                csv_writer.writerow({'code': l[index[0]], 'prenom': l[index[1]], 'matriculeFiscale': l[index[2]],
                                     'frais_liv': l[index[3]], 'frais_retour': l[index[4]]})
        page += 1
        