#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 12:08:33 2022

@author: pthuringer
"""


class Sorcier :


    def __init__(self,nom):
        #self.nom1 = print("Entrez le nom du premier sorcier : ")
        #self.nom2 = print("Entrez le nom du deuxième sorcier : ")
        self.nom = print("Entrer le nom du sorcier : ")
     
    def getNom(self):
        print("Le sorcier s'appelle " + self.nom)  #retourne le nom du sorcier
        

    def getPDV(self):
        #self.PDV1 = 5
        #self.PDV2 = 5
        self.PDV = 5
    
    def setPDV(self,pdv):
        #modifie le nombre de points de vie du sorcier
    
    def lancerSort(self,sort):
        
		#affiche : [nom du sorcier] lance le sort [nom du sort] de type [type du sort]
        #si le sort est de type offensif ou sournois, affiche : avec [nombre de points de dégâts du sort] points de dégât
        #sinon si le sort est de type défensif, affiche : avec [nombre de points de récupération] points de récupération

    def recupererPDV(self,nbPdv):
       #ajoute nbPdv points à la jauge de points de vie du sorcier
    
    def perdrePDV(self,nbPdv):
       #enlève nbPdv points à la jauge de points de vie du sorcier