# -*- encoding: utf-8 -*-
#************************************
# Auteur : Philippe Mulhem
# Date : January 2021
# Description : Génération d'un vocabulaire à partir d'une liste de fichier texte dans un répertoire
# Usage : python zipf_miashs_2021.py
#************************************

#lib
from operator import itemgetter
import re
import os

#repertoire qui contient les documents a traiter
inppathname = "/home/dcissm2rs/salmoner/Recherche_infos/cacm-miashs/"

frequency = {} # table des couples (mots/frequences)

def splitInWords(strinput):
    """
    Function : splitInWords
    Input : strinput : string à être découpée en mots
    Output : la liste les mots découpés
    Description : utilise une expression réguliere
    """
    print "SplitInWords" # A FAIRE : decouper en mots qui commencent par une lettre suivie d'une suite non-vide de lettres ou de chiffres.

def Zipf(inpath):
    """
    Function : Zipf
    Input : inpath : string of the path containing the processed files
    Output : none
    Description : ouvre chaque fichier de inpath, sépare en mots et ajoute à frequency
    """
    global frequency
    for filename in os.listdir(inpath):
        print  "processing :"+inppathname+filename
        open_file = open(inppathname+filename, 'r')
        file_to_string = open_file.read()
        words=splitInWords(file_to_string)  # met dans words la liste de mots
        open_file.close()
    # A FAIRE : ajouter au tableau de frequences pour chaque mot
        print "Process words"

def PrintInfoGen():
    """
    Function : PrintInfoGen
    Input : none
    Output : none
    Description : affiche les infos générales sur le vocabulaire stocké dans frequency
    """
    # A FAIRE : afficher les infos demandees : nombre de termes du vocabulaire, 10 plus frequents
    #           il faut trier la liste des termes.
    global frequency
    print "PrintInfoGen"


# Appels des 2 fonctions principales
if __name__ == "__main__":
    Zipf(inppathname)
    PrintInfoGen()
    print 'nombre de mots lu :' # A FAIRE : afficher le nombre total de mots lus
