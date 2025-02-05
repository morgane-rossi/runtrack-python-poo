class Student :
    # constructeur avec attributs privés
    def __init__(self, nom, prenom, num_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__num_etudiant = num_etudiant
        self.__nb_credits = 0
        self.level = self.__student_eval()

    # accesseurs
    def get_nom(self):
        return self.__nom
    
    def get_prenom(self):
        return self.__prenom

    def get_num_etudiant(self):
        return self.__num_etudiant

    def get_nb_credits(self):
        return self.__nb_credits

    def add_credits(self, nb_credits):
        if nb_credits > 0 :
            print(f"{nb_credits} credits ont bien été ajoutés")
            self.__nb_credits += nb_credits
        else :
            print("Le nombre de crédits ne peut pas être inférieur ou égal à zéro")

    def __student_eval(self):
        if self.__nb_credits >= 90 :
            return "Excellent"
        elif self.__nb_credits >= 80 :
            return "Très bien"
        elif self.__nb_credits >= 70 :
            return "Bien"
        elif self.__nb_credits >= 60 :
            return "Passable"
        else :
            return "Insuffisant"

    def __str__(self):
        return f"Le nombre de credits de {self.get_prenom()} {self.get_nom()} est de {self.get_nb_credits()} points"

    def student_info(self):
        print(f"Nom = {self.get_nom()}")
        print(f"Prénom = {self.get_prenom()}")
        print(f"id = {self.get_num_etudiant()}")
        print(f"Niveau = {self.__student_eval()}")

john_doe = Student("Doe", "John", "145")
john_doe.add_credits(10)
john_doe.add_credits(8)
john_doe.add_credits(12)
print(john_doe)
john_doe.add_credits(40)
john_doe.student_info()