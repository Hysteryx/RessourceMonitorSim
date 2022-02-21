from time import sleep as sl

class File:
 
    def __init__(self):
        '''initialisation d'une file vide'''
        self.val=[]
 
    def estVide(self):
        '''renvoie True si la file est vide, False sinon'''
        return self.val==[]
    
    def enfile(self,x):
        '''Ajoute l’élément x au sommet de la file'''
        self.val.append(x)
    
    def defile(self):
        '''pour une file non vide :
        supprime et renvoie l’élément au sommet de la file'''
        assert not self.estVide(), "Pile vide !"
        return self.val.pop(0)
    
    def taille(self):
        '''renvoie le nombre d'éléments de la file'''
        return len(self.val)
 
    def tete(self):
        '''affiche la tete de la file'''
        assert not self.estVide()
        return self.val[0]
        
    def __str__(self):
        '''affiche la file sous forme de liste'''
        return str(self.val)
 
class Ressources:


    def __init__(self,name,tps) -> None:
        '''Process avec un nom et une valeur de temps d'exection'''
        self.name = name
        self.tps = tps 
        self.intialTps = tps #permet d'effectuer un suivis depuis le début 


    def calculPercent(self):
        """calcul le pourcentage de calcul effectué"""
        res = 0
        res = int(self.tps) / int(self.intialTps) * 100 
        return 100 - res 
    
    def newTps(self, newVal):
        '''Assigner un nouveau temps'''
        self.tps = newVal
        return newVal

    def timeR(self):
        '''renvoie le temps actuel'''
        return self.tps

    def newName(self, newName):
        '''Modifie le nom actuel du process'''
        self.name = newName
        return self.name

    def nameP(self):
        '''renvoie le nom actuel'''
        return self.name

    def __str__(self) -> str:
        return f"[{self.name}, {self.tps}]"


class Scheduleur:

    def __init__(self, tps) -> None:
        self.tmax = tps    #temps alloué à chaque processus max 
        self.file = File() #file des processus 

    def add(self, newProcess):
        """
        Ajoute des processus dans la file 
        """
        self.file.enfile(newProcess)

    def modifTps(self, newTps):
        """
        Modifie le temps alloué au traitement de chaque ressource 
        """
        self.tmax = newTps

    def run(self):
        """
        Simule l'éxecution des processus indiquée dans la classe directement (relié à self)
        
            - Pourcentage de traitement du processus 
            - Gestion des automatique du temps  
        """
        Initial = self.file
        TimePerRessource = self.tmax
        while not Initial.estVide():
            inCalcul = Initial.defile()
            if inCalcul.timeR() >= TimePerRessource:
                nt = inCalcul.timeR() - TimePerRessource
                inCalcul.newTps(nt)
                print(f'Ressource : [{inCalcul.nameP()}] calculée à {inCalcul.calculPercent()}% !')
                Initial.enfile(inCalcul)
            else: 
                inCalcul.newTps(0)
                print(f"[END-PROCESS] - La ressource '{inCalcul.nameP()}' à été calculée avec succès !")
            sl(int(TimePerRessource)/ 100)

    def affiche(self):  #pas de str car l'utilisation poserais pb 
        for i in range(self.file.taille()):
            prov = self.file.defile()
            print(prov,end=', ')
            self.file.enfile(prov)
        if self.file.taille() == 0:
            print("Aucun processus en file d'attente ")

    def clear(self):
        self.file = File()
        print('La file est désormais vide !')


"""
Utilisation 

test = Ressources('test',50)
a = scheduleur(5)
a.add(test)

a.run()
"""