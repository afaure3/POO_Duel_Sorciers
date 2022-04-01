#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 12:29:21 2022

@author: pthuringer
"""


from Tour import Tour

class Duel:

    def __init__(self,sorcier1, sorcier2):
        #initialisation du sorcier 1
        self.sorcier1 = sorcier1
        #initialisation du sorcier 2
        self.sorcier2 = sorcier2
        #initialisation des points de vie du sorcier 1 à 5
        self.sorcier1.setPDV(5)
        #initialisation des points de vie du sorcier 2 à 5
        self.sorcier2.setPDV(5)
        #initialisation de tourCourant avec la création d’une instance de Tour
        self.tourCourant = Tour(1, sorcier1, sorcier2)
        #initialisation du premier élément du tableau tours avec le tour courant
        self.tours = [self.tourCourant]
        #initialisation de l’état du seul à « en cours »
        self.etat = "en cours"
    
    def getTourCourant(self):
        return self.tourCourant
        #retourne le tour courant du duel
    
    def getEtat(self):
        return self.etat
       #retourne l’état du duel
    
    def setEtat(self, etat):
        #modifie l’état du duel
        self.etat = etat
        
     
    def tourSuivant(self):
        #calcule le numero du tour suivant à partir du tour courant
        numeroSuivant = self.tourCourant.getNumero() + 1
        #instancie un nouveau Tour avec le numéro suivant
        tourSuivant = Tour(numeroSuivant, self.sorcier1, self.sorcier2)
        #affecte le nouveau tour à tourCourant
        self.tourCourant = tourSuivant
        #ajout du nouveau tour à au tableau tours
        #self.tours[0].numero = self.tourCourant
        self.tours.append(self.tourCourant)
    
    def determinerVainqueur(self):
        #score du tour courant
        Tour.getScore(self)
        #test les valeurs des points de vie stockés dans le score et affiche le résultat (ne pas oublier le match nul)
        if Tour.scores[0] == 0:
            print("le sorcier 2 gagne le duel !")
        elif Tour.scores[1] == 0:
            print("Le sorcier 1 a gagné le duel !")
        elif Tour.scores[0] == 0 and Tour.scores[1] == 0:
            print("Match nul ! Les deux sorciers ont perdu...")

    def afficherResumeDuel(self):
        print('Le duel est terminé. Résumé du duel : ')
        Tour.afficherResumeTour(self)
        Duel.determinerVainqueur(self)
