class Produit :

    def __init__(self, nom, prixHT, TVA):
        """
        Constructeur qui prend en paramètre
        le nom, le prix HT et la TVA
        d'un Produit
        La TVA doit être un pourcentage
        """          
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def __str__(self):
        """
        Méthode qui renvoie de façon explicite et lisible
        les propriétés :
        nom, prix et TVA
        ainsi que le prix TTC calculé
        """
        return "nom : " + str(self.get_nom()) + " - prix HT : " + str(self.get_prixHT()) + " - TVA : " + str(self.get_TVA()) + " - prix TTC : " +  str(self.CalculerPrixTTC())

######################################################
    # Méthodes permettant de modifier  le nom du produit et son prix.
    def set_nom(self, nom):
        self.nom = nom

    def set_prix(self, prixHT):
        self.prixHT = prixHT
######################################################


######################################################
    # Méthodes permettant de retourner chaque information du produit
    def get_nom(self):
        return self.nom

    def get_prixHT(self):
        return self.prixHT

    def get_TVA(self):
        return self.TVA
######################################################


    def afficher(self):
        return self.__str__()

    # TVA est un pourcentage
    def CalculerPrixTTC(self):
        prixTTC = self.prixHT * (1 + (self.TVA / 100))
        return f"{prixTTC:2f}"


PQ = Produit("PQ", 13, 19)
print(f"Prix TTC d'un rouleau de papier toilette : {PQ.CalculerPrixTTC()}")
print(PQ.afficher())
print()
SNSV = Produit("Ordinateur portable", 1850, 19)
print(f"prix TTC d'un ordinateur portable : {SNSV.CalculerPrixTTC()}")
print(SNSV.afficher())
print()
coquillettes = Produit("Coquillettes", 0.99, 5.5)
print(f"Prix TTC d'1 kilo de pâtes : {coquillettes.CalculerPrixTTC()}")
print(coquillettes.afficher())