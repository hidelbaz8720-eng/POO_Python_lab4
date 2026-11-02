# TP 4 : Polymorphisme en Python

##  Présentation
Ce TP porte sur le polymorphisme en programmation orientée objet (POO) avec Python. Il permet de comprendre comment plusieurs classes peuvent partager une interface commune tout en ayant des comportements différents.

##  Objectifs pédagogiques
- Comprendre le principe du polymorphisme.
- Utiliser l'héritage entre les classes.
- Manipuler les classes abstraites.
- Redéfinir les méthodes dans les classes filles.
- Utiliser des collections contenant différents types d'objets.
- Appliquer le principe de substitution et le Duck Typing.

---

##  Exercice 1 : Polymorphisme avec les animaux

### Description
Création d'une classe mère `Animal` et de plusieurs classes filles `Chien`, `Chat` et `Vache`.

Chaque classe redéfinit la méthode `parler()` pour produire un son différent.

Une classe `Robot` est également ajoutée pour démontrer le principe du Duck Typing, sans hériter de la classe `Animal`.

### Concepts utilisés
- Héritage
- Redéfinition des méthodes
- Polymorphisme
- Duck Typing
- Collection d'objets

### Capture d'écran de l'exécution

<img width="1366" height="768" alt="ex1" src="https://github.com/user-attachments/assets/7676a31e-87b5-416c-823b-68d84d323992" />


##  Exercice 2 : Gestion des formes géométriques

### Description
Création d'une classe abstraite `Forme` contenant la méthode abstraite `aire()`.

Trois classes filles sont développées :
- `Cercle` : calcul de l'aire d'un cercle.
- `Rectangle` : calcul de l'aire d'un rectangle.
- `Triangle` : calcul de l'aire d'un triangle.

Une classe supplémentaire `Carre` est ajoutée par héritage de `Rectangle`.

Les différentes formes sont stockées dans une même liste et leurs aires sont calculées automatiquement.

### Concepts utilisés
- Classes abstraites avec `ABC`.
- Décorateur `@abstractmethod`.
- Héritage.
- Polymorphisme.
- Méthode spéciale `__str__()`.
- Constructeur parent avec `super()`.

###  Capture d'écran de l'exécution

<img width="1366" height="768" alt="ex2" src="https://github.com/user-attachments/assets/cac53ae6-54b3-465c-bb31-b77f76d5ec0c" />


##  Exercice 3 : Gestion des moyens de paiement

### Description
Création d'une classe abstraite `Paiement` avec une méthode abstraite `payer()`.

Trois classes spécialisées sont développées :
- `CarteBancaire` : paiement par carte bancaire.
- `PayPal` : paiement via un compte PayPal.
- `Crypto` : paiement en cryptomonnaie.

Une fonction `traiter_paiements()` permet de parcourir une collection hétérogène et d'exécuter la méthode `payer()` sans vérifier le type des objets.

Des vérifications sont également ajoutées pour le montant, le numéro de carte et les informations de paiement.

### Concepts utilisés
- Abstraction.
- Héritage.
- Encapsulation.
- Polymorphisme.
- Validation des données.
- Algorithme de Luhn.
- Utilisation de `super()`.

###  Capture d'écran de l'exécution

<img width="1366" height="768" alt="ex3" src="https://github.com/user-attachments/assets/05d45510-2bfb-415d-b6bd-a81200f08a8d" />


## Structure du projet

```text
TP4-Polymorphisme/
│
├── exercice1.py
├── exercice2.py
├── paiements.py
├── README.md
│
└── images/
    ├── exercice1.png
    ├── exercice2.png
    └── exercice3.png
```

##  Technologies utilisées
- Python 3
- Programmation orientée objet (POO)
- Module `abc`
- Bibliothèque `math`

## Conclusion

Ce TP m'a permis de mettre en pratique les principaux concepts de la programmation orientée objet en Python, notamment l'héritage, l'abstraction et le polymorphisme.

À travers les trois exercices, j'ai appris à concevoir des classes réutilisables, à redéfinir des méthodes et à manipuler différents objets de manière interchangeable.
