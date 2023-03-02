from random import *


def cles():
    """Cette fonction ne prend pas de parametre et renvoie un valeur contenant les 
    valeurs propres à chaque joueur"""
    valeur={"trous_J1" : [4,4,4,4,4,4], "trous_J2": [4,4,4,4,4,4], "grenier_J1" : 0, "grenier_J2" : 0}
    return valeur

def plateau(valeur):
    """Cette fonction ne prend pas de parametre et affiche le plateau"""
    print("\nJ1   6 | 5 | 4 | 3 | 2 | 1    ",valeur['grenier_J1'])
    chaine = "     "
    for i in range(6):
        chaine += str(valeur["trous_J1"][-i-1]) + "   "
    print (chaine)
    print("")
    chaine = "     "
    for i in range(6):
        chaine += str(valeur["trous_J2"][i]) + "   "
    print(chaine)
    print("J2   1 | 2 | 3 | 4 | 5 | 6    ", valeur['grenier_J2'] , "\n")
    return

def action_joueur(joueur):
    '''Demande au joueur quel coup souhaite t'il jouer, et renvoie le coup souhaiter entre 0 et 5'''
    print("C'est au tour du Joueur " + str(joueur))
    coup_jouer=int(input("Quel coup souhaitez-vous jouer (nombre entre 1 et 6) ?  "))
    
    return coup_jouer
    
    
    
    
def jouer(valeur,colonne,joueur):

    """Cette fonction permet au 1er joueur de prendre toutes les graines de l'un des 6 trous se trouvant de son côté et en dépose une dans chaque                 trou suivant celui qu'il a vidé."""
    
    if joueur == 1:
        autrejoueur = 2
    else:
        autrejoueur = 1
        
    j = colonne
    # Verifie combien de points il y a à distribuer
    distribue=valeur["trous_J"+str(joueur)][colonne-1]
    
    # Répartie les points tant que l'on a pas tout distribué
    while distribue != 0:
        
        # Verifie dans quel case les points doivent etre placés
        if j < 6:
            if colonne-1 != j:
                valeur["trous_J"+str(joueur)][j] += 1
                distribue -= 1
            j += 1
            
        else:
            valeur["trous_J"+str(autrejoueur)][j-6] += 1
            j += 1
            distribue -= 1
        if j > 11:
            j = 0
            
    if j < 6:
        joueurtombe = joueur
        tombee = j
    else:
        joueurtombe = autrejoueur
        tombee = j-6
    print(tombee,joueurtombe)
    # Met la valeur de la case de base à 0
    valeur["trous_J"+str(joueur)][colonne-1]=0
    return valeur,tombee,joueurtombe


def capture(valeur, trou, joueur, joueurtombe):
    '''prend comme entrée
    valeur = des tuples nommé contenant différentes listes avec toutes les informations sur les graines
    joueur = chiffres entre 1 et 2 indiquant qui est en train de jouer
    trou = chiffres entre 0 et 6, qui est l'indice de la dernière case sur laquelle on dépose des graines
    Cette fonction permet de capturer les graines présente dans la dernière case, Si la dernière graine qui est déposée dans un trou de l’adversaire comportant déjà 2 ou
3 graines. Les graines capturées sont déposée dans le grenier du joueur et le trou est laissé vide.
    '''

    trou -= 1
    test=1
    
    if joueur != joueurtombe:
        while test == 1: #tant que test==1
            
            if joueur == 1:   
                
                #si la valeur du trou est égale à 2 ou 3
                if valeur['trous_J2'][trou] == 2 or valeur['trous_J2'][trou] == 3:  
                
                    #on ajoute le nombre de graine présente dans le trou dans le grenier du joueur 1
                    valeur['grenier_J1'] = int(valeur['grenier_J1']) + int(valeur['trous_J2'][trou]) 
                    #on vide le trou
                    valeur['trous_J2'][trou] = 0 
                    
                    if trou==0:
                        test=0
                    else:
                        trou-=1
                    
                else:
                    #on sort de la boucle while
                    test = 0 
                    
            else:
                
                #si la valeur du trou est égale à 2 ou 3
                if valeur['trous_J1'][trou] == 2 or valeur['trous_J1'][trou] == 3:
                    
                    #on ajoute le nombre de graine présente dans le trou dans le grenier du joueur 2
                    valeur['grenier_J2'] = int(valeur['grenier_J2']) + int(valeur['trous_J1'][trou])  
                    #on vide le trou
                    valeur['trous_J1'][trou] = 0  
                    
                    if trou==0:
                        test=0
                    else:
                        trou-=1
                    
                    
                else:
                    #on sort de la boucle while
                    test=0 


def jeu():
    """Cette fonction initie le jeu sans interface graphique"""
    valeur = cles()
    joueur = randint(1,2)
    
    while valeur['grenier_J1'] <= 24 and valeur['grenier_J2'] <= 24 and valeur['grenier_J1'] + valeur['grenier_J2'] != 48:
        
        plateau(valeur)
        coup = action_joueur(joueur)
        valeur, tombee, joueurtombe = jouer(valeur, coup, joueur)
        capture(valeur, tombee, joueur, joueurtombe)
        print("tombée",tombee)
    
        if valeur['trous_J1'] == [0 for i in range(6)]:
            for i in range(6): valeur['grenier_J2'] += valeur['trous_J2'][i]
            
        elif valeur['trous_J2'] == [0 for i in range(6)]:
            for i in range(6): valeur['grenier_J1'] += valeur['trous_J1'][i]
        
        if joueur == 1:
            joueur = 2
        else:
            joueur = 1
    
    return valeur