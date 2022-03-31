#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 12:15:24 2022

@author: pthuringer
"""
from Sort import Sort

class SortOffensif(Sort):
    def __init__(self, nom, pdd):
        Sort.__init__(self, nom, "offensif", pdd, 0)
        self.nom = nom
        self.pdd = pdd