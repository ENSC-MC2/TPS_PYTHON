class Personne():
    
    def __init__(self,nom,prenom) :
        self.nom = nom
        self.prenom = prenom
    
    def fullname(self):
        return f"Hi, my name is : {self.nom} {self.prenom}"