# MonitoringSystem
Ce dépôt contient un projet de système de surveillance utilisant Python, Bash, SQLite, et sera de préférence hébergé sur un serveur de flask sur Linux. Vous pouvez également utiliser Apache.

# Projet de surveillance système

Ce projet vise à développer un système de surveillance des ressources système telles que le CPU, la mémoire et le stockage. Il utilise Flask comme framework web pour afficher les données collectées.

## Fonctionnalités

- Surveillance en temps réel du CPU, de la mémoire et du stockage.
- Affichage des alertes en cas de seuils dépassés.
- Interface utilisateur conviviale pour la visualisation des données.
- Possibilité de personnaliser les seuils de déclenchement des alertes
- fait un web scraping (parsing) du site cert alert .

## Installation

1. Cloner le dépôt GitHub sur votre machine locale :

   ```bash
   git clone https://github.com/BelaggounWalid/MonitoringSystem.git  

Installer les dépendances Python :
pip install -r requirements.txt

2. Modifier les chemins des sondes et fichiers .sh surtout en fonction de l'emplacement des scripts téléchargés.

3. Lancer l'application Flask : python3 webpage.py

4. Accéder à l'application dans votre navigateur en ouvrant l'URL : http://localhost:5000

5. faites attention de faire la redirection des ports si vous utiliser une machine virtuelle 


# Collecte d'Informations

La première étape consiste à recueillir des informations, telles que les utilisateurs connectés, l'utilisation du CPU et de la RAM, ainsi que l'espace disque utilisé. Il existe deux façons de procéder : soit en exécutant chaque sonde pour récupérer une information particulière, soit en exécutant la sonde (execute.sh) pour récupérer toutes les informations en une seule fois. Ces informations seront stockées dans des fichiers. Les scripts se trouvent dans un dossier nommé "Firststep".

# I.a. Récupération des Utilisateurs Connectés :
Ce script est écrit en Bash.

Script : sonde1.sh
Résultat du script : currentUsers.txt
I.b Récupération de l'Utilisation de la Mémoire (HDD) :
Ces sondes sont écrites en Python et en Bash.

Script : sondeallusers.sh (pour récupérer tous les utilisateurs, y compris ceux non connectés)
Résultat du script : allusr.txt
Script : sonde2M.py
Résultat du script : memoire.txt
I.c Récupération de l'Utilisation du CPU et de la RAM :
Ces sondes sont écrites en Bash.

Script : sonde3.sh (pour l'utilisation du CPU)
Résultat du script : cpu_usage.txt
Script : sonde4.sh (pour l'utilisation de la RAM)
Résultat du script : ram_usage.txt
En exécutant le script execute.sh, toutes les informations sont récupérées en une seule fois dans les fichiers mentionnés ci-dessus.

Librairies Tierces Utilisées :
os,shutil

# Archivage et Nettoyage :

Pour stocker les données, nous utilisons une base de données  anisdatabase.db où toutes les informations récupérées dans la partie 1 sont stockées. Les scripts se trouvent dans un dossier nommé "Secondstep".

II.b Un fichier JSON est utilisé pour transformer les objets complets et les stocker dans la table de la base de données. La base de données contient une table avec 5 champs : [‘users’, ’cpu’, ’memoire’, ’ram’, ‘date’].

II.c Nous récupérons les données de la première partie et les transformons en objet JSON.

II.d Pour supprimer les informations obsolètes, nous avons écrit un script Python. 

III.e pour le parseur web il est code dans le fichier parseur.py il recupere la derniere cert  alerte dans le site  https://www.cert.ssi.gouv.fr et la stoke dans la table cert-alert qui contient 4 champs (date,referecne,title,status) de la base de données anisdatabase.db .
 
IV.f Un script Bash nommé execute2.sh a été créé pour automatiser la partie deux, permettant de remplir la base de données et de supprimer les informations obsolètes et fait le parsing du site   https://www.cert.ssi.gouv.fr.  pour la suppression on met une table Seuil qui contient un champ temps_limite qui nous permet de configurer le temps limite pour supprimer la donnée
 et aussi y'a des script buckup.py qui va faire le sauvegarde de la base de donne au moment d'inserion .

Librairies Tierces Utilisées :
sqlite3, json, time, datetime, os,pytz,beautifulsoup4,requests .

# Affichage et Alertes :
tous les fichier de cette patie sont dans le dossier Thirdstep. et on a un fichier execute3.sh qui execue tous les code de cette partie

Un script de détection de crise (crisedetecion.py )a été développé pour détecter les dépassements d'utilisation de la mémoire, du CPU ou de la RAM. Un e-mail sera envoyé à l'administrateur en cas de menace détectée (sendMail.py qui utilise le protcole smtp en utilisant le serveur de la fac smtpz.univ-avignon.fr ). ce script utilise comme reference les données qui se trouve dans la table Seuil .


Un script de dgeneration de graph  (graph.py )a été développé pour generer des graphs  d'utilisation de la mémoire, du CPU et de la RAM. 
 
Librairies Tierces Utilisées :

pygal,smtplib,MIMEText,MIMEMultipart

#  Interface Web :

Pour cette partie, une page web HTML a été créée pour afficher les dereniere cert alertes et mettre un lien pour rediriger le user vers l 'alerte dans le site  https://www.cert.ssi.gouv.fr. et cette page  affiche aussi  les informations de cpu,ram ,user et memoire sous forme de graphiques colorés. Les données du graphique sont actualisées à chaque changement d'information en utilisant un script Python webpage.py .

on a ajouté un script form.py qui permet de generer un formulaire qui coniteint les donnes de la tables Seuil ce qui permettre aux utilisateurs de changer les valeurs limites de la table Seuil 

Librairies Tierces Utilisées :
Flask. 

en fin pour automatiser tous ce projet il y'a  un fichier finalexecute qui execute chaque execute.sh de chaque partie et aussi les applications flasks .
on le met dans un crontab pour que ca soit automatique .en choisissant un intervale de temsp precis .
 
 explication des bebliotheques utilisées:
1. Requests : Une bibliothèque HTTP pour effectuer des requêtes HTTP dans Python.
2. BeautifulSoup : Une bibliothèque pour analyser des documents HTML et extraire des données.
3. SQLite3 : Un module intégré à Python pour travailler avec des bases de données SQLite.
4. Datetime : Un module intégré à Python pour manipuler des dates et heures.
5. Locale : Un module intégré à Python pour effectuer des opérations basées sur la localisation.
6. Pytz : Une bibliothèque pour manipuler des fuseaux horaires dans Python.
7. Colorama : Une bibliothèque pour ajouter des couleurs et des styles au texte dans la console.
8 .Subprocess : Un module intégré à Python pour exécuter des sous-processus.
9. pygal : Une bibliothèque de génération de graphiques en Python.
10. smtplib : Un module intégré à Python pour envoyer des e-mails via SMTP.
11. Email.mime : Un module intégré à Python pour la création de messages MIME pour l'envoi d'e-mails.
12. ask : Un framework web léger pour Python, utilisé pour créer l'interface utilisateur et gérer les requêtes HTTP.