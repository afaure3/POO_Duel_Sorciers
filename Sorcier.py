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
        self.pdv = 0
     
    def getNom(self):
        return self.nom

    def getPDV(self):
        return self.pdv
    
    def setPDV(self,pdv):
        self.pdv = pdv
    
    def lancerSort(self, sorts):
        if sorts.getType() == "offensif" or sorts.getType() == "sournois":
            print(self.getNom(), "lance le sort", sorts.getNom(), "de type", sorts.getType(), "avec", sorts.getPDD(), "points de dégats.")
        elif sorts.getType() == "défensif":
            print(self.getNom(), "lance le sort", sorts.getNom(), "de type", sorts.getType(), "avec", sorts.getPDR(), "points de récupération.")

    def recupererPDV(self,nbPdv):
        self.pdv = self.pdv + nbPdv
    
    def perdrePDV(self,nbPdv):
        self.pdv = self.pdv - nbPdv