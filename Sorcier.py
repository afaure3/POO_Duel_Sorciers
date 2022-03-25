#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 12:08:33 2022

@author: pthuringer
"""

from Sort import Sort

class Sorcier :


    def __init__(self,nom):
        self.nom = nom
     
    def getNom(self):
        return self.nom
        #retourne le nom du sorcier
        

    def getPDV(self):
        return self.pdv
        #retourne les points de vie du sorcier 
    
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
        self.pdv = self.pdv + self.nbPDv
        #if Sort.getType(self) == "Sort défensif":
            #if Sort.getType(self) == "Expelliarmus":
                #self.nbPdv = self.nbPdv + 5
            #elif Sort.getType(self) == "Protego":
                #self.nbPdv = self.nbPdv + 3
            #elif Sort.getType(self) == "Spero Patronum":
                #self.nbPdv = self.nbPdv + 4
    
    def perdrePDV(self,nbPdv):
        #enlève nbPdv points à la jauge de points de vie du sorcier
        #self.nbPdv = Sort.getPDV(self)
        self.pdv = self.pdv - self.nbPDV
        #if Sort.getType(self) == "Sort offensif":
            #if Sort.getType(self) == "Impedimenta":
                #self.nbPdv = self.nbPdv - 5
            #elif Sort.getType(self) == "Crache Limace":
                #self.nbPdv = self.nbPdv - 5
            #elif Sort.getType(self) == "Flipendo":
                #self.nbPdv = self.nbPdv - 4
        #if Sort.getType(self) == "Sort sournois":
            #if Sort.getType(self) == "Legilimens" :
               #self.nbPdv = self.nbPdv - 5
            #elif Sort.getType(self) =="Morsmordre":
                #self.nbPdv = self.nbPdv - 3
            #elif Sort.getType(self) =="Oubliettes":
                #self.nbPdv = self.nbPdv - 4