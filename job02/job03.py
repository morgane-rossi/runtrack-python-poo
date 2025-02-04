class Livre :
    # constructeur avec attributs privés
    def __init__(self, titre, auteur, nb_pages):
        self.set_titre(titre)
        self.set_auteur(auteur)
        self.set_nb_pages(nb_pages)
        self.__disponible = True

    # accesseurs
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nb_pages(self):
        return self.__nb_pages
    
    # mutateurs
    def set_titre(self, titre):
        self.__titre = titre
    
    def set_auteur(self, auteur):
        self.__auteur = auteur
    
    def set_nb_pages(self, nb_pages):
        if not (nb_pages > 0 and type(nb_pages) == 'int'):
            print("Le nombre de pages doit être un entier supérieur à zéro")
        else :
            self.__nb_pages = nb_pages

    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.verification():
            print("Le livre a bien été emprunté")
            self.__disponible = False
        else :
            print("Impossible d'emprunter le livre")
    
    def rendre(self):
        if not self.verification():
            print("Le livre a bien été rendu")
            self.__disponible = True
        else :
            print("Le livre a déjà été rendu")

livre = Livre("Poil de Carotte", "H Bazin", 225)
livre.emprunter()
livre.rendre()
livre.emprunter()
