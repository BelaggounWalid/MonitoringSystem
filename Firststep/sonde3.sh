#!/bin/sh


#prcourir le fichier qui contient tout les utilisateures  connecté ou non  

for  user in $( cat allusr.txt);
do
        # faire la somme de la troisieme colone qui fait referance a la cosomation du CPU

	# la commande ps permet d'afficher les daetailles l'option -h c'est pour ne pas afficher le head l'option -x c'est pour afficher tout les terminal utiliser et l'option -U c'est pour specifier l'utilisateur sur le quele les information seront afficher

    ps hux -U ${user} | awk -v user=${user}  '{ sum += $3 } END { printf "%.2f\n" , sum ; }'
    

done



