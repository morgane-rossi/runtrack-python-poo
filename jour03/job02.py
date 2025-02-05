class CompteBancaire :

    # constucteur
    def __init__(self, num_compte, nom, prenom, decouvert):
        self.__num_compte = num_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = 0
        self.__decouvert = decouvert
    
    # accesseurs
    def get_num_compte(self):
        return self.__num_compte
    
    def get_nom(self):
        return self.__nom
    
    def get_prenom(self):
        return self.__prenom
    
    def get_solde(self):
        return self.__solde
    
    def get_decouvert(self):
        return self.__decouvert
    
    # mutateurs
    def set_num_compte(self, num_compte):
        self.__num_compte = num_compte
    
    def set_nom(self, nom):
        self.__nom = nom
    
    def set_prenom(self, prenom):
        self.__prenom = prenom
    
    def set_solde(self, solde):
        self.__solde = solde
    
    def set_decouvert(self, decouvert):
        self.__decouvert = decouvert
    

    def afficher_solde(self):
        # cette méthode affiche dans le terminal le solde du client.
        print(f"Solde du client : {self.get_solde()} euros")

    def afficher(self):
        print(f"Numéro de compte : {self.get_num_compte()}")
        print(f"Titulaire du compte : {self.get_prenom()} {self.get_nom()}")
        self.afficher_solde()

    # versement
    def versement(self, somme):
        self.__solde += somme

    # retrait
    def retrait(self, somme):   
        if somme > self.get_solde() and not self.get_decouvert():
            print("Montant trop élevé par rapport à votre solde bancaire, retrait impossible")
            return False
        else :
            self.__solde -= somme
            print(f"Nouveau solde : {self.get_solde()} euros")
            return True

    def agios(self):
        if self.get_solde() < 0 :
            self.__solde += (self.get_solde() / 10)

    def virement(self, other, somme):
        if self.retrait(somme):
            other.versement(somme)
            print(f"Le versement de la somme de {somme} euros a bien été effecuté")
        else:
            print("Versement impossible")


fauchay = CompteBancaire("1", "Martin", "Gertrude", True)
fauchay.versement(4)
fauchay.versement(12)
fauchay.retrait(412)
fauchay.afficher()
print("agios")
fauchay.agios()
fauchay.afficher_solde()
print()
# Elisabeth Fourmi donne de la thune
fourmi = CompteBancaire("2", "Fourmi", "Mauricette", True)
fourmi.versement(512)
fourmi.virement(fauchay, 435.6)
fauchay.afficher()
print()
fourmi.afficher()