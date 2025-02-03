from math import pi

class Cercle :

    def __init__(self, rayon):
        """
        Constructeur qui prend en paramètre
        le rayon du Cercle
        """        
        self.rayon = rayon
    
    def changerRayon(self, rayon):
        self.rayon = rayon

    def circonference(self):
        return 2 * pi * self.rayon

    def aire(self):
        return pi * self.rayon * self.rayon

    def diametre(self):
        return self.rayon * 2

    def afficherInfos(self):
        print("rayon du cercle : ", self.rayon, " - diamètre du cercle : ", self.diametre(), " - circonference du cercle : ", self.circonference(), " - aire du cercle : ", self.aire())

cercle1 = Cercle(4)
cercle1.afficherInfos()
cercle2 = Cercle(7)
cercle2.afficherInfos()