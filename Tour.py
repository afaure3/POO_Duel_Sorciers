#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 12:18:28 2022

@author: pthuringer
"""

from SortOffensif import SortOffensif
from SortDefensif import SortDefensif
from SortSournois import SortSournois
from Sort import Sort
from Sorcier import Sorcier

class Tour:
    def __init__(self, numero, sorcier1, sorcier2, score):
        self.numero = 1
        self.sorcier = [sorcier1, sorcier2]
        self.sorcier1 = sorcier1
        self.sorcier2 = sorcier2
        self.score = [[sorcier1.pdv],[sorcier2.pdv]]
        print("Tour", numero)
        self.sorts = [] #à revoir -> demande d'un tableau à double dimension
    def getNumero(self):
        return Tour.numero
    
    def getScore(self):
        return self.score
    
    def getSorciers(self):
        return self.sorcier

    def tourSorcier1(self):
        print("-", self.sorcier1, " : ")
        if self.numero%3 == 1 :
            while(True):
                saisiesorcier1 = input('Choisir un sort offensif : 1 pour Flipendo, 2 pour Impedimenta, 3 pour Crache limace : ')
                if saisiesorcier1 == "1" :
                    SortOffensif('Flipendo', 4, 0)
                    self.sorts.append(SortOffensif)
                    break
                elif saisiesorcier1 == "2" :
                    SortOffensif('Impedimenta', 5, 0)
                    self.sorts.append(SortOffensif)
                    break
                elif saisiesorcier1 == "3" :
                    SortOffensif('Crache Limace', 5, 0)
                    self.sorts.append(SortOffensif)
                    break
                else:
                    print("Mauvaise saisie, veuillez recommencer.")
        elif self.numero%3 == 2 :
            while(True):
                saisiesorcier1 = input('Choisir un sort sournois : 1 pour Legilimens, 2 pour Morsmordre, 3 pour Oubliettes : ')
                if saisiesorcier1 == "1" : 
                    SortSournois('Legilimens', 5, 0)
                    self.sorts.append(SortSournois)
                    break
                elif saisiesorcier1 == "2" :
                    SortSournois('Morsmordre', 3, 0)
                    self.sorts.append(SortSournois)
                    break
                elif saisiesorcier1 == "3" :
                    SortSournois('Oubliettes', 4, 0)
                    self.sorts.append(SortSournois)
                    break
                else:
                    print("Mauvaise saisie, veuillez recommencer") 
        elif self.numero%3 == 0 :
            while(True):
                saisiesorcier1 = input("Choisir un sort défensif : 1 pour Expelliarmus, 2 pour Protego, 3 pour Spero Patronum : ")
                if saisiesorcier1 == "1" :
                    SortDefensif('Expelliarmus', 5, 0)
                    self.sorts.append(SortDefensif)
                    break
                elif saisiesorcier1 == "2" :
                    SortDefensif('Protego', 3, 0)
                    self.sorts.append(SortDefensif)
                    break
                elif saisiesorcier1 == "3" :
                    SortDefensif('Spero Patronum', 4, 0)
                    self.sorts.append(SortDefensif)
                    break
                else:
                    print("Mauvaise saisie.")

    def tourSorcier2(self):
        print("-", self.sorcier2, " : ")
        if self.numero%3 == 1 :
            while(True):
                saisiesorcier2 = input("Choisir un sort défensif : 1 pour Expelliarmus, 2 pour Protego, 3 pour Spero Patronum : ")
                if saisiesorcier2 == "1" :
                    SortDefensif('Expelliarmus', 5, 0)
                    self.sorts.append(SortDefensif)
                    break
                elif saisiesorcier2 == "2" :
                    SortDefensif('Protego', 3, 0)
                    self.sorts.append(SortDefensif)
                    break
                elif saisiesorcier2 == "3" :
                    SortDefensif('Spero Patronum', 4, 0)
                    self.sorts.append(SortDefensif)
                    break
                else:
                    print("Mauvaise saisie.")
        elif self.numero%3 == 2 :
            while(True):
                saisiesorcier2 = input('Choisir un sort offensif : 1 pour Flipendo, 2 pour Impedimenta, 3 pour Crache limace : ')
                if saisiesorcier2 == "1" :
                    SortOffensif('Flipendo', 4, 0)
                    self.sorts.append(SortOffensif)
                    break
                elif saisiesorcier2 == "2" :
                    SortOffensif('Impedimenta', 5, 0)
                    self.sorts.append(SortOffensif)
                    break
                elif saisiesorcier2 == "3" :
                    SortOffensif('Crache Limace', 5, 0)
                    self.sorts.append(SortOffensif)
                    break
                else:
                    print("Mauvaise saisie, veuillez recommencer.")
        elif self.numero%3 == 0 :
            while(True):
                saisiesorcier2 = input('Choisir un sort sournois : 1 pour Legilimens, 2 pour Morsmordre, 3 pour Oubliettes : ')
                if saisiesorcier2 == "1" :
                    SortSournois('Legilimens', 5, 0)
                    self.sorts.append(SortSournois)
                    break
                elif saisiesorcier2 == "2" :
                    SortSournois('Morsmordre', 3, 0)
                    self.sorts.append(SortSournois)
                    break
                elif saisiesorcier2 == "3" :
                    SortSournois('Oubliettes', 4, 0)
                    self.sorts.append(SortSournois)
                    break
                else:
                    print("Mauvaise saisie, veuillez recommencer")

    def calculerPDV(self):
        Sort.type1 = Tour.tourSorcier1
        Sort.type2 = Tour.tourSorcier2
            
        if Sort.type1 == 'offensif' and Sort.type2 == 'défensif':
            if 1:
                SortOffensif.pdd = 4
            elif 2 or 3:
                SortOffensif.pdd = 5
            else:
                print("error ¯\_(ツ)_/¯")
            Sorcier.perdrePDV(self.sorcier1)

            if  1:
                SortDefensif.pdr = 5
            elif 2:
                SortDefensif.pdr = 3
            elif 3:
                SortDefensif.pdr = 4
            else:
                print("error ¯\_(ツ)_/¯")
            Sorcier.recupererPDV(self.sorcier2)
        
        elif Sort.type1 == 'sournois' and Sort.type2 == 'offensif':
            if 1:
                SortSournois.pdd = 5
            elif 2:
                SortSournois.pdd = 3
            elif 3:
                SortSournois.pdd = 4
            else:
                print("error ¯\_(ツ)_/¯")
            Sorcier.perdrePDV(self.sorcier1)

            if 1:
                SortOffensif.pdd = 4
            elif 2 or 3:
                SortOffensif.pdd = 5
            else:
                print("error ¯\_(ツ)_/¯")
            Sorcier.perdrePDV(self.sorcier2)

        elif Sort.type1 == 'défensif' and Sort.type2 == 'sournois':
            if 1:
                SortDefensif.pdr = 5
            elif 2:
                SortDefensif.pdr = 3
            elif 3:
                SortDefensif.pdr = 4
            else:
                print("error ¯\_(ツ)_/¯")
            Sorcier.recupererPDV(self.sorcier1)

            if 1:
                SortSournois.pdd = 5
            elif 2:
                SortSournois.pdd = 3
            elif 3:
                SortSournois.pdd = 4
            else:
                print("error ¯\_(ツ)_/¯")
            Sorcier.perdrePDV(self.sorcier2)
        
        self.score.append(self.sorcier)
    

    def afficherScoreTour(self):
        print(Tour.getScore(self))

    def afficherResumeTour(self):
        print('Tour' + self.numero)
        Tour.afficherScoreTour(self)