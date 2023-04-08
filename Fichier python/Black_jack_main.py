## Terminal Projet 1 Black Jack  / Groupe 6 : Matt,théo, Bictor, Edgar  / M. Pereira - T. Rey

from random import *

# Ce projet utilise plusieurs fichiers Class avec méthodes

from lesPilescorrige import *
# Contient une class Pile qui permet de creer et manipuler une pile de taille définie
# La class pile comporte les méthodes suivantes  estVide() estPleine()  Afficher_pile()   empiler(element)   depiler()

from Carte import *
# Permet de définir des objects Cartes avec une valeur et une couleur

from Paquet_Carte import *
# Permet de définir un object qui va contenir toutes les cartes possible du jeu sous formes de pile soit 4x52cartes
# La class Paquet_Carte contient les méthodes suivantes  ajouter_carte(carte)    retirer_carte()

from Joueur import *
# Permet de creer un object Joueur qui contient toutes les informations de chaques joueurs de la parties (Banquier y compris)
# La class Joueur possèdes les méthodes suivantes   calcul_somme()   pioche(monjeu)


def generer_carte():
    '''Creer un object monjeu via la class Paquet_Carte qui va contenir toutes les cartes du jeu rangée aléatoirement'''

    monjeu = Paquet_Carte()  # creer un object monjeu qui va contenir toutes les cartes de la pioche


    #ajoute 208 cartes (sous formes de liste avec la couleur et la valeur de la carte) à une liste temporaire (liste_jeu_complet)
    liste_jeu_complet = []

    for i in range(4):
        for coul in ['pique', 'trefle','coeur','carreau']:
            for i in range(1,14):
                info_carte = Carte(i, coul)
                liste=[info_carte.valeur,info_carte.couleur]
                liste_jeu_complet.append(liste)


    # Parcourt liste_jeu_complet et ajoute une des valeurs aléatoire de la liste à la Pile tas de l'object monjeu
    # (le but avoir une pile contenant la liste de toute les cartes rangé de façon aléatoire)

    for i in range(len(liste_jeu_complet)):

        carte = liste_jeu_complet.pop(randint(0,len(liste_jeu_complet)-1))
        monjeu.ajouter_carte(carte)

    return monjeu





def info_banque_auto():
    '''Demande "Si la banque est gérer par un Joueur" et renvoie la réponse sous forme de boolean'''
    
    
    stop = False
    compteur = 0
    
    while stop == False:
        
        banque_auto = str(input("\nSouhaiter vous que la Banque soit gérer par un Joueur ? (1 : oui / 0 : non)"))
        

        if compteur > 3:
            stop = True
            banque_auto= "oui"

        if banque_auto =='1' or banque_auto =='oui':
            stop = True
            banque_auto = False
            
        if banque_auto == 'non' or banque_auto == '0':
            stop = True
            banque_auto = True

        if stop == False:
            print("La valeur que vous avez renvoyé est incorrect \n")
            compteur += 1
    
    print("")
    
    return banque_auto





def info_nb_joueur(banque_auto):
    '''Prend un paramètre, Banque auto : boolean indiquant si la banque est gérer par un Joueur ou non
    
    Cette fonction demande "le nombre de Joueur souhaiter" et renvoie le nombre de Joueur sous forme (int)
    '''

    stop = False
    compteur = 0
    

    while stop == False:  # Tant que la valeur renvoyer n'est pas correct 
        
        # Permet d'indiquer le nombre de Joueur min et max selon si la banque est gérer par un Joueur ou non
        if banque_auto == True:
            nb_joueur_max = 4
            nb_joueur_min = 0
        else:
            nb_joueur_max = 5
            nb_joueur_min = 1
        
        
        nb_joueur = str(input("Combien voulez-vous de Joueur ? (int " + str(nb_joueur_min) + " à " + str(nb_joueur_max) + ") "))
        
        
        # Si le compteeur dépasse 3 on renvoie 1 Joueur pour éviter une boucle infini
        if compteur > 3:
            stop = True
            nb_joueur= "1"

        if nb_joueur_min <= int(nb_joueur) and int(nb_joueur) <= nb_joueur_max  :
            stop = True

        else:
            print("La valeur que vous avez renvoyé est incorrect \n")
            compteur += 1
    
    return int(nb_joueur)





