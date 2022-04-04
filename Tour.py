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
    def __init__(self, numero, sorcier1, sorcier2):
        self.__numero = numero
        self.__sorciers = [sorcier1, sorcier2]
        self.__scores = [0, 0]
        print("Tour", numero)
        self.__sorts = []
                      
    def getNumero(self):
        return self.__numero
    
    def getScore(self):
        return self.__scores
    
    def getSorciers(self):
        return self.__sorciers

    def tourSorcier1(self):
        print("-", self.__sorciers[0].getNom(), " : ")
        if self.__numero%3 == 1:
            while(True):
                saisiesorcier1 = input('Choisir un sort offensif : 1 pour Flipendo, 2 pour Impedimenta, 3 pour Crache limace : ')
                if saisiesorcier1 == "1":
                    choixsort = SortOffensif('Flipendo', 4)
                    self.__sorts.append(choixsort)
                    break
                elif saisiesorcier1 == "2":
                    choixsort = SortOffensif('Impedimenta', 5)
                    self.__sorts.append(choixsort)
                    break
                elif saisiesorcier1 == "3":
                    choixsort = SortOffensif('Crache Limace', 5)
                    self.__sorts.append(choixsort)
                    break
                else:
                    print("Mauvaise saisie, veuillez recommencer.")
        elif self.__numero%3 == 2:
            while(True):
                saisiesorcier1 = input('Choisir un sort sournois : 1 pour Legilimens, 2 pour Morsmordre, 3 pour Oubliettes : ')
                if saisiesorcier1 == "1":
                    choixsort = SortSournois('Legilimens', 5)
                    self.__sorts.append(choixsort)
                    break
                elif saisiesorcier1 == "2":
                    choixsort = SortSournois('Morsmordre', 3)
                    self.__sorts.append(choixsort)
                    break
                elif saisiesorcier1 == "3":
                    choixsort = SortSournois('Oubliettes', 4)
                    self.__sorts.append(choixsort)
                    break
                else:
                    print("Mauvaise saisie, veuillez recommencer") 
        elif self.__numero%3 == 0:
            while(True):
                saisiesorcier1 = input("Choisir un sort défensif : 1 pour Expelliarmus, 2 pour Protego, 3 pour Spero Patronum : ")
                if saisiesorcier1 == "1":
                    choixsort = SortDefensif('Expelliarmus', 5)
                    self.__sorts.append(choixsort)
                    break
                elif saisiesorcier1 == "2":
                    choixsort = SortDefensif('Protego', 3)
                    self.__sorts.append(choixsort)
                    break
                elif saisiesorcier1 == "3":
                    choixsort = SortDefensif('Spero Patronum', 4)
                    self.__sorts.append(choixsort)
                    break
                else:
                    print("Mauvaise saisie.")

        self.__sorciers[0].lancerSort(choixsort)

    def tourSorcier2(self):
        print("-", self.__sorciers[1].getNom(), " : ")
        if self.__numero%3 == 1:
            while(True):
                saisiesorcier2 = input("Choisir un sort défensif : 1 pour Expelliarmus, 2 pour Protego, 3 pour Spero Patronum : ")
                if saisiesorcier2 == "1":
                    choixsort = SortDefensif('Expelliarmus', 5)
                    self.__sorts.append(choixsort)
                    break
                elif saisiesorcier2 == "2":
                    choixsort = SortDefensif('Protego', 3)
                    self.__sorts.append(choixsort)
                    break
                elif saisiesorcier2 == "3":
                    choixsort = SortDefensif('Spero Patronum', 4)
                    self.__sorts.append(choixsort)
                    break
                else:
                    print("Mauvaise saisie.")
        elif self.__numero%3 == 2:
            while(True):
                saisiesorcier2 = input('Choisir un sort offensif : 1 pour Flipendo, 2 pour Impedimenta, 3 pour Crache limace : ')
                if saisiesorcier2 == "1":
                    choixsort = SortOffensif('Flipendo', 4)
                    self.__sorts.append(choixsort)
                    break
                elif saisiesorcier2 == "2":
                    choixsort = SortOffensif('Impedimenta', 5)
                    self.__sorts.append(choixsort)
                    break
                elif saisiesorcier2 == "3":
                    choixsort = SortOffensif('Crache Limace', 5)
                    self.__sorts.append(choixsort)
                    break
                else:
                    print("Mauvaise saisie, veuillez recommencer.")
        elif self.__numero%3 == 0:
            while(True):
                saisiesorcier2 = input('Choisir un sort sournois : 1 pour Legilimens, 2 pour Morsmordre, 3 pour Oubliettes : ')
                if saisiesorcier2 == "1":
                    choixsort = SortSournois('Legilimens', 5)
                    self.__sorts.append(choixsort)
                    break
                elif saisiesorcier2 == "2":
                    choixsort = SortSournois('Morsmordre', 3)
                    self.__sorts.append(choixsort)
                    break
                elif saisiesorcier2 == "3":
                    choixsort = SortSournois('Oubliettes', 4)
                    self.__sorts.append(choixsort)
                    break
                else:
                    print("Mauvaise saisie, veuillez recommencer")

        self.__sorciers[1].lancerSort(choixsort)

    def calculerPDV(self):
        type1 = self.__sorts[0].getType()
        type2 = self.__sorts[1].getType()

        if type1 == 'offensif':
            if self.__sorts[0].getNom() == "Flipendo":
                pointsperdus = self.__sorts[0].getPDD()
            elif self.__sorts[0].getNom() == "Impedimenta":
                pointsperdus = self.__sorts[0].getPDD()
            elif self.__sorts[0].getNom() == "Crache Limace":
                pointsperdus = self.__sorts[0].getPDD()
            self.__sorciers[1].perdrePDV(pointsperdus)

        if type2 == 'défensif':
            if self.__sorts[1].getNom() == "Expelliarmus":
                pointsrecup = self.__sorts[1].getPDR()
            elif self.__sorts[1].getNom() == "Protego":
                pointsrecup = self.__sorts[1].getPDR()
            elif self.__sorts[1].getNom() == "Spero Patronum":
                pointsrecup = self.__sorts[1].getPDR()
            self.__sorciers[1].recupererPDV(pointsrecup)
        
        if type1 == 'sournois':
            if self.__sorts[0].getNom() == "Legilimens":
                pointsperdus = self.__sorts[0].getPDD()
            elif self.__sorts[0].getNom() == "Morsmordre":
                pointsperdus = self.__sorts[0].getPDD()
            elif self.__sorts[0].getNom() == "Oubliettes":
                pointsperdus = self.__sorts[0].getPDD()
            self.__sorciers[1].perdrePDV(pointsperdus)

        if type2 == 'offensif':
            if self.__sorts[1].getNom() == "Flipendo":
                pointsperdus = self.__sorts[1].getPDD()
            elif self.__sorts[1].getNom() == "Impedimenta":
                pointsperdus = self.__sorts[1].getPDD()
            elif self.__sorts[1].getNom() == "Crache Limace":
                pointsperdus = self.__sorts[1].getPDD()
            self.__sorciers[0].perdrePDV(pointsperdus)

        if type1 == 'défensif':
            if self.__sorts[0].getNom() == "Expelliarmus":
                pointsrecup = self.__sorts[0].getPDR()
            elif self.__sorts[0].getNom() == "Protego":
                pointsrecup = self.__sorts[0].getPDR()
            elif self.__sorts[0].getNom() == "Spero Patronum":
                pointsrecup = self.__sorts[0].getPDR()
            self.__sorciers[0].recupererPDV(pointsrecup)

        if type2 == 'sournois':
            if self.__sorts[1].getNom() == "Legilimens":
                pointsperdus = self.__sorts[1].getPDD()
            elif self.__sorts[1].getNom() == "Morsmordre":
                pointsperdus = self.__sorts[1].getPDD()
            elif self.__sorts[1].getNom() == "Oubliettes":
                pointsperdus = self.__sorts[1].getPDD()
            self.__sorciers[0].perdrePDV(pointsperdus)

        score1 = self.__sorciers[0].getPDV()
        score2 = self.__sorciers[1].getPDV()
        if score1 < 0:
            score1 = 0
        if score2 < 0:
            score2 = 0
        self.__scores = [score1, score2]
    

    def afficherScoreTour(self):
        print('Le score du Tour est :')
        print(self.getScore())

    def afficherResumeTour(self):
        print('Tour', self.getNumero())
        print('Le sorcier', self.__sorciers[0].getNom(), "a lancé", self.__sorts[0].getNom())
        print('Le sorcier', self.__sorciers[1].getNom(), "a lancé", self.__sorts[1].getNom())
        self.afficherScoreTour()