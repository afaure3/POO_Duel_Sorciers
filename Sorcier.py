#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 12:08:33 2022

@author: pthuringer
"""

from Sort import Sort

class Sorcier :


    def __init__(self,nom, pdv):
        self.nom = print("Entrer le nom du sorcier : ")
        self.pdv = 5
     
    def getNom(self):
        print("Le sorcier s'appelle " + self.nom + ".")
        return self.nom
        #retourne le nom du sorcier
        

    def getPDV(self):
        print("Le sorcier a " + self.PDV +" points de vie." )
        return self.PDV
    
    def setPDV(self,pdv):
        #modifie le nombre de points de vie du sorcier
        self.setPDV = self.pdv - self.pdd or + self.pdr
    
    def lancerSort(self,sort):
        if Sort.getType(self) == "offensif" or "sournois" : 
            print((self.nom) + "lance le sort " + (Sort.getNom(self)) + " de type " + (Sort.getType(self)) + " avec " (Sort.getPDD(self)) + " points de dégats.")
        else:
            print((self.nom) + "lance le sort " + (Sort.getNom(self)) + " de type " + (Sort.getType(self)) + " avec " (Sort.getPDR(self)) + " points de récupération.")
		#affiche : [nom du sorcier] lance le sort [nom du sort] de type [type du sort]
        #si le sort est de type offensif ou sournois, affiche : avec [nombre de points de dégâts du sort] points de dégât
        #sinon si le sort est de type défensif, affiche : avec [nombre de points de récupération] points de récupération

    def recupererPDV(self,nbPdv):
       #ajoute nbPdv points à la jauge de points de vie du sorcier
       self.nbPdv = Sort.getPDR(self)
       self.PDV = + self.nbPDV 
       
    
    def perdrePDV(self,nbPdv): 
       #enlève nbPdv points à la jauge de points de vie du sorcier
       self.nbPdv = Sort.getPDV(self)
       self.PDV = - self.nbPDV 