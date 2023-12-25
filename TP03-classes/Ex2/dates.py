class dates():

    def __init__(self,jour,mois,annee):
        self.jour = jour
        self.mois = mois
        self.annee = annee

        if self.mois > 12 or self.mois < 1 :
            raise ValueError("Ce type des mois impossibles")
        elif self.jour > 31 or self.jour < 1 :
            raise ValueError("Ce type des jours impossibles")
        elif self.annee < 0 :
            raise ValueError("Ce type des annees impossibles")
        
    def _it_(self,d2):
        if self.annee < d2.annee :
            return True
        elif self.annee > d2.annee :
            return False
        else :
            if self.mois < d2.mois :
                return True
            elif self.mois > d2.mois :
                return False
            else :
                if self.jour < d2.jour :
                    return True
                else :
                    return False