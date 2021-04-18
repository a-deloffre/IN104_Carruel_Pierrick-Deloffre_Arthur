
class Rectangle:
    
    def __init__(self,a,b):
        self.longueur, self.largeur = a , b
    def perimetre(self):
        return 2 * (self.longueur + self.largeur)
    def aire(self):
        return self.longueur * self.largeur
    def is_square(self):
        return self.longueur == self.largeur

fig = Rectangle(3,8)
print( "Le périmétre est :" , fig.perimetre() )
print( "L'aire est :" , fig.aire() )

if fig.is_square():
    print( "C'est un carré" )
else:
    print("Ce n'est pas un carré")