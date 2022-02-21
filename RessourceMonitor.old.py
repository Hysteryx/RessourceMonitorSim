################
# Dépendances #
##############

from dependancies import File

##########
# code #
#######

def sheduleur(list, timeR):
    """Indiquer une liste (exemple à la fin) ainsi que un temps aloué au traitement de chaque ressources;\nExemple: \n\np1 = [ ["P1", 5], ["P2", 1], ["P3", 2]]\nsheduleur(p1,1)"""
    initial = File()
    end = File()
    for i in range(len(list)):
        initial.enfile(list[i])
    while not initial.estVide():
        calcul = initial.defile()
        if calcul[1] >= timeR: 
            calcul[1] = calcul[1] - timeR 
            initial.enfile(calcul)
            print(calcul)
        else: 
            print("['"+calcul[0] + "', 0]", end=f' : Finit après {timeR - calcul[1]} unité(s) de temps\n')
            calcul[1] = 0
            end.enfile(calcul)
    print('\n----- Etat des Processus -----\n')
    for i in range(end.taille()):
        print(end.defile(), end=" --> Términé\n")


##########
# Tests #
########
  
p1 = [ ["P1", 5], ["P2", 1], ["P3", 2]] 
sheduleur(p1,1)

