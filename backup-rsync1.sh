#!/bin/bash
# script-name: backup-rsync-01.sh
# autor: evttenorio

DIR=/home/usuario/meusarquivos # DIRETÓRIO DE ORIGEM
DIRB=/home/usuario/backupmeusarquivos # DIRETÓRIO DE BACKUP
LIXEIRA=/home/usuario/recoverbackupfiles
DATA=`date +%B/%d-%m-%Y--%Hh`

#echo $'\e[1;36m\U1F504 RSYNC [verbose-mode]\e[0m'
rsync --delete --backup-dir="$LIXEIRA/$DATA" -raAXtuv $DIR $DIR
