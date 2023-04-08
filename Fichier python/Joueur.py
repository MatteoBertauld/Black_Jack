# Ce fichier utilise un fichier Class avec méthodes

from Paquet_Carte import *
# Permet de définir un object qui va contenir toutes les cartes possible du jeu sous formes de pile soit 4x52cartes
# La class Paquet_Carte contient les méthodes suivantes  ajouter_carte(carte)    retirer_carte()

class Joueur:
    '''Créer un object Joueur qui va contenir toutes les informations du Joueur durant la partie

    Attention il existes 3 types d'Object Joueurs différents
    - Le banquier
    - un bot avec IA
    - Ou un humain

    Le Joueur humain à l'attribut self.bot == False contrairement au bot avec IA

    Le Banquier est stoqué dans une variable à part il n'a donc pas d'attributs qui le différencie d'un Humain

    Attributs:

    - nom             : chaine de caractère contenant le nom indiqué par le joueur

    - liste_carte     : liste avec une liste de 2 valeurs pour chaques cartes qui comprend la valeur et la couleur de la carte

    - somme           : int qui contient la somme des valeurs de toutes les cartes de liste_carte calculé par la méthode calcul_somme

    - score           : int qui contient le score gagné par le joueur  / il n'y a pas de limite

    - arret           : boulean qui permet de savoir si le joueur souhaite s'arreter (True) ou continue de piocher (False)

    - as_vaut_11      : boolean indiquant si les as sont valent 1 ou 11

    - bot             : boolean indiquant si L'object est un bot ou un Humain/Banquier


    - nb_blackjack    : int qui contient le nombre de blackjack en 2 cartes fait par Le Joueur

    - nb_partie_gagner: int qui contient le nombre de blackjack en 2 cartes fait par Le Joueur

    Méthode:

    - calcul_somme  : Calcul la somme des cartes que le joueur possède et met à jour l'attribut somme

    - Pioche        : Fait piocher une carte au joueur et rajoute les informations de la carte piocher dans liste_carte


    '''


    def __init__(self, pseudo):
        ''' Prend un paramètre pseudo et initialise toutes les informations du joueur, avec notamment le pseudo indiqué par le joueur'''


        self.nom = pseudo
        self.bot = False

        self.liste_carte = []
        self.nb_carte = 0

        self.somme = 0
        self.as_vaut_11 = 0

        self.score = 0
        self.arret = False

        self.nb_blackjack = 0
        self.nb_partie_gagner = 0


    def calcul_somme(self):
        ''' Calcul la somme des cartes que le joueur possède et met à jour l'attribut somme'''

        self.somme=0
        si_as = []
        self.as_vaut_11 = 0

        for element in self.liste_carte:

            if element[0] >= 10:
                self.somme += 10
            else:
                if element[0] == 1:
                    si_as.append(element[0])
                else:
                    self.somme += element[0]

        for element in si_as:

            if self.somme <= 10:
                self.somme += 11
                self.as_vaut_11 += 1
            else:
                self.somme += 1

    def pioche(self,monjeu):
        '''Fait piocher une carte au joueur et rajoute les informations de la carte piocher dans liste_carte'''

        ajouter = monjeu.retirer_carte()
        self.liste_carte.append(ajouter)
        self.nb_carte += 1


    def __str__(self):
        ''' Permet l'affichage str des informations du joueur'''

        info_cartes = ""

        for carte in self.liste_carte:

            temp = carte[0]

            if temp == 1:
                temp = "As"

            if temp == 11:
                temp = "Valet"

            if temp == 12:
                temp = "Dame"

            if temp == 13:
                temp = "Roi"

            info_cartes += str(temp) + " de " + str(carte[1]) + "\n"

        a = str(self.nom) + " : \n" + info_cartes + "Somme : " + str(self.somme) + "\n"



        return a