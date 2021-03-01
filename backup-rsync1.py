# Python-Script
# Script-name: backup-rsync-01.py
# Autor: evttenorio
import os, subprocess

DIR="/home/usuario/meusarquivos" # DIRETÓRIO DE ORIGEM
DIRB="/home/usuario/backupmeusarquivos" # DIRETÓRIO DE BACKUP
LIXEIRA="/home/usuario/recoverbackupfiles"
x=str(subprocess.check_output(['date','+%B/%d-%m-%Y--%Hh']))
DATA = x.replace("'","").replace("b","").replace("\\n","")
MIRROR = (LIXEIRA+"/"+DATA)

def main():
    #print ('\x1b[1;36m RSYNC [verbose-mode]\x1b[0m')
    print ('\U00002796' * 40)
    rsync = ('rsync --delete --backup-dir='+MIRROR+' -raAXtuv '+DIR+' '+DIRB)
    os.system(rsync)

if __name__ == "__main__":
    main()
