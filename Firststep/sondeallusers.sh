#!/bin/bash

#recuperer toute les  1 ére et 7 éme colnes du fichie /etc/passwd qui contient "bin/bash" qui contient dans la premiere colone les utilisateur de tout le system et rediriger ver un ficher(flux de redirection)

cut /etc/passwd -f1,7 -d':' | grep -i 'bin/bash' > allUsers.txt

#contabiliser le nombre d'utilisateures recuperé

nmb=`cat allUsers.txt | grep -i 'bin/bash' | wc -l`

#soustraire 1 vu que le "root" sera tousjours le premier

nm=$((nmb-1))

#exclure le "root" de la liste des utilisateures et rediriger le resultas final dans un fichier

cat allUsers.txt | cut -f1 -d':' | head -n $nmb |tail -$nm > allusr.txt

