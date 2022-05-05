import random

#compare le mot entré par le joueur avec le mot a deviner
#proposition est le mot entré par le joueur
#secret est le mot à deviner
def comparer(proposition,secret):
    #On sépare en plusieurs tableaux
    p=list(proposition)
    s=list(secret)
    res=['']*6
    x = 0
    y = 0
    #On test chaque lettre une par une
    while x<=5:
        while y <= 5:
            if(p[x]==s[y]):
                if(x==y):
                    res[x]='o'
                if((x!=y) and (res[x]=='')):
                    res[x]='+'
            y+=1
        y=0
        if(res[x]==''):
            res[x]='x'
        x+=1
    return str.join("",res)

#un tour de la partie
#secret est le mot à deviner
#lexique est la liste de mot du jeu
#Retourne si le tour est gagné ou perdu
def tour(secret,lexique):
    bool = False
    #Tant que la proposition entrée n'est pas valide
    #C'est-à-dire que le mot n'est soit pas dans le lexique
    #Soit qu'il contient des majuscules
    while bool == False:
        proposition = str(input())
        for p in lexique:
            if(proposition==p):
                bool = True
        if(proposition.islower()==False):
            print("Le mot contient des majuscules")
            bool = False
        elif bool == False:
            print("Le mot n'est pas dans le lexique")
        else:
            bool=True
    #Le mot est le bon
    if proposition==secret:
        return True
    else:
        print(comparer(proposition,secret))
        return False

#La partie entière
#lecique est la liste de mots de la partie
def partie(lexique):
    #On prend un mot aléatoire
    secret = lexique[random.randrange(0,len(lexique))]
    #Tour de jeu
    nbtour=0
    won=False
    #Tant que le jeu n'est pas fini
    while nbtour <= 5:
        print("Tour n° " + str(nbtour+1))
        bool = tour(secret, lexique)
        if bool == True:
            won=True
            break
        nbtour+=1
        print("Raté")
    if won == True:
        print("Tu as gagné!")
    elif won == False:
        print("Tu as perdu!")

#importation des mots du jeu
#nomFichier est le chemin vers le fichier qui contient les mots
def lire_exique(nomFichier):
    l = open(nomFichier, 'r')
    lexique = l.read().splitlines()
    print(lexique)
    l.close()
    return lexique

if __name__ == '__main__':
    lexique = lire_exique("lexique.txt")
    partie(lexique)
