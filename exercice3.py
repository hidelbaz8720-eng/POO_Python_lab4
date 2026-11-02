
from abc import ABC, abstractmethod


# Classe abstraite Paiement
class Paiement(ABC):

    def __init__(self, montant):
        if montant <= 0:
            raise ValueError("Le montant doit être positif.")

        self._montant = montant

    @abstractmethod
    def payer(self):
        pass


# Classe CarteBancaire
class CarteBancaire(Paiement):

    def __init__(self, montant, numero, cvv):
        super().__init__(montant)

        if not numero.isdigit() or len(numero) != 16:
            raise ValueError("Le numéro de carte doit contenir 16 chiffres.")

        if not self.verifier_luhn(numero):
            raise ValueError("Numéro de carte invalide.")

        if not cvv.isdigit() or len(cvv) != 3:
            raise ValueError("Le CVV doit contenir 3 chiffres.")

        self.numero = numero
        self.cvv = cvv

    @staticmethod
    def verifier_luhn(numero):
        chiffres = [int(c) for c in numero]
        somme = 0

        for i in range(len(chiffres) - 1, -1, -1):
            chiffre = chiffres[i]

            if (len(chiffres) - i) % 2 == 0:
                chiffre *= 2

                if chiffre > 9:
                    chiffre -= 9

            somme += chiffre

        return somme % 10 == 0

    def payer(self):
        return f"Paiement de {self._montant:.2f} DH effectué par carte bancaire."


# Classe PayPal
class PayPal(Paiement):

    def __init__(self, montant, email, token):
        super().__init__(montant)

        if "@" not in email:
            raise ValueError("Adresse email invalide.")

        self.email = email
        self.token = token

    def payer(self):
        return f"Paiement de {self._montant:.2f} DH effectué avec PayPal."


# Classe Crypto
class Crypto(Paiement):

    def __init__(self, montant, wallet_id, reseau):
        super().__init__(montant)

        if not wallet_id:
            raise ValueError("Identifiant du portefeuille obligatoire.")

        self.wallet_id = wallet_id
        self.reseau = reseau

    def payer(self):
        return f"Paiement de {self._montant:.2f} DH effectué en crypto sur le réseau {self.reseau}."


# Fonction de traitement des paiements
def traiter_paiements(liste):
    for paiement in liste:
        print(paiement.payer())


# Programme principal
if __name__ == "__main__":

    paiements = [

        CarteBancaire(200, "4532015112830366", "123"),
        CarteBancaire(350, "6011111111111117", "456"),

        PayPal(150, "hamza@gmail.com", "TOKEN123"),
        PayPal(250, "test@gmail.com", "TOKEN456"),

        Crypto(500, "WALLET001", "BTC"),
        Crypto(700, "WALLET002", "ETH")

    ]

    traiter_paiements(paiements)
