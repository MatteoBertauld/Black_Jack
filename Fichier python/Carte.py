# Ce fichier utilise un fichier Class avec méthodes

from Paquet_Carte import *
# Permet de définir un object qui va contenir toutes les cartes possible du jeu sous formes de pile soit 4x52cartes
# La class Paquet_Carte contient les méthodes suivantes  ajouter_carte(carte)    retirer_carte()



class Carte :
    '''Permet de Créer des Objects Cartes avec pour chaques objects définies les informations valeurs et couleurs

    Informations :

    -valeur  : int contient la valeur de la carte (avec l'as qui par default vaut 1, et le valet, la dame et le roi qui valent respectivement 11,12 et 13)
    -couleur : chaine de caractère qui contient le symbole de la carte ( "pique" / "trefle" / "carreau" / "coeur" )

    '''

    def __init__(self,valeur,couleur):
        '''Prend deux paramètres valeur et couleur et initialise l'object carte, avec les valeurs donnés'''

        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        ''' Permet l'affichage str des informations de la carte'''

        return str(self.valeur) + " de " + str(self.couleur)