def select_joueur(nb_joueur,banque_auto):
    '''Prends en paramètres :
    - nb_joueur : int(0 à 5) indiquant le nombre de Joueur Humain
    - banque_auto : boulean indiquant si la banque doit être gérer automatiquement ou non
    
    Cette fonction demande et attribue un nom pour chaques joueurs, séléctionne un banquier de manière aléatoire, et Creer les objects Joueurs
    
    A noter que, Le banquier et les bots ou IA sont considérer comme des Objects Joueurs même s'il ont un fonctionnement différents
    
    Renvoie Une liste de Tous les Object joueurs sans compter le banquier et l'Object Joueur(Banquier)
    '''
    
    
    if banque_auto == True:
        Nb_bot = 4-nb_joueur
    else:
        Nb_bot = 5-nb_joueur
        
        
    # Attribut un nom aléatoire pour les bots
    nom_bot = ["Bot(Jean Bombeur)","Bot(Louis Fine)","Bot(Anne Riz)","Bot(Le Père Spective)","Bot(Jone Yalidai)"]
    L_nom_bot = []  # listes des nom des bots
    
    for i in range(Nb_bot):
        L_nom_bot.append(nom_bot.pop(randint(0,len(nom_bot)-1)))
    
    
    # demande le nom pour chaque joueur à l'utilisateur
    L_nom_joueur= [] # listes des noms de chaques joueurs
    
    for i in range(nb_joueur):
        L_nom_joueur.append(str(input("joueur " + str(i+1) +" :")))
    
    print("")
    
    
    # Si jamais l'utilisateur ne rentre pas de nom, on lui definie un nom par default
    
    for i in range(len(L_nom_joueur)) :

        if L_nom_joueur[i] == '':
            L_nom_joueur[i] = "Joueur " + str(i+1)
            
            
    # si la banque est gérer par un joueur on attribut aléatoirement le role de Banquier
    
    if banque_auto == False:
        alea= randint(0,len(L_nom_joueur)-1)
        banque = L_nom_joueur.pop(alea)
        print(banque + " est le banquier. \n")
        
        Banquier= Joueur("Banquier (" + banque + ")")
    
    # sinon on créer un nouvelle Object Banquier
    else:
        Banquier = Joueur("Banquier")
    
    L_joueur = []  
    
    
    # On definie les 4 Joueurs
    
    for i in range(len(L_nom_bot)): 
        
        L_joueur.append(Joueur(L_nom_bot[i]))
        
        L_joueur[i].bot = True
    
    for i in range(len(L_nom_joueur)): 
        
        L_joueur.append(Joueur(L_nom_joueur[i]))
        
    return [L_joueur,Banquier]  # on renvoie la liste des 4 Joueurs et le Banquier
    

 
    
