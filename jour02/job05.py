class Voiture :

    # constructeur avec attributs privés
    def __init__(self, marque, modele, annee, kilometrage):
        self.set_marque(marque)
        self.set_modele(modele)
        self.set_annee(annee)
        self.set_kilometrage(kilometrage)
        self.__en_marche = False
        self.__reservoir = 50
    
    # accesseurs
    def get_marque(self):
        return self.__marque
    
    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee
    
    def get_kilometrage(self):
        return self.__kilometrage
    
    def get_en_marche(self):
        return self.__en_marche


    # mutateurs
    def set_marque(self, marque):
        self.__marque = marque
    
    def set_modele(self, modele):
        self.__modele = modele
    
    def set_annee(self, annee):
        self.__annee = annee
    
    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage
    
    def set_en_marche(self, en_marche):
        self.__en_marche = en_marche

    def demarrer(self):
        if (self.__verifier_plein > 5):
            self.__en_marche = True
        else :
            print("La voiture n'a pas assez d'essence pour démarrer")
    
    def arreter(self):
        self.__en_marche = False
    
    def __verifier_plein(self):
        return self.__reservoir