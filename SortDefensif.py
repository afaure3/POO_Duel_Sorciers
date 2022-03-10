#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 12:16:39 2022

@author: pthuringer
"""
from Sort import Sort

class SortDefensif(Sort):
    def __init__(self,nom, pdr):
        Sort.__init__(self)
        self.dégats = 2 # à voir quand on sera plus loin si plus complexe ou pris en charge par un autre fichier + pas sûr du nombre de dégats 
