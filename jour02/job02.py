class Livre :
    # constructeur avec attributs privés
    def __init__(self, titre, auteur, nb_pages):
        self.set_titre(titre)
        self.set_auteur(auteur)
        self.set_nb_pages(nb_pages)

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
        if not (nb_pages > 0 and isinstance(nb_pages, int)):
            print("Le nombre de pages doit être un entier supérieur à zéro")
        else :
            self.__nb_pages = nb_pages

livre = Livre("Poil de Carotte", "H Bazin", 225)
print(livre.get_nb_pages())
livre.set_nb_pages(12)
print(livre.get_nb_pages())