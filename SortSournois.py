#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 12:17:38 2022

@author: pthuringer
"""

from Sort import Sort

class SortSournois(Sort):
    def __init__(self, nom, pdd):
        Sort.__init__(self, nom, "sournois", pdd, 0)
        self.nom = nom
        self.pdd = pdd