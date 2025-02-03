class Point :

    def __init__(self, x, y):
        """
        Constructeur qui prend en paramètre les coordonnées du Point
        x coordonnée horizontale
        y coordonnée verticale
        """        
        self.x = x
        self.y = y
    
    def afficherLesPoints(self) :
        """
        Méthode qui affiche les coordonnées d'un Point
        """
       
        print("coordonnées : (",self.x," : ",self.y,")")

    def afficherX(self):
        print(self.x)
    
    def afficherY(self):
        print(self.y)

    # Setters du Point
    def changerX(self, x):
        self.x = x

    def changerY(self, y):
        self.y = y

pointA = Point(5, -3)
pointA.afficherLesPoints()