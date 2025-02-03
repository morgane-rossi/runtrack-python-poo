class Personnage :

    def __init__(self, x, y):
        """
        Constructeur qui prend en paramètre les coordonnées X et Y
        et initialise la position du Personnage
        sur le plateau du jeu
        = une matrice à deux dimensions.
        X coordonnée horizontale et Y coordonnée verticale.
        """
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def bas(self):
        self.y += 1

    def haut(self):
        self.y -= 1
    
    def position(self):
        """
        Renvoie les coordonnées du Personnage
        sous la forme d'un tuple (x, y)
        """
        return(self.x, self.y)

paladin = Personnage(3, 2)
print(paladin.position())
paladin.bas()
paladin.bas()
paladin.droite()
print(paladin.position())