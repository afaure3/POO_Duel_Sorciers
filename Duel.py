#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 12:29:21 2022

@author: pthuringer
"""


from Tour import Tour

class Duel:

    def __init__(self,sorcier1, sorcier2):
        self.__sorcier1 = sorcier1
        self.__sorcier2 = sorcier2
        self.__sorcier1.setPDV(5)
        self.__sorcier2.setPDV(5)
        self.__tourCourant = Tour(1, sorcier1, sorcier2)
        self.__tours = [self.__tourCourant]
        self.__etat = "en cours"
    
    def getTourCourant(self):
        return self.__tourCourant
    
    def getEtat(self):
        return self.__etat
    
    def setEtat(self, etat):
        self.__etat = etat
        
     
    def tourSuivant(self):
        numeroSuivant = self.__tourCourant.getNumero() + 1
        tourSuivant = Tour(numeroSuivant, self.__sorcier1, self.__sorcier2)
        self.__tourCourant = tourSuivant
        self.__tours.append(self.__tourCourant)
    
    def determinerVainqueur(self):
        self.__tourCourant.getScore()
        if self.__tourCourant.scores[0] == 0 and self.__tourCourant.scores[1] > 0:
            print("le sorcier 2 gagne le duel !")
        elif self.__tourCourant.scores[1] == 0 and self.__tourCourant.scores[0] > 0:
            print("Le sorcier 1 a gagné le duel !")
        elif self.__tourCourant.scores[0] == 0 and self.__tourCourant.scores[1] == 0:
            print("Match nul ! Les deux sorciers ont perdu...")

    def afficherResumeDuel(self):
        print('Le duel est terminé. Résumé du duel : ')
        self.__tourCourant.afficherResumeTour()
        self.determinerVainqueur()