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
        #initialisation du sorcier 2
        #initialisation des points de vie du sorcier 1 à 5
        #initialisation des points de vie du sorcier 2 à 5
        #initialisation de tourCourant avec la création d’une instance de Tour       
        #initialisation du premier élément du tableau tours avec le tour courant
        #initialisation de l’état du seul à « en cours »
    
    def getTourCourant(self):
        return tourCourant
        #retourne le tour courant du duel
    
    def getEtat(self):
        return self.etat
       #retourne l’état du duel
    
    def setEtat(self,etat):
        self.etat = 
        #modifie l’état du duel
     
    def tourSuivant(self):
        #calcule le numero du tour suivant à partir du tour courant
        #instancie un nouveau Tour avec le numéro suivant
        #affecte le nouveau tour à tourCourant
        #ajout du nouveau tour à au tableau tours
    
    def determinerVainqueur(self):
        #score du tour courant
        #test les valeurs des points de vie stockés dans le score et affiche le résultat (ne pas oublier le match nul)

    def afficherResumeDuel(self):
        #affiche : Le duel est terminé. Résumé du duel :
        #pour chaque tour stocké dans la tableau tours, appelle afficheResumeTour()
        #appelle determinerVainqueur
