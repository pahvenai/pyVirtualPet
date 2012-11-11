# -*- coding: utf-8 -*-
__author__="Patrik Ahvenainen"
__date__ ="$11.11.2012 23:09:11$"

'''
This module contains class Game which is intended to be the only class 
from the package of the same name that communicates with GUI. This is 
the interface to GUI.

Created on Nov 11, 2012
Last update: Nov 11, 2012

@author: Patrik Ahvenainen
'''

from Pet import Pet

class Game(object):
    '''
    Contains handles for all parts of the game.
    '''


    def __init__(self,pets=[],activePet=0):
        '''
        Create a new game. Must have at least one pet.
        '''
        
        self._pets = pets
        self.activePet = activePet
        
    def addPet(self,name,species='snail'):
        self._pets.append(Pet(name,species))
        
    @property
    def NofPets(self):
        return len(self._pets)        
    @property
    def pet(self,index=-1):
        if index < 0:
            return self._pets[self.activePet]