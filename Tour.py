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
        self.numero = numero
        self.sorciers = [sorcier1, sorcier2]
        self.scores = [0, 0]
        print("Tour", numero)
        self.sorts = []
                      
    def getNumero(self):
        return self.numero
    
    def getScore(self):
        return self.scores
    
    def getSorciers(self):
        return self.sorciers

    def tourSorcier1(self):
        print("-", self.sorciers[0].getNom(), " : ")
        if self.numero%3 == 1 :
            while(True):
                saisiesorcier1 = input('Choisir un sort offensif : 1 pour Flipendo, 2 pour Impedimenta, 3 pour Crache limace : ')
                if saisiesorcier1 == "1" :
                    sortoffensif = SortOffensif('Flipendo', 4)
                    self.sorts.append(sortoffensif)
                    break
                elif saisiesorcier1 == "2" :
                    sortoffensif = SortOffensif('Impedimenta', 5)
                    self.sorts.append(sortoffensif)
                    break
                elif saisiesorcier1 == "3" :
                    sortoffensif = SortOffensif('Crache Limace', 5)
                    self.sorts.append(sortoffensif)
                    break
                else:
                    print("Mauvaise saisie, veuillez recommencer.")
        elif self.numero%3 == 2 :
            while(True):
                saisiesorcier1 = input('Choisir un sort sournois : 1 pour Legilimens, 2 pour Morsmordre, 3 pour Oubliettes : ')
                if saisiesorcier1 == "1" : 
                    sortsournois = SortSournois('Legilimens', 5)
                    self.sorts.append(sortsournois)
                    break
                elif saisiesorcier1 == "2" :
                    sortsournois = SortSournois('Morsmordre', 3)
                    self.sorts.append(sortsournois)
                    break
                elif saisiesorcier1 == "3" :
                    sortsournois = SortSournois('Oubliettes', 4)
                    self.sorts.append(sortsournois)
                    break
                else:
                    print("Mauvaise saisie, veuillez recommencer") 
        elif self.numero%3 == 0 :
            while(True):
                saisiesorcier1 = input("Choisir un sort défensif : 1 pour Expelliarmus, 2 pour Protego, 3 pour Spero Patronum : ")
                if saisiesorcier1 == "1" :
                    sortdefensif = SortDefensif('Expelliarmus', 5)
                    self.sorts.append(sortdefensif)
                    break
                elif saisiesorcier1 == "2" :
                    sortdefensif = SortDefensif('Protego', 3)
                    self.sorts.append(sortdefensif)
                    break
                elif saisiesorcier1 == "3" :
                    sortdefensif = SortDefensif('Spero Patronum', 4)
                    self.sorts.append(sortdefensif)
                    break
                else:
                    print("Mauvaise saisie.")

    def tourSorcier2(self):
        print("-", self.sorciers[1].getNom(), " : ")
        if self.numero%3 == 1 :
            while(True):
                saisiesorcier2 = input("Choisir un sort défensif : 1 pour Expelliarmus, 2 pour Protego, 3 pour Spero Patronum : ")
                if saisiesorcier2 == "1" :
                    sortdefensif = SortDefensif('Expelliarmus', 5)
                    self.sorts.append(sortdefensif)
                    break
                elif saisiesorcier2 == "2" :
                    sortdefensif = SortDefensif('Protego', 3)
                    self.sorts.append(sortdefensif)
                    break
                elif saisiesorcier2 == "3" :
                    sortdefensif = SortDefensif('Spero Patronum', 4)
                    self.sorts.append(sortdefensif)
                    break
                else:
                    print("Mauvaise saisie.")
        elif self.numero%3 == 2 :
            while(True):
                saisiesorcier2 = input('Choisir un sort offensif : 1 pour Flipendo, 2 pour Impedimenta, 3 pour Crache limace : ')
                if saisiesorcier2 == "1" :
                    sortoffensif = SortOffensif('Flipendo', 4)
                    self.sorts.append(sortoffensif)
                    break
                elif saisiesorcier2 == "2" :
                    sortoffensif = SortOffensif('Impedimenta', 5)
                    self.sorts.append(sortoffensif)
                    break
                elif saisiesorcier2 == "3" :
                    sortoffensif = SortOffensif('Crache Limace', 5)
                    self.sorts.append(sortoffensif)
                    break
                else:
                    print("Mauvaise saisie, veuillez recommencer.")
        elif self.numero%3 == 0 :
            while(True):
                saisiesorcier2 = input('Choisir un sort sournois : 1 pour Legilimens, 2 pour Morsmordre, 3 pour Oubliettes : ')
                if saisiesorcier2 == "1" :
                    sortsournois = SortSournois('Legilimens', 5)
                    self.sorts.append(sortsournois)
                    break
                elif saisiesorcier2 == "2" :
                    sortsournois = SortSournois('Morsmordre', 3)
                    self.sorts.append(sortsournois)
                    break
                elif saisiesorcier2 == "3" :
                    sortsournois = SortSournois('Oubliettes', 4)
                    self.sorts.append(sortsournois)
                    break
                else:
                    print("Mauvaise saisie, veuillez recommencer")

    def calculerPDV(self):
        type1 = self.sorts[0].getType()
        type2 = self.sorts[1].getType()

        if type1 == 'offensif' and type2 == 'défensif':
            if 1:
                pointsperdus = self.sorts[0].getPDD()
            elif 2 or 3:
                pointsperdus = self.sorts[0].getPDD()
            self.sorciers[1].perdrePDV(pointsperdus)

            if 1:
                pointsrecup = self.sorts[1].getPDR()
            elif 2:
                pointsrecup = self.sorts[1].getPDR()
            elif 3:
                pointsrecup = self.sorts[1].getPDR()
            self.sorciers[1].recupererPDV(pointsrecup)
        
        elif type1 == 'sournois' and type2 == 'offensif':
            if 1:
                pointsperdus = self.sorts[0].getPDD()
            elif 2:
                pointsperdus = self.sorts[0].getPDD()
            elif 3:
                pointsperdus = self.sorts[0].getPDD()
            self.sorciers[1].perdrePDV(pointsperdus)

            if 1:
                pointsperdus = self.sorts[1].getPDD()
            elif 2 or 3:
                pointsperdus = self.sorts[1].getPDD()
            self.sorciers[0].perdrePDV(pointsperdus)

        elif type1 == 'défensif' and type2 == 'sournois':
            if 1:
                pointsrecup = self.sorts[0].getPDR()
            elif 2:
                pointsrecup = self.sorts[0].getPDR()
            elif 3:
                pointsrecup = self.sorts[0].getPDR()
            self.sorciers[0].recupererPDV(pointsrecup)

            if 1:
                pointsperdus = self.sorts[1].getPDD()
            elif 2:
                pointsperdus = self.sorts[1].getPDD()
            elif 3:
                pointsperdus = self.sorts[1].getPDD()
            self.sorciers[0].perdrePDV(pointsperdus)

        score1 = self.sorciers[0].getPDV()
        score2 = self.sorciers[1].getPDV()
        self.scores = [score1, score2]
    

    def afficherScoreTour(self):
        print(Tour.getScore(self))

    def afficherResumeTour(self):
        print('Tour', self.numero)
        self.afficherScoreTour()