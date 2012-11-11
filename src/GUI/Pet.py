# -*- coding: utf-8 -*-
__author__="Patrik Ahvenainen"
__date__ ="$12.11.2012 00:03:45$"

'''
Created on Nov 12, 2012

@author: Patrik Ahvenainen
'''

import Tkinter as T

class Pet(T.Frame):
    '''
    This class handles drawing a single pet on master.
    All items are contained within a single Frame.
    '''

    WIDTH_OF_PIC = 400

    def __init__(self,master, pet=''):
        '''
        master should be root
        '''
        self.master = master
        T.Frame.__init__(self, master)
        self.NofObjects = 0
        self.mainWindow = []        
        self.drawPet(pet)
        self.pack(side = T.LEFT)        
        
    def drawPet(self, pet=''):
        '''
        May break; add checks
        '''
        if not pet:
            pet = self.master.game.pet
                
        # Add main photo
        image_path = self.master.graphicsRoot + 'animals/' + pet.species + '_small.gif'             
        self.gifs = []
        self.gifs.append(T.PhotoImage(file=image_path, master=self))
        self.mainWindow.append(T.Button(self, image=self.gifs[0], width=Pet.WIDTH_OF_PIC,bd=0,takefocus=0))
        self.mainWindow[0].image = self.gifs[0] # keeps a reference        
        self.NofObjects += 1 # keep track of total number of objects
        
        #self.mainWindow.append(T.Label(self, text=self.master.game.pet.name, width=WIDTH_OF_PIC))
        #self.NofObjects += 1 # keep track of total number of objects
        #self.mainWindow[self.NofObjects-1].pack()
        
        for index in range(0,self.NofObjects):
            self.mainWindow[index].grid(row=index, column=0)
        
        
    def addLabel(self,pet=''):
        '''
        Does not work. Does not do anything. Don't use.
        '''
        if not pet:
            pet = self.master.game.pet
            
        self.laabeli = T.Label(self, text=self.master.game.pet.name, width=Pet.WIDTH_OF_PIC)
        self.laabeli.grid()
                
