#!/bin/bash

#creo una cartella in cui viene eseguito l'esercizio di Python
mkdir esameMurro

#copio il file
cp esameCM.py esameCM_c.py
	#cp esameClaudiaMurro.sh esameClaudiaMurro_c.sh

#sposto il file copiato nella cartella
mv esameCM_c.py esameMurro
	#mv esameClaudiaMurro_c.sh esameMurro

#entro nella cartella
cd esameMurro

#----------------------------------------------------------
#scarico dati
wget https://raw.githubusercontent.com/MilenaValentini/TRM_Dati/main/Nemo_6670.dat
if [ $? -eq 0 ]
then
echo OK
else
echo FAULT
fi
ls -l Nemo_6670.dat
export DATA_FILE_PATH=`pwd`/Nemo_6670.dat

#scrivo su terminale il path da dare in input per l'esercizio in Python
echo $DATA_FILE_PATH

#assegno i permessi
chmod +rwx $DATA_FILE_PATH 

#inizia esercizio di Python
python3 esameCM_c.py
