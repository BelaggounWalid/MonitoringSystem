# Récupérer la liste de tous les utilisateurs du système
all_users=$(cut -d: -f1 /etc/passwd)

# Récupérer la liste des utilisateurs connectés
connected_users=$(who | cut -d' ' -f1 | sort -u)
echo "$all_users" >> allusr.txt
echo "$connected_users" >> allusr.txt

