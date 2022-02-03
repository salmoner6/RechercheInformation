# -*- encoding: utf-8 -*-
#************************************
# Auteur : Philippe Mulhem & Erin Salmon 
# Date : January 2021
# Description : Génération d'un vocabulaire à partir d'une liste de fichier texte dans un répertoire
# Usage : python zipf_miashs_2021.py
#************************************

#lib
import imp
from operator import itemgetter
import re
import os

#repertoire qui contient les documents a traiter
inppathname = "/home/dcissm2rs/salmoner/Recherche_infos/cacm-miashs/"

frequency = {} # table des couples (mots/frequences)
compteur = 0

def splitInWords(strinput):
    """
    Function : splitInWords
    Input : strinput : string à être découpée en mots
    Output : la liste les mots découpés
    Description : utilise une expression réguliere
    """
    objRegex=re.compile("([a-z][a-z0-9]+)")
    splitorig=objRegex.findall(strinput.lower())
    splitfinal=filter(None,splitorig)
    # print "SplitInWords" # decouper en mots qui commencent par une lettre suivie d'une suite non-vide de lettres ou de chiffres.
    return splitfinal
    

def Zipf(inpath):
    """
    Function : Zipf
    Input : inpath : string of the path containing the processed files
    Output : none
    Description : ouvre chaque fichier de inpath, sépare en mots et ajoute à frequency
    """
    global frequency
    global compteur
    for filename in os.listdir(inpath):
        print  "processing :"+inppathname+filename
        open_file = open(inppathname+filename, 'r')
        file_to_string = open_file.read()
        words=splitInWords(file_to_string)  # met dans words la liste de mots
        open_file.close()
    # ajouter au tableau de frequences pour chaque mot
        # print "Process words"
        for x in words: 
            if x in frequency.keys():
                frequency[x]+= 1
                compteur += 1

            else: 
                frequency.update({x : 1}) # frequency[x] = 1
                compteur += 1
    # print(frequency)



def PrintInfoGen():
    """
    Function : PrintInfoGen
    Input : none
    Output : none
    Description : affiche les infos générales sur le vocabulaire stocké dans frequency
    """
    # afficher les infos demandees : nombre de termes du vocabulaire, 10 plus frequents
    global frequency
    print "PrintInfoGen"
    print "nombre de mots du vocabulaire : ", len(frequency)

    # 
    # print top 10 words and their frequencies
    # 
    from operator import itemgetter
    i = 0
    for key, value in reversed(sorted(frequency.items(), key=itemgetter(1))):
        print key, ":", value
        i+=1
        if i == 10:
            break

    #
    # print top 10 words without their frequencies
    # 
    # from operator import itemgetter
    # i = 0
    # dict = reversed(sorted(frequency.items(), key=itemgetter(1)))
    # for k, v in dict:
    #     print (k)
    #     i+=1
    #     if i == 10:
    #         break
        

# Appels des 2 fonctions principales
if __name__ == "__main__":
    Zipf(inppathname)
    PrintInfoGen()
    print 'nombre de mots lu :', compteur # afficher le nombre total de mots lus