def gagnant(liste_joueur,Banquier):
    """Prends en paramètres
    - liste_joueur : Liste de Tous les Objects Joueur de type (humain ou bot)
    - Banquier     : L'object Banquier
    
    Cette Fonction calcul quelles sont les joueurs qui ont gagnés la partie selon 5 cas différents et attribue les points gagnées à chaques Joueurs (banquier et bot y compris)"""

    joueur_en_jeu = []  # liste de tous les joueurs ayant une somme infèrieur à 21
    liste_gagnant = []  # liste des tous les joueurs qui ont gagné la partie
    blackjack=[]  # liste des tous les joueurs ayant une somme égale à 21 en 2 cartes

    mise = 12
    pot = 4*mise


    # Pour tous les joueurs on effectue plusieurs tests et on attribue chaques joueur à une ou plusieurs listes ci dessus

    for J in liste_joueur:

        if J.somme <=21:
            joueur_en_jeu.append(J)

        if J.somme == 21:
            if J.nb_carte == 2:
                blackjack.append(J)

        if Banquier.somme > 21:
            if J.somme <= 21:
                liste_gagnant.append(J)

        if Banquier.somme <= 21:
            if J.somme >= Banquier.somme:
                if J.somme <= 21:
                    liste_gagnant.append(J)


    a = ""
    
    # Cas 1 : blackjack
    if len(blackjack) >= 1:
        pot = pot/len(blackjack)

        for J in blackjack:
            
            J.nb_partie_gagner += 1
            J.nb_blackjack += 1
            J.score += pot
            a += str(J.nom) + " gagne " + str(pot) + " points" + "\n"

        print("Black Jack en 2 cartes: " + "\n" + a)

        return
        
    # Cas 2 : blackjack du Banquier
    if len(blackjack) == 0:

        if Banquier.somme == 21 and Banquier.nb_carte ==2:
            
            Banquier.nb_partie_gagner += 1
            Banquier.nb_blackjack += 1
            Banquier.score += pot
            a += str(Banquier.nom) + " gagne " + str(pot) + " points" + "\n"
            
            print("Le Banquier remporte la partie avec un Black Jack en 2 cartes: " + "\n" + a)

            return
        

    # Cas 3 : Le banquier dépasse
    if Banquier.somme > 21:

        for J in joueur_en_jeu:
            
            J.score += mise*2
            J.nb_partie_gagner += 1
            a += str(J.nom) + " gagne " + str(mise*2) + " points" + "\n"

        print("Le banquier à dépassé : " + "\n" + a)

        return

    # Cas 4 : La mise est partagé entre les joueurs qui ont plus ou autant que le banquier
    if Banquier.somme <= 21:
        if len(liste_gagnant) >= 1:
            pot = pot/len(liste_gagnant)

            for J in liste_gagnant:
                
                J.score += pot
                J.nb_partie_gagner += 1

                a += str(J.nom) + " gagne " + str(pot) + " points" + "\n"
            
            
            Banque_somme = str(Banquier.somme)
            if Banquier.somme < 21:
                Banque_somme += " ou plus"
            
            print("Les joueurs ayant " + Banque_somme + " se repartisse la mise: " + "\n" + a)

            return

    # Cas 5 : Personne ne gagne la banque récupère toutes les mises
    if Banquier.somme <= 21:
        if len(liste_gagnant) == 0:

            Banquier.nb_partie_gagner += 1
            Banquier.score += pot

            print("Le banquier à gagné : " + str(pot) + " points \n")

            return


def bot(Obj_joueur):
    '''Prends un paramètre id_joueur, qui contient un Object Joueur de type (humain, bot ou Banquier) et renvoie une chaine de caractère selon plusieurs critères 'oui' ou 'non' qui indique à la fonction repartition si le bot souhaite repiocher'''
     
    if Obj_joueur.somme <= 14:
        
        return 'oui'  # indique qu'on souhaite repiocher
     
    # Si les as valents 11, c'est qu'on peut repiocher sans risquer de dépasser pour espérer avoir mieux
    if Obj_joueur.as_vaut_11 >= 1 and Obj_joueur.somme <= 18:
        
        return 'oui'  # indique qu'on souhaite repiocher
        
    return 'non'  # indique qu'on ne souhaite pas repiocher
         
    

