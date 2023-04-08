# TNSI
# Exercice Pile version "classe" du TP D02
# M. Pereira - T. Rey
# Corrigé

class Pile:
    """Classe définissant une pile. Attributs :
    - sa taille max
    - ses éléments (une liste Python)
    - la première case libre
    Méthodes :
    - empile(e)
    - depile()
    - estVide()
    - estPleine
    - affichePile
    """

    # Constructeur :
    def __init__(self,taille):
        self._taille = taille # double _ : attribut privé
        self._elements = [0]*taille # tableau des éléments
        self._case_libre = 0 # première case libre

    def estVide(self):
        """Retourne un booléen indiquant si la pile est vide."""
        return self._case_libre == 0

    def estPleine(self):
        """Retourne un booléen indiquant si la pile est pleine."""
        return self._taille == self._case_libre

    def affichePile(self):
        """Donne un affichage de la pile"""
        if self.estVide():
            print("La pile est vide")
        else:
            for i in range(self._case_libre-1,-1,-1):
                print(self._elements[i])
        if self.estPleine():
            print("La pile est pleine")
        print("-------")

    def empile(self,e):
        """Ajoute l'élément e à la pile si la pile n'est pas pleine.
        Retourne False si la pile est pleine"""
        if self.estPleine():
            return False
        else:
            self._elements[self._case_libre] = e
            self._case_libre = self._case_libre + 1

    def depile(self):
        """Retire le dernier élément de la pile et le retourne.
        Si la pile est vide, retourne False."""
        if self.estVide():
            return False
        else:
            self._case_libre = self._case_libre - 1
            return self._elements[self._case_libre]



# Exemple
def exemple():
    p = Pile(5)
    p.empile(7)
    p.affichePile()
    p.empile(8)
    p.empile(18)
    p.empile(84)
    p.empile(87)
    p.empile(7)
    p.empile(4)
    p.affichePile()
    for i in range(6):
        p.depile()
        p.affichePile()

