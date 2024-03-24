# -*- coding:utf-8 -*-

import sqlite3
import json
import time
import datetime, timedelta
import os
import shutil
import pytz
from datetime import datetime

#------------------------------------------------------ part 2 / stockage -------------------------------------------------------------------

# Define the timezone for Europe/Paris
paris_timezone = pytz.timezone('Europe/Paris')

#Ouverture et Récupération les premieres lignes du resulta de chaque sonde ( nom_user + cpu % + memoire Miga )

currentUser = open('/home/anis/Firststep/currentUsers.txt', "r")
cpuUsage = open('/home/anis/Firststep/cpu_usage.txt', "r")
memoryUsage = open('/home/anis/Firststep/memoire.txt', "r")
ramUsage = open('/home/anis/Firststep/ram_usage.txt', "r")
# recuperation des utilisateures connecté un par un
user =currentUser.readline()
user=user.rstrip(os.linesep)

# utilisation du cpu de l'utulisateur recuperer en ligne en dessu
cpu=cpuUsage.readline()
cpu=cpu.rstrip(os.linesep)
cpu=float(str(cpu).replace(",", "."))

# consomation de la meoire de l'utilisateur recuperer deux ligne avant

memory=memoryUsage.readline()
memory=memory.rstrip(os.linesep)

# consomation de la ram de l'utilisateur recuperer trois ligne avant

ram=ramUsage.readline()
ram=ram.rstrip(os.linesep)
ram=float(str(ram).replace(",", "."))
  

dateNow = datetime.now(paris_timezone)


#boucle WHILE pour suavgarder les infos recuperer depuis les sondes
# parcourir par rapport au fichier des users
while user:
        
        # recuperer la date de sauvgardage
        date = datetime.now(paris_timezone).strftime('%Y-%m-%d %H:%M:%S')

        # creation de  l'objet JSON
        objet_json = {'users':user,'cpu': cpu,'memory' :memory,'ram' :ram,'date':date,}

        # Codage l'objets JSON "json.dump"
        # envoyer les infos dans un ficher JSON (objet_json.JSON) avec json.dump() 
        with open('objet_json.json','w') as fichier:
                json.dump(objet_json,fichier)

        # incrémenter de la boucle pour recuperer les infos sur le rest des utilisateures

        user =currentUser.readline()
        user=user.rstrip(os.linesep)


        cpu=cpuUsage.readline()
        cpu=cpu.rstrip(os.linesep)
        cpu=str(cpu).replace(",", ".")

        memory=memoryUsage.readline()
        memory=memory.rstrip(os.linesep)

        ram=ramUsage.readline()
        ram=ram.rstrip(os.linesep)
        ram=str(ram).replace(",", ".")


       #------------------------------ inserstion des informations du fichier JSON dans la base de donnée---------------------


        # etablir une connexion a la base de données

        connecte = sqlite3.connect('anisdatabase.db')

        connecte.row_factory = sqlite3.Row

        connected = connecte.cursor()

        # vérifier si la base existe si non la base va etre creé


        # Récupération des info stocker dans le fichier JSON pour un utilisateur

        with open('objet_json.json') as objet_json:

                   #Décodage d’objets JSON

               objet_sql = json.load(objet_json)

        #  Insertion des infos dans la base de données

        connected.execute("INSERT INTO dataBase (users, cpu, memory, ram, date) VALUES (?, ?, ?, ?, ?)",(
                                        objet_sql['users'],

                                        objet_sql['cpu'],

                                        objet_sql['memory'],

                                        objet_sql['ram'],

                                        objet_sql['date'], ))
                

        #  enregistter les modifications faites sur la base de donnée

        connecte.commit()

        # Fermer la base

        connecte.close()


# Fermer tout les fichiers  

currentUser.close()

cpuUsage.close()

memoryUsage.close()

ramUsage.close()

# ----------------------------------------------------- fin du stockage ---------------------------------------------------------- 


# Sauvegarde de la base de données


