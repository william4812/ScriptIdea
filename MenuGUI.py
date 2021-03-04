# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:10:16 2020

@author: wwei
"""

import os, logging

from tkinter import *

import tkinter as tk

import subprocess
#subprocess.call(r"H:\Buffer_zone\quick_calculation\BH_power_estimation\GUI_power_estimation_logo\Power_estimation_15.exe")
#==============================

Font = "Times New Roman"
Font_size = "11"
Label_bd = "11"
Label_width = "19"

#==============================
def SteadyStateModel():
    subprocess.call(r"SS_Power_estimation_16.exe")  
#==============================
def TransientModel():
    #print("Test for transient model")
    #print("T_Power_estimation.exe")
    subprocess.call(r"T_Power_estimation.exe")  
#==============================
    
if __name__ == "__main__":
    
    root = Tk() #create one root widget for this program
    
    wids = root.winfo_screenwidth() # width of the screen
    heis = root.winfo_screenheight() # height of the screen
    rx = root.winfo_x()
    ry = root.winfo_y()
    logging.debug( wids )
    logging.debug( heis )
    
    Title = root.title( "BH calculator menu")
    root.configure(background="Dark grey")
    root.geometry("1200x384")
    
    # Creating a photoimage object to use image 
    photoSS = PhotoImage(file = r"SteadyState.png") 
    
    Label(root, text = 'Steady state model (piping system)', font =(Font, 20)).grid(row = 0, column = 0, sticky = NSEW)
    
    tk.Button(root, text='Steady state model', font=(Font, Font_size), bd=Label_bd, #width = Label_width, 
              relief="groove", fg = "black", bg = "light grey", image = photoSS,  command=SteadyStateModel
              ).grid(row = 1 , column = 0, sticky = NSEW)
    
    photoT = PhotoImage(file = r"Transient.png") 
    
    Label(root, text = 'Transient model (vacuum table)', font =(Font, 20)).grid(row = 0, column = 1, sticky = NSEW)
        
    tk.Button(root, text='Transient model', font=(Font, Font_size), bd=Label_bd,# width = Label_width, 
              relief="groove", fg = "black", bg = "light grey", image = photoT, command=TransientModel
              ).grid(row = 1 , column = 1, sticky = NSEW)
    

    
    root.mainloop()
    logging.debug('End of program')