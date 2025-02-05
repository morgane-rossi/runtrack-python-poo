class Tache :

    def __init__(self, titre, description):
        self.titre = titre
        self.description = description
        self.status = "a_faire"
 
class ListeDeTaches :

    # constructeur sans arguments
    def __init__(self):
        self.taches = []

    def ajouter_tache(self, tache):
        self.taches.append(tache)
    
    def supprimer_tache(self, tache):
        self.taches.remove(tache)
    
    def marquer_comme_finie(self, tache):
        for i in range(len(self.taches)):
            if tache.titre == self.taches[i].titre and tache.description == self.taches[i].description :
                self.taches[i].status = "finie"

    def afficher_liste(self):
        for tache in self.taches :
            print(f"{tache.titre} : {tache.description} - status : {tache.status}")
    
    def filter_liste(self, status):
        resultat = ListeDeTaches()
        for tache in self.taches :
            if tache.status == status :
                resultat.ajouter_tache(tache)
        return resultat

maliste = ListeDeTaches()
un = Tache("bubule", "nourrir le poisson rouge")
maliste.ajouter_tache(un)
deux = Tache("esclave", "embaucher un stagiaire")
maliste.ajouter_tache(deux)
trois = Tache("loyer", "payer le loyer")
maliste.ajouter_tache(trois)

maliste.supprimer_tache(deux)

quatre = Tache("puyo", "sortir le chien")
maliste.ajouter_tache(quatre)

# changer le statut d’une tâche
maliste.marquer_comme_finie(un)
maliste.afficher_liste()
print()
print("liste des tâches qui restent à faire")
reste_a_faire = maliste.filter_liste("a_faire")
reste_a_faire.afficher_liste()