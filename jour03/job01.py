class Ville :
    def __init__(self, nom, nb_habitants):
        self.__nom = nom
        self.__nb_habitants = nb_habitants

    def __str__(self):
        return f"Population de la ville de {self.get_nom()} : {self.get_nb_habitants()} habitants"
    
    def get_nom(self):
        return self.__nom
    
    def get_nb_habitants(self):
        return self.__nb_habitants
    
    def set_nom(self, nom):
        self.__nom = nom
    
    def set_nb_habitants(self, nb_habitants):
        self.__nb_habitants = nb_habitants


class Personne :
    def __init__(self, nom, age, ville :Ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.ajouterPopulation(ville)

    def get_nom(self):
        return self.__nom
    
    def get_age(self):
        return self.__age
    
    def get_Ville(self):
        return self.__ville
    
    def set_nom(self, nom):
        self.__nom = nom
    
    def set_age(self, age):
        self.__age = age
    
    def set_Ville(self, ville: Ville):
        self.__ville = ville
    
    def ajouterPopulation(self, ville: Ville):
        self.__ville.set_nb_habitants(Ville.get_nb_habitants() + 1)
        


paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)


print(paris)
print(marseille)
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)
print(f"Mise a jour de la population de la ville de {paris.get_nom()} {paris.get_nb_habitants()} habitants")
print(f"Mise a jour de la population de la ville de {marseille.get_nom()} {marseille.get_nb_habitants()} habitants")