#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 12:18:28 2022

@author: pthuringer
"""

from SortOffensif import SortOffensif
from SortDefensif import SortDefensif
from SortSournois import SortSournois

class Tour:
    

    def __init__(self,numero, sorcier1, sorcier2, score):
        #initialise le numero du tour
        self.numero = []
        #initialise la liste sorcier avec les deux sorciers 
        sorcier = [1, 2[sorcier1, sorcier2]]
        #initialise le score à 0,0
        self.score = [sorcier1, sorcier [0, 0]]
        #affiche : # Tour [numero du tour] # 
        print("Tour" + self.numero)
    

    def getNumero(self):
        #retourne le numero du tour
        return self.numero
    

    def getScore(self):
        #retourne le score en fin de tour
        return self.score
    

    def getSorciers(self):
        #retourne la liste des sorciers participant au tour
        listesorcier = [nom1,nom2]
        print(listesorcier)

    def tourSorcier1(self):
        print(sorcier1)
        #affiche : - [nom du sorcier 1] :
        # Teste si le numero du tour est 1 ou 4,7,10 etc c’est-à-dire si numero%3=1 -> Dans ce cas le sorcier 1 doit lancer un sort offensif
        if numero%3=1 :
            while(True):
                print('Choisir un sort offensif: 1 pour Flipendo, 2 pour Impedimenta, 3 pour Crache limace : ')
                if 1 :
                       #instancie le sort offensif Flipendo avec 4 points de dégâts
                       SortOffensif('Flipendo', 4)
                       SortOffensif.append(sorts)
                       break
                    elif 2 : 
                       #instancie le sort offensif Impedimenta avec 5 points de dégâts
                       SortOffensif('Impedimenta', 5)
                       SortOffensif.append(sorts)
                       break
                    elif 3 :
                        #instancie le sort offensif Crache Limace avec 5 points de dégâts
                        SortOffensif('Crache Limace', 5)
                        SortOffensif.append(sorts)
                        break
                    else:
                        print("Mauvaise saisie, veuillez recommencer.")
             
        #Teste si le numero du tour est 2 ou 3,8,11 etc c’est-à-dire si numero%3=2 -> Dans ce cas le sorcier 1 doit lancer un sort sournois
    elif numero%3=2 :
            while(True):
                print('Choisir un sort sournois: 1 pour Legilimens, 2 pour Morsmordre, 3 pour Oubliette : ')
                if 1 : 
                       #instancie le sort sournois Legilimens avec 5 points de dégâts
                       #ajoute le sort à la liste sorts
                       break
                    elif 2 : 
                       #instancie le sort sournois Morsmordre avec 3 points de dégâts
                       #ajoute le sort à la liste sorts
                       break
                    elif 3 : instancie le sort sournois Oubliettes avec 4 points de dégâts
                       #ajoute le sort à la liste sorts
                       break
                    #autre saisie : affiche « Mauvaise saisie, veuillez recommencer »
           
       # Teste si le numero du tour est 3 ou 6,9,12 etc c’est-à-dire si numero%3=0 -> Dans ce cas le sorcier 1 doit lancer un sort défensif
        elif numero%3=0 :
            while(True):
                #demande de saisie utilisateur avec le message : Choisir un sort défensif : 1 pour Expelliarmus, 2 pour Protego, 3 pour Spero Patronum :
                #Cas où la saisie est :
                    #1 : 
                       #instancie le sort défensif Expelliarmus avec 5 points de dégâts
                       #ajoute le sort à la liste sorts
                       break
                    #2 : 
                       #instancie le sort défensif Protego avec 3 points de dégâts
                       #ajoute le sort à la liste sorts
                       break
                    #3 : instancie le sort défensif Spero Patronum avec 4 points de dégâts
                       #ajoute le sort à la liste sorts
                       break
                    #autre saisie : affiche « Mauvaise saisie »
          
        #le sorcier 1 lance le sort choisi
    

    def tourSorcier2(self):
     #instructions similaires à tourSorcier1() mais pour le sorcier 2, attention les types de sort diffèrent du sorcier 1 pour le même numéro de tour cf. Règles de combat: Ex: au tour 1 le sorcier 1 lance un sort offensif et le sorcier 2 répond par un sort défensif, etc     

    def calculerPDV(self):

        #Type du sort lancé par le sorcier 1
        #Type du sort lancé par le sorcier 1
            
        # Test du cas d'un sort offensif contré par un sort défensif
        if(#condition types de sorts):
            #points de dégât du sort du sorcier 1
            #application des points de dégâts sur la jauge de pdv du sorcier 2, appel de perdrePDV()

            #points de récupération du sort du sorcier2
            #application des points de récupération sur la jauge du sorcier 2, appel de recupererPDV()
        
        # test du cas d'un sort sournois contré par un sort offensif
        elif(#condition types de sorts):

            #point de dégâts du sort du sorcier 1
            #application des point de dégâts sur la jauge du sorcier 2, appel de perdrePDV()

            #points de dégâts du sort du sorcier 2
            #application des points de dégâts sur la jauge du sorcier 1, appel de perdrePDV()

        
        # Test du cas d'un sort défensif contré par un sort sournois
        elif(#condition types de sorts):
              
            #points de récupération du sort du sorcier 1
            #application des points de récupération sur la jauge du sorcier 1, appel de recupererPDV()

            #points de dégats du sort du sorcier 2
            #application des points de dégâts sur la jauge du sorcier 1, appel de perdrePDV()
        

         #enregistrement des points de vie de chaque sorcier dans le tableau de score en fin de tour      
    

    def afficherScoreTour(self):
        #affichage du score en fin de tour
    

    def afficherResumeTour(self):
        #affiche : # Tour [Numero du Tour] #
        #appel de afficherScoreTour()