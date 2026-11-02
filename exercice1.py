
# Classe mère Animal
class Animal:

    def parler(self):
        raise NotImplementedError(
            "Cette méthode doit être redéfinie"
        )


# Classe Chien
class Chien(Animal):

    def parler(self):
        return "Ouaf !"


# Classe Chat
class Chat(Animal):

    def parler(self):
        return "Miaou !"


# Extension : classe Vache
class Vache(Animal):

    def parler(self):
        return "Meuh !"


# Extension : classe Robot (Duck Typing)
class Robot:

    def parler(self):
        return "Bonjour ! Je suis un robot."


# Fonction qui utilise le polymorphisme
def faire_parler(animal):
    print(animal.parler())


# Programme principal
if __name__ == "__main__":

    animaux = [
        Chien(),
        Chat(),
        Chien(),
        Vache(),
        Robot()
    ]

    # Faire parler tous les objets
    for animal in animaux:
        faire_parler(animal)
