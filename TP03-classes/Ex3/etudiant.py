from Personne import Personne

class etudiant(Personne):

    def __init__(self,nom,prenom,notes):
        super().__init__(nom,prenom)
        self.notes = notes
    
    def ajouteNote(self,note):
        self.notes.append(note)