class Vecteur2D():

    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def ToString(self):
        return f"Cordonne sont : ({self.x},{self.y})"

    # ou bien
    # def __str__(self):
    #     return f"Cordonne sont : ({self.x},{self.y})"
    
    def Equals(self, v2):
        return self.x == v2.x and self.y == v2.y
    
    def Norme(self):
        return (self.x**2 + self.y**2)**0.5