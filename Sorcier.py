#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 12:08:33 2022

@author: pthuringer
"""

from Sort import Sort

class Sorcier :


    def __init__(self,nom,pdv):
        self.nom = nom
        self.pdv = pdv
     
    def getNom(self):
        return self.nom
        #retourne le nom du sorcier
        

    def getPDV(self):
        return self.pdv
        #retourne les points de vie du sorcier 
    
    def setPDV(self,pdv):
        #modifie le nombre de points de vie du sorcier
        self.pdv = self.nbPdv
    
    def lancerSort(self,sort):
        if Sort.getType(self) == "offensif" or Sort.getType(self) == "sournois" : 
            print(self.nom, "lance le sort ", Sort.getNom(self), " de type ", Sort.getType(self), " avec ", Sort.getPDD(self), " points de dégats.")
        elif Sort.getType(self) == "défensif" :
            print(self.nom, "lance le sort ", Sort.getNom(self), " de type ", Sort.getType(self), " avec ", Sort.getPDR(self), " points de récupération.")
        else:
            print("error ¯\_(ツ)_/¯")
		#affiche : [nom du sorcier] lance le sort [nom du sort] de type [type du sort]
        #si le sort est de type offensif ou sournois, affiche : avec [nombre de points de dégâts du sort] points de dégât
        #sinon si le sort est de type défensif, affiche : avec [nombre de points de récupération] points de récupération

    def recupererPDV(self,nbPdv):
        #ajoute nbPdv points à la jauge de points de vie du sorcier
        self.nbPDV = self.pdv + self.pdr
    
    def perdrePDV(self,nbPdv):
        #enlève nbPdv points à la jauge de points de vie du sorcier
        self.nbPdv = self.pdv - self.pdd