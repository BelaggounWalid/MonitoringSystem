#!/bin/bash
cd /home/anis/Firststep
rm currentUsers.txt
./sonde1.sh > currentUsers.txt
./sondeallusers.sh
python3 sonde2M.py | cut -f1 -d"/"  > memoire.txt
./sonde3.sh | cut -f1 -d" " > cpu_usage.txt
./sonde4.sh | cut -f2 -d" " > ram_usage.txt


