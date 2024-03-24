#!/bin/bash
cd /home/anis/Firststep
./execute.sh
cd /home/anis/Secondstep
./execute2.sh
cd /home/anis/Thirdstep
./execute3.sh
cd /home/anis/Fourthstep
cp /home/anis/Thirdstep/line_chart.svg /home/anis/Fourthstep/static/line_chart.svg
cd /home/anis/Fourthstep
python3 webpage.py
python3 form.py

