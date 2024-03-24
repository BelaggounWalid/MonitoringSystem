import os
#ouvrir le ficher "allusr.txt" qui contient tout les utilisateures dy system connectée ou non en mode lecture

file = open('allusr.txt', "r")

#parcourir la premiere ligne (le premier utilisateur)

actuelusers =file.readline()

#boucle while pour parcourir tout le fichier ( tout les utilisateures )

while actuelusers:

    #la librairie "os.system" permet d'executer des commandes internes du systeme 
    #recuperer la consomation de la memoire de chaque utilisateur a partir de son espace home la variable actueluser contien l'utilisateur

    os.system('du -sm /home/' + str(actuelusers))

    #incrementation qui nous permet de lire le contenu de tout le fichet(chaque utilisateur)

    actuelusers =file.readline()
    #fermeture du fichier
file.close()



