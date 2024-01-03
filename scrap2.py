from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import json
import requests




SECURE_URL='https://core.jax-delivery.com/api/colis?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2NvcmUuamF4LWRlbGl2ZXJ5LmNvbS9hcGkvYXV0aC9sb2dpbiIsImlhdCI6MTcwNDIzMDIzMSwiZXhwIjoxNzA0Mzc0MjMxLCJuYmYiOjE3MDQyMzAyMzEsImp0aSI6InVyemcwNjRleFl2M1RQSTQiLCJzdWIiOiIyNzMiLCJwcnYiOiIyM2JkNWM4OTQ5ZjYwMGFkYjM5ZTcwMWM0MDA4NzJkYjdhNTk3NmY3In0.BuzcjXe6C_4CrB40ukKZ2sfdOffSbYyQzWwB4c_0phE&adresseLivraison=&cod=&code=&created_at=&depot=&is_echange=nonechange&description=&governorat=&nomContact=&referenceExterne=&statut_id=&tel=&paye=&client_id=&livre_par=&verse=&date_debut_enlev=&date_fin_enlev=&date_debut_livraison=&date_fin_livraison=&date_debut_retour=&date_fin_retour=&id=0&nbr=25&page='
 
URL = 'https://admin.jax-delivery.com/#'
LOGIN_ROUTE=('https://core.jax-delivery.com/api/auth/login')

HEADERS={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36','origin':URL,'Referer':URL+LOGIN_ROUTE}




login_payload={'email': "mohameddhiabensaad@gmail.com",' password': "192587"}

with requests.session() as s :
        s.post(LOGIN_ROUTE,data=login_payload)
        page = 531
        en_attente_count = 0 
        expi =0
        # while True :
        r = s.get(SECURE_URL + str(page))
        data = json.loads(r.text)["data"]
                
                # if not data:
                #     break  # No more data, exit the loop

        header = list(data[0].keys())
  
        index = [header.index(i) for i in ['created_by','status']]
                # print(index)

        with open("output3.csv", "a", newline="", encoding="utf-8") as csv_file:  # Use "a" to append to the file
            Lheader = ['Expéditeur','status']
            csv_writer = csv.DictWriter(csv_file, fieldnames=Lheader)
            if page ==1:
                 csv_writer.writeheader()  # Write header only for the first page
            for entry in data:
                l = list(entry.values())
                # status_value = l[index[1]][0]['libelle'] if l[index[1]] else ''  # Extract 'libelle' value from the list 
                # expediteur=l[index[0]]
                                # Check if 'libelle' is "en attente" and increment the count
                                # if status_value =="Reçu par l'expediteur":
                                #       csv_writer.writerow({'Expéditeur': l[index[0]], 'status': status_value})
                                #       expi+=1
            print(l)      
                
                # with open("output3.text", "w", newline="", encoding="utf-8") as file:
                #        file.write('pqge:'+str(page)+'\n')
                #        file.write('Total en attent:'+str(en_attente_count)+"\n")
                #        file.write('Total en expi:'+str(expi))
                # page -= 1
        
# print(expi,en_attente_count)