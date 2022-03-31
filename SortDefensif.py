#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 12:16:39 2022

@author: pthuringer
"""
from Sort import Sort

class SortDefensif(Sort):
    def __init__(self, nom, pdr):
        Sort.__init__(self, nom, "défensif", pdr, 0)
        self.nom = nom
        self.pdr = pdr