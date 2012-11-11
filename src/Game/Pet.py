# -*- coding: utf-8 -*-
__author__="Patrik Ahvenainen"
__date__ ="$11.11.2012 20:37:35$"

'''
This module contains the Pet class

Created on Nov 11, 2012
Last Update: Nov 11, 2012

@author: Patrik Ahvenainen
'''

class Pet(object):
    '''
    Pet contains the class definition of a virtual pet
    '''

    # class constants 
    MAX_ATTRIBUTE_VAL = 100
    MIN_ATTRIBUTE_VAL = 0
    DEFAULT_INITIAL_CHANGE = 10
    DEFAULT_STARTING_MASS = 1 # [grams]
    DEFAULT_BIRTH_TEMP = 295 # [Kelvins]
    
    STATUSES = ['awake', 'asleep', 'dead', 'comatose']

    def __init__(self,name,species='snail'):
        '''
        Constructor
        '''
        
        self._name = name
        self._species = species

        self._age = 0 # [years]
        self._discipline = Pet.MIN_ATTRIBUTE_VAL # out of 100
        self._fittness = Pet.MIN_ATTRIBUTE_VAL+Pet.DEFAULT_INITIAL_CHANGE # out of 100        
        self._happiness = Pet.MIN_ATTRIBUTE_VAL+Pet.DEFAULT_INITIAL_CHANGE # out of 100
        self._health = Pet.MAX_ATTRIBUTE_VAL-Pet.DEFAULT_INITIAL_CHANGE # out of 100
        self._hunger = Pet.MAX_ATTRIBUTE_VAL-Pet.DEFAULT_INITIAL_CHANGE # out of 100
        self._hygiene = Pet.MIN_ATTRIBUTE_VAL+Pet.DEFAULT_INITIAL_CHANGE # out of 100
        self._mass = Pet.DEFAULT_STARTING_MASS # [grams]
        self._status = 'awake'
        self._temperature = Pet.DEFAULT_BIRTH_TEMP # [Kelvins]
        self._tiredness = Pet.MAX_ATTRIBUTE_VAL-Pet.DEFAULT_INITIAL_CHANGE # out of 100
        
    @property
    def age(self):
        return self._age        
    @property
    def hygiene(self):
        return self._hygiene        
    @property
    def discipline(self):
        return self._discipline        
    @property
    def fittness(self):
        return self._fittness        
    @property
    def happiness(self):
        return self._happiness
    @property
    def health(self):
        return self._health    
    @property
    def hunger(self):
        return self._hunger
    @property
    def mass(self):
        return self._mass
    @property
    def name(self):
        return self._name
    @property
    def species(self):
        return self._species
    @property
    def status(self):
        return self._status
    @property
    def temperature(self):
        return self._temperature
    @property
    def tiredness(self):
        return self._tiredness

#######################
### Public methods  ###
#######################

    def clean(self):
        '''
        Cleans the pet
        '''
        self._clean()

    def drink(self,mass):
        '''
        drink is given in grams. A quarter of the mass of the drink
        is ingested and used as nutrition, half added as the mass
        of the pet
        '''
        self._increaseMass(mass/4)
        self._updateHunger(mass/4)
        
    def exercise(self, time, effectiveness):
        '''
        Time used to exercise with the pet and the fun effectiveness
        affect the fitness of the pet
        Time is given in seconds (real time) and effectiveness is a coefficient
        (Max 100)
        '''
        fitnessIncrease = time*effectiveness
        self._increaseFitness(fitnessIncrease)
    
    def feed(self,mass):
        '''
        Food is given in grams. Half of the mass of the food
        is ingested and used as nutrition, half added as the mass
        of the pet
        '''
        self._increaseMass(mass/2)
        self._updateHunger(mass/2)
        
    def playWith(self,time,funFactor):
        '''
        Time used to play with the pet and the fun factor
        affect the happiness of the pet
        Time is given in seconds (real time) and funFactor is a coefficient
        that tells how much fun pet is having during play time
        '''
        happinessIncrease = time*funFactor
        self._increaseHappiness(happinessIncrease)

    def study(self,time,effectiveness):
        '''
        Time used to play with the pet and the fun factor
        affect the happiness of the pet
        Time is given in seconds (real time) and effectiveness is a coefficient
        (max 100)
        '''
        disciplineIncrease = time*effectiveness/100
        self._increaseDiscipline(disciplineIncrease)

        
#######################
### Private methods ###
#######################

    def _clean(self):
        '''
        '''
        self._hygiene = Pet.MAX_ATTRIBUTE_VAL
        
    def _increaseDiscipline(self, disciplineIncrease):
        '''
        Time (in real time seconds) used to train discipline
        converts so that 100 seconds sees an increase of 10%
        '''
        self._discipline += disciplineIncrease/10
        if self._discipline > Pet.MAX_ATTRIBUTE_VAL:
            self._discipline = Pet.MAX_ATTRIBUTE_VAL

    def _increaseFitness(self, fitnessIncrease):
        '''
        Time (in real time seconds) used to exercise the pet
        converts so that 100 seconds sees an increase of 10%
        '''
        self._fitness += fitnessIncrease/10
        if self._fitness > Pet.MAX_ATTRIBUTE_VAL:
            self._fitness = Pet.MAX_ATTRIBUTE_VAL

    def _increaseHappiness(self, happinessIncrease):
        '''
        happinessIncrease is a number such that 100 gives maximum
        increase of 100% happiness
        '''
        
        self._happiness += happinessIncrease
        if self._happiness > Pet.MAX_ATTRIBUTE_VAL:
            self._happiness = Pet.MAX_ATTRIBUTE_VAL

    def _increaseMass(self, mass):
        '''
        Mass of nutrition is directly added to the mass of the pet
        '''
        self._weight += mass
    
    def _updateHunger(self, mass):
        '''
        Hunger is decreased relative to body mass
        If ingested nutrition mass is 10% of total body
        mass, pet is no longer hungry
        '''
        relative = 10 * mass / self.weight
        self._hunger -= relative
        if self._hunger < Pet.MIN_ATTRIBUTE_VAL:
            self._hunger = Pet.MIN_ATTRIBUTE_VAL
    