def repartition(liste_joueur,Banquier,monjeu):
    '''Prends en paramètres
    - liste_joueur qui contient une liste de tous les Objects Joueurs de type (bot ou humain)
    - Banquier qui contient L'Object Joueur de type Banquier
    - monjeu qui contient une pile de toutes les Cartes du jeu
    
    Cette fonction fait piocher les joueurs jusqu'a ce qu'il s'arrete ou que la somme du jouer est supèrieur ou égale à 21
    '''
    
    # Ici puisque ce n'est pas précisé j'ai décidé comme dans les règles officiel de faire piocher 2 cartes au Banquier avant tous les Joueurs et d'afficher uniquement la première carte du banquier. ça ne change pas grand chose au jeu
    Banquier.pioche(monjeu)
    Banquier.calcul_somme()
    print(Banquier)

    Banquier.pioche(monjeu)
    Banquier.calcul_somme()
    
    print("___________________________________ \n")
    
    
    # Pour Tous les Objects Joueur de type (bot ou humain)  :
    for J in liste_joueur: 
    
        # On fait piocher 2 cartes pour chaques Joueur puisqu'il est impossible de dépasser 21 avec 2 cartes, donc dans tous les cas le Joueur devra repiocher tant qu'il n'aura pas au moins 2 cartes
        J.pioche(monjeu)
        J.pioche(monjeu)
        J.calcul_somme()
        
        # on vérifié que le Joueur n'a pas fait de Black Jack en 2 cartes
        if J.somme == 21:
            if J.nb_carte == 2:
                print(J)
                
                print(J.nom + " vient de faire un Black Jack !! \n")
                print("___________________________________ \n")
        
    all_arret = 0
    
    # Tant que les 4 Joueurs ne se sont pas arreter
    while all_arret <= 4:
    
        for J in liste_joueur:
    
            if J.somme < 21 and J.arret == False:
                
                print(J)
                
                # Si l'Object Joueur est de type humain
                if J.bot == False:
                
                    stop = False
                    compteur = 0
                    # tant que la valeur renvoyé est incorect
                    while stop == False:
                        
                        reponse = str(input(J.nom + " : Souhaiter-vous continuer à piocher (1 : oui / 0 : non) :"))
                        
                        # Au bout de 3 valeurs incorect on décide par défault que le Joueur ne repioche pas pour éviter une boucle infini
                        if compteur > 3:
                            stop = True
                            reponse = "non"
        
                        if reponse =='1' or reponse =='oui' or reponse == 'non' or reponse == '0':
                            stop = True
        
                        else:
                            print("La valeur que vous avez renvoyé est incorrect \n")
                            compteur += 1
                
                # si c'est un Object de type Bot on utilise la fonction bot pour avoir une réponse
                else:
                    reponse = bot(J)
                    
                if reponse == '0' or reponse == 'non':
                    J.arret = True
                    print(J.nom + " s'arrête de piocher")
                else:
                    if J.bot == True:
                        print(J.nom + " décide de piocher")
                    
                    J.pioche(monjeu)
                    J.calcul_somme()
                    
                    print("")
                    print(J)
                    
                    if J.somme > 21:
                        print(J.nom + " viens de dépasser")

    
                print("___________________________________ \n")
            
            else:
                all_arret +=1


def banque(Banquier,monjeu):
    '''Prend en paramètres 
    - liste_joueur qui contient une liste de tous les Objects Joueurs de type (bot ou humain)
    - Banquier qui contient L'Object Joueur de type Banquier

    Cette fonction fait piocher le banquier tant que la somme de ces cartes n'est pas supèrieur à 17 puis affiche son jeu et précise s'il a eu un Black Jack en 2 cartes'''
    
    while Banquier.somme <=17:
        Banquier.pioche(monjeu)
        Banquier.calcul_somme()

    print(Banquier)
    
    if Banquier.somme == 21:
        if Banquier.nb_carte == 2:
            print(Banquier.nom + " vient de faire un Black Jack !! \n")


def affiche_somme(liste_joueur,Banquier):
    '''Prend en paramètres 
    - liste_joueur qui contient une liste de tous les Objects Joueurs de type (bot ou humain)
    - Banquier qui contient L'Object Joueur de type Banquier
    
    Cette fonction affiche la sommes des cartes de chaques joueurs'''

    a= "Sommes de toutes les cartes : \n"
    for joueur in liste_joueur:
        a += str(joueur.nom) + " : " + str(joueur.somme)
        if joueur.somme == 21:
            if joueur.nb_carte == 2:
                a+= " Black Jack !!"
        a += "\n"

    a += str(Banquier.nom) + " : " + str(Banquier.somme)
    if Banquier.somme == 21:
        if Banquier.nb_carte == 2:
            a+= " Black Jack !!"
    a += "\n"

    print(a)

