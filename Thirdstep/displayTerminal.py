# coding: utf-8
import sqlite3
import os
import colorama
import subprocess
from colorama import Fore, Back, Style


colorama.init(autoreset=True)
# connextion ala base de donnée
connecte = sqlite3.connect('/home/anis/Secondstep/anisdatabase.db')
connected = connecte.cursor()

#requette pour recupere tout les information de la base

connected.execute('select * from dataBase ')
#transformar en tableu a l'aide de la fonction fetchall()

table = connected.fetchall()

#parcourir le tableau

for info in table:
        #affichage en couleures des information dans le terminal
        print(Fore.WHITE +"----------------------------------------------------------------------------" , end="\n")
        subprocess.call(' echo "\033[0;34m Nom Compte \033[0;31m----------------: \033[0;32m {}"'.format(info[0]),shell=True)
        subprocess.call(' echo "\033[0;34m Utilisation de CPU % \033[0;31m------: \033[0;32m {}"'.format(info[1]),shell=True)
        subprocess.call(' echo "\033[0;34m Consomation de Memoire G\033[0;31m---: \033[0;32m {}"'.format(info[2]/1024),shell=True)
        subprocess.call(' echo "\033[0;34m Consomation de Ram kb \033[0;31m---------: \033[0;32m {}"'.format(info[3]),shell=True)
        subprocess.call(' echo "\033[0;34m Date de connexion \033[0;31m---------: \033[0;32m {}"'.format(info[4]),shell=True)
        print(Fore.WHITE +"----------------------------------------------------------------------------" , end="\n")
        print("\n")

        
       
connecte.commit()
connecte.close()

