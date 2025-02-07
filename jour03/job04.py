class Joueur :
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.nb_buts = 0
        self.nb_passes = 0
        self.cart_jaunes = 0
        self.cart_rouges = 0

    def marquer_but(self):
        self.nb_buts += 1

    def passe_decisive(self):
        self.nb_passes += 1

    def rec_cart_jaune(self):
        self.cart_jaunes += 1

    def rec_cart_rouge(self):
        self.cart_rouges += 1

    def afficher_stats(self):
        print(f"Statistiques du joueur : {self.nom}")
        print(f"Numéro : {self.numero} - position : {self.position}")
        print(f"Position : {self.position}")
        print(f"Nombre de buts marqués : {self.nb_buts}")
        print(f"Nombre de passes : {self.nb_passes}")
        print(f"Nombre de cartons jaunes : {self.cart_jaunes}")
        print(f"Nombre de cartons rouges : {self.cart_rouges}")


class Equipe :
    
    def __init__(self, nom):
        self.nom = nom
        self.liste_joueurs = []

    def ajouter_joueur(self, joueur: Joueur):
        self.liste_joueurs.append(joueur)

    def afficher_stats_joueurs(self):
        for joueur in self.liste_joueurs:
            joueur.afficher_stats()
            print()

    def mettre_a_jour_stats_joueur(self, joueur: Joueur):
        pass

loufoques = Equipe("Les joyeux loufoques")

#Créez plusieurs joueurs avec les paramètres de votre choix 
# et ajoutez-les aux équipes.
 # Présenter l’ensemble des joueurs de chaque équipe.

poussin = Joueur("Toshiki Inugai", "1", "attaquant")
loufoques.ajouter_joueur(poussin)
zidane = Joueur("Zidane Zinedine", "10", "milieu")
loufoques.ajouter_joueur(zidane)
barthez = Joueur("Barthez Fabien", "2", "goal")
loufoques.ajouter_joueur(barthez)
domond = Joueur("Domond Chelsea", "19", "attaquant")
loufoques.ajouter_joueur(domond)
blanchard = Joueur("Blanchard Ninon", "15", "defenseur")
loufoques.ajouter_joueur(blanchard)
print(f"Équipe {loufoques.nom} avant le début du match")
print("Composition de notre équipe de choc :")
for joueur in loufoques.liste_joueurs :
    print(joueur.nom)

print("Mon cher Jean-Mimi le match commence")
print("Tout à fait Thierry !")
print()
poussin.marquer_but()
poussin.marquer_but()
poussin.marquer_but()
poussin.marquer_but()
poussin.marquer_but()
zidane.rec_cart_jaune()
zidane.rec_cart_jaune()
zidane.rec_cart_jaune()
zidane.rec_cart_rouge()
zidane.rec_cart_rouge()
zidane.rec_cart_rouge()
zidane.rec_cart_rouge()
zidane.rec_cart_rouge()
domond.passe_decisive()
domond.passe_decisive()
domond.passe_decisive()
domond.passe_decisive()
domond.passe_decisive()
domond.passe_decisive()
domond.passe_decisive()
domond.passe_decisive()
domond.marquer_but()
domond.marquer_but()
domond.marquer_but()
domond.rec_cart_jaune()
domond.rec_cart_jaune()
domond.rec_cart_rouge()

# Et afficher à nouveau les statistiques des joueurs
loufoques.afficher_stats_joueurs()