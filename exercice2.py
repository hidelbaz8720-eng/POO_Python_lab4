
from abc import ABC, abstractmethod
import math


# Classe abstraite Forme
class Forme(ABC):

    @abstractmethod
    def aire(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} - aire : {self.aire():.2f}"


# Classe Cercle
class Cercle(Forme):

    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return math.pi * self.rayon ** 2


# Classe Rectangle
class Rectangle(Forme):

    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur


# Classe Triangle
class Triangle(Forme):

    def __init__(self, base, hauteur):
        self.base = base
        self.hauteur = hauteur

    def aire(self):
        return 0.5 * self.base * self.hauteur


# Extension : classe Carre
class Carre(Rectangle):

    def __init__(self, cote):
        super().__init__(cote, cote)


# Programme principal
if __name__ == "__main__":

    formes = [
        Cercle(3),
        Rectangle(4, 5),
        Triangle(6, 2),
        Carre(4)
    ]

    for f in formes:
        print(f)
