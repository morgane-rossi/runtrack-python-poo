class Animal :

    def __init__(self):
        """
        Constructeur qui initialise âge à zéro
        et prénom à une chaîne de caractères vide
        """
        self.age = 0
        self.prenom = ""

    def afficherAge(self):
        print(f"L'age de l'animal {self.age} ans")

    def vieillir(self):
        self.age += 1

    def nommer(self, prenom):
        self.prenom = prenom
        print(f"L'animal se nomme {self.prenom}")

mon_chien = Animal()
mon_chien.afficherAge()
mon_chien.vieillir()
mon_chien.afficherAge()
mon_chien.nommer("Poki")