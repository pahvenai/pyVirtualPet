# -*- coding: utf-8 -*-
__author__="Patrik Ahvenainen"
__date__ ="$11.11.2012 22:31:23$"

'''
This module contains functions for GUI modification

Created on Nov 11, 2012
Last update: Nov 11, 2012

@author: Patrik Ahvenainen
'''

import Tkinter as T
import tkFileDialog, tkMessageBox
from SimpleCallback import SimpleCallback
from Pet import Pet

def createMenu(root):
    '''
    Creates the menu on the top of the screen which
    has the following menu items
    
    Exit <ESC>    
    '''
    # create a top-level menu
    menubar = T.Menu(root)
    
    # create a pull-down menu, and add it to the menu bar
    filemenu = T.Menu(menubar, tearoff=0)
    filemenu.add_separator()  
    filemenu.add_command(label="Exit <ESC>", command=root.destroy)

    menubar.add_cascade(label="Game", menu=filemenu)

    # display the menu
    root.config(menu=menubar)
    
def drawScreen(root):
    '''
    Draw all objects on screen
    '''
    root.petFrame = Pet(root)
  
    
def keyboardBindings(root):
    '''
    Handle keyBoard bindings:

    <Escape>      Quit game
    '''
    

    callback = SimpleCallback(quit, root)
    root.bind("<Escape>", callback)
    root.bind("<Control-x>", callback)
    root.bind("<Control-q>", callback)


  
def quit(root, event=None):
    if tkMessageBox.askokcancel("Quit", "Do you really wish to quit?"):
        root.destroy()
