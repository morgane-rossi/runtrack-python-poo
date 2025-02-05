class Commande :

    def __init__(self, num_commande, status):
        self.set_num_commande(num_commande)
        self.__liste_plats_commandes = []
        self.__status = status
    
    # accesseurs
    def get_num_commande(self):
        return self.__num_commande
    
    def get_liste_plats_commandes(self):
        return self.__liste_plats_commandes

    def get_status(self):
        return self.__status

    # mutateurs
    def set_num_commande(self, num_commande):
        self.__num_commande = num_commande

    def set_liste_plats_commandes(self, liste_plats_commandes):
        self.__liste_plats_commandes = liste_plats_commandes

    def set_status(self, status):
        self.__status = status


    def ajouter_plat(self, plat):
        self.__liste_plats_commandes.append(plat)

    def annuler_commande(self):
        self.__liste_plats_commandes = []   
        self.__status = "annulée"
    

    def calculer_total(self):
        total = 0
        for plat in self.get_liste_plats_commandes():
            total += plat["prix"]
        return total


    # afficher une commande avec son total à payer
    def afficher_commande(self):
        print(f"Numéro de commande : {self.get_num_commande()}")
        for plat in self.get_liste_plats_commandes():
            print(f"{plat['nom']} - prix : {plat['prix']}")
        print(f"Total de la commande HT :  {self.calculer_total()}")
        print()
        print(f"Total TTC : {self.calculer_tva()}")

    # méthode permettant de calculer la TVA
    def calculer_tva(self):
        return self.calculer_total() * 1.19

commande = Commande(1, "en cours")
commande.ajouter_plat({
    "nom": "spaghetti bolognaise",
    "prix": 13.50
})

commande.ajouter_plat({
    "nom": "tiramisu",
    "prix": 6.50
})

#print(commande.calculer_total())
commande.afficher_commande()