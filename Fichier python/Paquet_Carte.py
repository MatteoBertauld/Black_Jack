# Ce fichier utilise un fichier Class avec méthodes

from lesPilescorrige import *
# Contient une class Pile qui permet de creer et manipuler une pile de taille définie
# La class pile comporte les méthodes suivantes  estVide() estPleine()  Afficher_pile()   empiler(element)   depiler()


class Paquet_Carte :
    '''Va permettre de Creer un object qui va contenir toutes les cartes possible du jeu sous formes de pile (self.tas) soit 4x52cartes

    Attribut:

    tas : Pile de taille 208 qui va contenir les informations de chaques cartes du jeu
    nb_carte : int qui indique le nombre de carte restant dans le jeu

    Méthode:

    (note : cette class utilise la classe Pile et les méthodes qui vont avec du fichier lesPilescorrige.py)

    - ajouter_carte permet de rajouter une carte de son choix en dernière position de la pile
    - retirer_carte permet de retirer la dernière carte de la pile
    - affichage renvoie les informations de la cartes ( valeur et couleur )
    - verif_tas renvoie un boolean qui indique s'il y a assez de carte pour relancer une partie

    '''

    def __init__ (self):
        '''initialise self.tas avec une pile définit de taile 208 (nombre total de cartes)'''

        self.tas = Pile(52*4)  # Un paquet de carte contient 52cartes x 4 paquets
        self.nb_carte = 0

    def ajouter_carte(self, carte):
        '''prend un paramètre carte et rajoute la carte choisi dans la liste'''

        self.tas.empile(carte)
        self.nb_carte += 1

    def retirer_carte(self):
        '''Retire la dernière carte de la pile et renvoie ses informations (valeurs et couleurs)'''

        self.nb_carte -= 1

        return self.tas.depile()


    def verif_tas(self):
        '''Renvoie un boolean indiquant s'il y a assez de carte dans le tas pour relancer une partie'''

        if self.nb_carte < 55: # 55 : on a au maximum 11 cartes par joueurs x nombre de joueur (5) donc 55 cartes

            return True
        return False


    def __str__(self):
        ''' Permet l'affichage str des informations du Paquet de carte'''

        self.tas.affichePile()

        return ""