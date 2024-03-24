# coding: utf-8

import sqlite3
import subprocess
import string

# connecction a la base de donnée
connecte = sqlite3.connect('/home/anis/Secondstep/anisdatabase.db')
connected = connecte.cursor()

connected.execute('select * from dataBase ')
#transformer la base de donnée en tableau avec fetchall
table = connected.fetchall()
thread=0
# Fetching data from the 'Seuil' table
connected.execute('SELECT * FROM Seuil')
seuil_data = connected.fetchone()  # Assuming you only have one row in the 'Seuil' table, adjust if necessary


# boucle for pour parcourir toutes les informations de la table (base de donée) 
for info in table:

        #verifie si les consomation en memoire ou CPU ou ram ne sont pas depassé    
        if info[1] > seuil_data[0] or info[2] > seuil_data[1] or info[3] > seuil_data[2]  :
            #si la consomation est depaseé rendre la varible thread true
            thread=1
#si crise a été detcter execution du script d'envoie du mail 

if thread == 1 :
    subprocess.Popen("python3 sendMail.py", shell=True)

