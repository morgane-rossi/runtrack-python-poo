class Rectangle :
    # constructeur avec attributs privés
    def __init__(self, longueur, largeur):
        self.set_longueur(longueur)
        self.set_largeur(largeur)

    # accesseurs
    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur
    
    # mutateurs
    def set_longueur(self, longueur):
        self.__longueur = longueur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur


rectangle = Rectangle(10, 5)
rectangle.set_longueur(8)
rectangle.set_largeur(15)
print(f"Longueur du rectangle : {rectangle.get_longueur()}")
print(f"Largeur du rectangle : {rectangle.get_largeur()}")