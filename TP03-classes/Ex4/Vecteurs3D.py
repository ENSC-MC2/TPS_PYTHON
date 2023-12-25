from Vecteur2D import Vecteur2D

class Vecteurs3D(Vecteur2D):

    def __init__(self,x,y,z) :
        super().__init__(x,y)
        self.z = z


    def ToString(self):
        return f"{super().ToString()} and z : {self.Z}"

    def Equals(self, v3):
        return super().Equals(v3) and self.z == v3.z

    def Norme(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5