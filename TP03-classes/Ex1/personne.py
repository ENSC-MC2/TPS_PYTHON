class Personne():

    def __init__(self,taille,poids,age) :
        self.taille = taille
        self.poids = poids
        self.age = age

    def imc(self):
        return self.poids / (self.taille**2)
    
    def interpretation(self):
        res = self.imc()
        if res <= 18.5 :
            return "insuffisance pondérale"
        elif res >= 30 :
            return "obesite"