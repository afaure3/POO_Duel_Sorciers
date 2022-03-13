#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 12:15:24 2022

@author: pthuringer
"""
from Sort import Sort

class SortOffensif(Sort):
    def __init__(self,nom, pdd):
        Sort.__init__(self)
        self.degats = 2    # à voir quand on sera plus loin si plus complexe ou pris en charge par un autre fichier

class SortOffensif(Sort):
    def __init__(self,nom, pdd):
        Sort.__init__(self)
        self._nom = "Sort offensif"
        self._type = "offensif"
        self._pdd = 3