def affiche_score(liste_joueur,Banquier):
    '''Prend en paramètres 
    - liste_joueur qui contient une liste de tous les Objects Joueurs de type (bot ou humain)
    - Banquier qui contient L'Object Joueur de type Banquier
    
    Cette fonction affiches le score de chaques joueurs'''

    a= "Score : \n"
    for joueur in liste_joueur:
        a += str(joueur.nom) + " : " + str(joueur.score) + "\n"

    a += str(Banquier.nom) + " : " + str(Banquier.score) + "\n"

    print(a)

def reset(liste_joueur,Banquier):
    '''Prend en paramètres 
    - liste_joueur qui contient une liste de tous les Objects Joueurs de type (bot ou humain)
    - Banquier qui contient L'Object Joueur de type Banquier
    
    Cette fonction réinitialise Pour chaque Object Joueur les attributs liste_carte, arret nb_carte, pour pouvoir relancer une partie'''

    for J in liste_joueur:

        J.liste_carte = []
        J.arret = False
        J.nb_carte = 0

    Banquier.liste_carte = []


def Classement_fin_partie(liste_joueur,Banquier):
    '''Prend en paramètres 
    - liste_joueur qui contient une liste de tous les Objects Joueurs de type (bot ou humain)
    - Banquier qui contient L'Object Joueur de type Banquier
    
    Cette fonction affiche le classement à la fin de la partie avec pour chaques Joueurs les infos sur le nombre de Black Jack fait durant la partie et le nombre de Partie gagnées
    '''
    
    Liste = liste_joueur
    
    Liste.append(Banquier)
    
    classement = []
    banque = False
    
    for i in range(len(Liste)):
        max = Liste[0].score
        maxJ = 0
        
        for J in range (1,len(Liste)):
            
            if Liste[J].score > max:
                max = Liste[J].score
                maxJ = J
        
        classement.append(Liste.pop(maxJ))

    a = ""
    
    
    
    print("\nClassement : \n1er : " + str(classement[0].nom) + " avec " + str(classement[0].score) + " points\n" + str(classement[0].nb_blackjack) + " Black Jack et " + str(classement[0].nb_partie_gagner) + " manches gagnées\n")
    
    for i in range(1,len(classement)):
        print(str(i+1) +"ième : " + str(classement[i].nom) + " avec " + str(classement[i].score) + " points\n" + str(classement[i].nb_blackjack) + " Black Jack et " + str(classement[i].nb_partie_gagner) + " manches gagnées\n")
        
    print("Merci d'avoir Jouer ;)")
        
    return
    
    

def jouer():
    '''Utilise toutes les Fonctions précédentes et simule une partie de Black Jack avec des Bots'''

    banque_auto = info_banque_auto()
    Nb_joueur = info_nb_joueur(banque_auto)

    temp = select_joueur(Nb_joueur,banque_auto)
    
    Banquier = temp[1]
    liste_joueur = temp[0]

    rejouer = True
    
    monjeu = generer_carte()

    while rejouer == True:

        repartition(liste_joueur,Banquier,monjeu)
        banque(Banquier,monjeu)

        affiche_somme(liste_joueur,Banquier)

        gagnant(liste_joueur,Banquier)

        affiche_score(liste_joueur,Banquier)
        
        if monjeu.verif_tas() == True:
            print("Fin de partie : Il n'y a plus assez de cartes")
            rejouer = False
        
        if rejouer == True:
            continuer= str(input("Souhaiter-vous rejouer (1 : oui / 0 : non) :"))
            print("")

            if continuer == '1' or continuer == 'oui':
                rejouer = True
            else:
                rejouer = False

            reset(liste_joueur,Banquier)
        
    Classement_fin_partie(liste_joueur,Banquier)
            
        
