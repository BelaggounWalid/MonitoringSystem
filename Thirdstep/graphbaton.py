# -*- coding: utf-8 -*-
import sqlite3
import pygal
from pygal.style import Style




# connecter a la base de donnees 
connecte = sqlite3.connect('/home/anis/Secondstep/anisdatabase.db')
connected = connecte.cursor() 


# recuperer toutes les information de base 
connected.execute('select * from dataBase ')

table = connected.fetchall()


# Initialisation  des listes 
user=[]
cpu=[]
memory=[]
ram=[]
date=[]

# boucle for pour parcourir toutes les infos dans la table  
for info in table:
        
        # Ajouter les infos de chaque ligne à a propre liste 
        user.append(info[0])
        cpu.append(info[1])
        memory.append(info[2])
        ram.append(info[3]/1024)
        date.append(info[4])

connecte.commit()
connecte.close()


# Diagramme en baton 

graph = pygal.Bar(x_label_rotation=20)
graph.x_labels = map(str, user)  
# representation des trois bars cpu % et memoire en giga et cpu en %
graph.add('Cpu %',cpu )
graph.add('Memoire en Giga', memory)
graph.add('Ram MB', ram)
# Renvoie le svg sous forme d'octets
#graph.render_to_png('graphe.png')
graph.render_to_file('line_chartbaton.svg')
graph.render()




