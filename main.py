#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 11:52:05 2022

@author: pthuringer
"""

from Sorcier import Sorcier
from Duel import Duel

    #main.py : programme principal
def main():
    nom1=input("Veuillez saisir le nom du sorcier 1 : ")
    #Instanciation du premier sorcier
    sorcier1 =  Sorcier(nom1)

    nom2=input("Veuillez saisir le nom du sorcier 2 : ")
    #Instanciation du second sorcier
    sorcier2 = Sorcier(nom2)

    print("\nLe duel peut commencer\n")
    #Instanciation du duel
    duel=Duel(sorcier1, sorcier2)

    #tant que le duel est en cours
    while duel.getEtat()=="en cours":
        #le sorcier 1 choisit un sort et le lance
        duel.getTourCourant().tourSorcier1()
        #le sorcier 2 choisit un sort et le lance
        duel.getTourCourant().tourSorcier2()
        #recalcul des points de vie
        duel.getTourCourant().calculerPDV()
        #affichage du score
        duel.getTourCourant().afficherScoreTour()
       
        score=duel.getTourCourant().getScore()
        #si le nombre de points de vie de chaque sorciers est strictement supérieur à 0
        if score[0]>0 and score[1]>0:
            #le duel continue on passe au tour suivant
            duel.tourSuivant()
        #sinon
        else:
            #le duel se termine
            duel.setEtat("terminé")
            #on affiche le résumé
            duel.afficherResumeDuel()
        
main()
