#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 12:17:38 2022

@author: pthuringer
"""

from Sort import Sort

#class SortSournois(Sort):
 #   def __init__(self,nom, pdd):
  #      Sort.__init__(self)
   #     self.degats = 2 # à voir quand on sera plus loin si plus complexe ou pris en charge par un autre fichier

class SortSournois(Sort):
    def __init__(self,nom, pdd):
        Sort.__init__(self)
        self._nom = "Sort sournois"
        self._type = "sournois"
        self._pdd = 2