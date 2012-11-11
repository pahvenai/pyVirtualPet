#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__="Patrik Ahvenainen"
__date__ ="$11.11.2012 20:37:35$"


'''
This module is used to run the GUI for Virtual pets (pyVirtualPet)

It uses TkInter for GUI.

Created on Nov 11, 2012
Last update: Nov 11, 2012

@author: Patrik Ahvenainen
'''

# Path hack for importing from sibling packages
import sys; import os; sys.path.insert(0, os.path.abspath('..'))

import Game.Game as P
import Tkinter as T
from GUImethods import createMenu, drawScreen, keyboardBindings

if __name__ == '__main__':
    root = T.Tk()
    root.title('pyVirtualPet')
    root.graphicsRoot = '../../graphics/'
    
    root.game = P.Game()
    root.game.addPet('Ansku-Bansku')
    
    
    
    createMenu(root)
    keyboardBindings(root)
    drawScreen(root)
    
    root.mainloop()


