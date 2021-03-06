from random import randint #fonction auto
from time import sleep as sp #rendre l'affichache mieux 
from dependancies import Ressources #simulation de la ressource 
from dependancies import Scheduleur #simulation du calcul des ressources

def menu_Start():
    """
    Organise et facilite l'utilisation des classes (dans dependancies)
    """
    isRunning = True 
    sheduleur = Scheduleur(5)
    while isRunning:
        terminal_rrp = input("\n>>>")
        if terminal_rrp == 'quit': #quitte la boucle 
            isRunning = False
        elif terminal_rrp == 'modifTime': #modifie le temps maximal alloué à chaque ressource 
            NewTime = input("Entrez le nouvel intervalle de temps :\n>>>")  
            sheduleur.modifTps(NewTime)
            print(f"Le temps d'execution maximale par ressources est définis sur : {NewTime}")
        elif terminal_rrp == 'add': #ajoute un nouveau processus 
            NewRessourceName = input('Rentrez du nouveau processus :\n>>>')
            NewTimeForRessource = int(input('Rentez le temps nécéssaire à son éxécution :\n>>>'))
            NewRessource = Ressources(NewRessourceName,NewTimeForRessource)
            sheduleur.add(NewRessource)
            print('La ressource à été ajoutée avec succès !\n\n')
        elif terminal_rrp == 'run': #simule le traitement des processus en file 
            print("----- Lancement de l'éxécution -----\n")
            sheduleur.run()
            print("\n----- Execution términée -----\n")
        elif terminal_rrp == "affiche": #affiche les processus en file 
            sheduleur.affiche()
        elif terminal_rrp == "auto": #génére 20 processus automatiquement avec un nom aléatoire 
            print('Genération aléatoire de processus !')
            lettres = "AZERTYUIOPQSDFGHJKLMWXCVBN0123456789"
            for i in range(20):
                name = ""
                for i in range(5):
                    name += lettres[randint(0,len(lettres)-1)]
                print(f"Processus [{name}] ajouté")
                sheduleur.add(Ressources(name,randint(0,100)))
                sp(0.05)
            print('20 processus ajoutés, faite : run pour les executer!\n')
        elif terminal_rrp == "clear": #vide la file d'attente
            sheduleur.clear()
        elif terminal_rrp == "help": #affiche les commandes les plus courantes 
            print("\n ----- HELP -----\n\n- quit --> ferme le programme\n- add --> ajoute un processus\n- run --> simule le calcul des processus indiquez précédement\n- modifTime --> modifie le temps maximale d'éxécution de chaque ressource")

menu_Start()
