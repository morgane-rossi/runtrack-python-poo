class Operation :

    def __init__(self):
        """
        Constructeur avec des valeurs par défaut
        """
        self.nombre1 = 3
        self.nombre2 = 42

op = Operation()
print(f"Le nombre1 est {op.nombre1}")
print(f"Le nombre2 est {op.nombre2}")