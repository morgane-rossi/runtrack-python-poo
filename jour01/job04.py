class Personne :

    def __init__(self, prenom, nom) :
        """
        Constructeur qui prend en paramètre le prénom et le nom
        de la Personne
        """
        self.prenom = prenom
        self.nom = nom

    def sePresenter(self):
        """
        Méthode qui renvoie le nom et le prénom
        de la personne
        """
        return f"Je suis {self.prenom} {self.nom}"


perso1 = Personne("Aerith", "Gainsborough")
print(perso1.sePresenter())

perso2 = Personne("Barret", "Wallace")
print(perso2.sePresenter())

perso3 = Personne("Cid", "Highwind")
print(perso3.sePresenter())