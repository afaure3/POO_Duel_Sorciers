#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 12:12:55 2022

@author: pthuringer
"""


class Sort:

    def __init__(self,nom, type, pdd, pdr):
        self._nom = nom
        self._pdd = pdd
        self._pdr = pdr
        self._type = type
    
    def getNom(self):
        return self._nom

    def getType(self):
        return self._type
    
    def getPDD(self):
        return self._pdd
    
    def getPDR(self):
        return self._pdr