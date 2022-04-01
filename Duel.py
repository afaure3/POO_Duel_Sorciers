#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 12:29:21 2022

@author: pthuringer
"""


from Tour import Tour

class Duel:

    def __init__(self,sorcier1, sorcier2):
        self.sorcier1 = sorcier1
        self.sorcier2 = sorcier2
        self.sorcier1.setPDV(5)
        self.sorcier2.setPDV(5)
        self.tourCourant = Tour(1, sorcier1, sorcier2)
        self.tours = [self.tourCourant]
        self.etat = "en cours"
    
    def getTourCourant(self):
        return self.tourCourant
    
    def getEtat(self):
        return self.etat
    
    def setEtat(self, etat):
        self.etat = etat
        
     
    def tourSuivant(self):
        numeroSuivant = self.tourCourant.getNumero() + 1
        tourSuivant = Tour(numeroSuivant, self.sorcier1, self.sorcier2)
        self.tourCourant = tourSuivant
        self.tours.append(self.tourCourant)
    
    def determinerVainqueur(self):
        Tour.getScore(self)
        if Tour.scores[0] == 0:
            print("le sorcier 2 gagne le duel !")
        elif Tour.scores[1] == 0:
            print("Le sorcier 1 a gagné le duel !")
        elif Tour.scores[0] == 0 and Tour.scores[1] == 0:
            print("Match nul ! Les deux sorciers ont perdu...")

    def afficherResumeDuel(self):
        print('Le duel est terminé. Résumé du duel : ')
        Tour.afficherResumeTour(self)
        self.determinerVainqueur()