class Operation :

    def __init__(self):
        """
        Constructeur avec des valeurs par défaut
        """
        self.nombre1 = 3
        self.nombre2 = 42

    def addition(self) :
        """
        Additionne “nombre1” et “nombre2” et affiche en console le résultat
        """
        somme = self.nombre1 + self.nombre2
        print(f"{self.nombre1} + {self.nombre2} = {somme}")

op = Operation()
op.addition()
