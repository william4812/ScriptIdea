# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 17:25:51 2020

@author: wwei
"""

#============================================Import modules
import os # The OS module in Python provides a way of using operating system dependent functionality"
clear = lambda: os.system("clear") # lambda functions are small functions usually not more than a line.
clear()
from tkinter import *
import tkinter as tk
from math import *
from numpy import *
import numpy as np
import pandas as pd

#============================================Format settings of the GUI
Font = "Times New Roman"    #The font shown on the GUI
Font_size = "11"            #The font size shown on the GUI
height = 4                  #The number of rows for each weldment to create matrix to store the inputs from the entry
Label_height = "1"          #Height of label

Label_width = "28"          #Width of the label
Input_width = "14" #str( int(Label_width) - 10 )   #Width of the input entries
Label_bd = "2"              #Border thickness
Label_relief = "groove"     #Grooved borders
        
row_ini = 0                 #Initial index of the first row on GUI 
column_ini = 0              #Initial index of the first column on GUI
row_ini_table = 2           #Initial index of the first row for the section of each weldment 

#Perperties of thermal conductivity/interface thermal conductance
k_C_const = {"Ins": 0.057, "6061-6T": 167, "FB": 0.057, "MB": 0.125, "Air": 0.026, "FIB": 0.049}    #W/m-K

rho = {"6061-6T": 2.7E3}  #kg/m3

Cp = {"6061-6T": 896}   #

hinf = 12           #W/m2-K

Fitted_ITC = 0.9    #W/m2-K

t = {"Ins": 2.54E-2, "6061-6T": 1.27E-2, "FB": 4E-4, "MB": 2.54E-2, "Air": 1.65E-2, "FIB": 2.54E-2} #meter



def A():    #m^2
    global Area
    Area = float( Input_h.get() )*2.54E-2 * float( Input_w.get() )*2.54E-2 
    return Area
#===========================    
def R1():   #K/W
    Rest = 1/(hinf * Area) + float(Input_t_ins.get())*2.54E-2/(k_C_const["Ins"]*Area) \
                           + t["6061-6T"]/(k_C_const["6061-6T"]*Area) \
                           + t["FB"]/(k_C_const["FB"]*Area) \
         + 1/(Fitted_ITC * Area)
         
    return Rest
#===========================    
def R2():   #°C/W
    Rest = t["MB"]/(k_C_const["MB"]*Area) \
         + t["Air"]/(k_C_const["Air"]*Area) \
         + t["FIB"]/(k_C_const["FIB"]*Area) \
         + 1/(hinf * Area)
    return Rest
#===========================    
def qRatio():
    A()
    invR = 1/np.round([R1(), R2()], 10); 
    qR = [ invR[0], invR[1] ]/np.sum(invR)  #The ratio of power into bidirections, 1 to top, 2 to bottom
    return qR
#===========================        
def ts():   #sec
    tsestiamte = round(float(Input_t_s.get())*3600, 10)
    gen_Label(Font, tsestiamte, 5, 3, "white", Input_width)
#===========================        
def TF():   #°C
    TFestimate = round(float(Input_T_s.get())*9/5+32, 10)
    gen_Label(Font, TFestimate, 4, 3, "white", Input_width)
#===========================    
def V():    #m^3
    global Volumn
    Volumn = round(float(Input_h.get()) * float(Input_w.get()) * float(Input_t.get())*25.4**3/1.0E9, 10)
    gen_Label(Font, format(Volumn, ".6f"), 11, 1, "white", Input_width)
#===========================
def Lump_Tran():
    Req = 1/(hinf * Area) + float(Input_t_ins.get())*2.54E-2/(k_C_const["Ins"]*Area)
    P = 1/Req / ( float(Input_rho.get())*float(Input_Cp.get())*Volumn ); #print("P", P)
    
    theta_s = float(Input_T_s.get()) - float(Input_T_inf.get()); 
    theta_i = float(Input_T_i.get()) - float(Input_T_inf.get());
    q1_est = (theta_s - theta_i*np.exp(-P*round(float(Input_t_s.get())*3600, 10))) * P / \
             (1-np.exp(-P*round(float(Input_t_s.get())*3600, 10))) * \
             ( float(Input_rho.get())*float(Input_Cp.get())*Volumn )
    #print(q1_est)
    Q = q1_est / ( float(Input_rho.get())*float(Input_Cp.get())*Volumn ); #print("Q", Q)
    return q1_est
#===========================
def Pw():
    gen_Label(Font, round(float(Input_t_s.get())*3600, 10), 5, 3, "white", Input_width)
    
    V(); ts(); TF(); qRatio(); A(); Lump_Tran()
    
    q = Lump_Tran() / qRatio()[0]; print(q)
    
    gen_Label(Font,format(q, ".2f"), 0, 1, "yellow", "24")    #Output of total watts, q(W)
    
    print("Pw")
#===========================Functions generating labels
def gen_Label(font, arg, r, c, color, wd):
    
    Label(gui, text = arg, font=(font, Font_size), fg = "black", bg = color, 
          height = Label_height, width = wd, bd=Label_bd, 
          relief="groove").grid(row = r, column = c, sticky=NSEW)
#===========================Functions generating entries    
def gen_Input(r, c):
    
    Input = Entry(gui, width = Input_width, font=(Font, "10"))
    Input.grid(row = r, column = c , sticky=NSEW)
    Input.insert(END, '%d' % (1))
    
#===========================Import the image
def img_label(imgPath, r, col):
#    print(imgPath)
    photo = PhotoImage(file = imgPath)
    label = Label(gui, image=photo, bg = 'lightgrey')
    label.image = photo
    label.grid(row = r, column = col, columnspan=5, rowspan=2, sticky=NSEW, padx=5, pady=5)
    
#===========================Main function

if __name__ == "__main__":
    
    global Volumn
    Volumn = 0.0
    
    gui = Tk()                              #create a GUI window
    gui.title("Transient model")            #Set the title of the GUI frame
    gui.configure(background="Dark grey")   #Set the background color
    wids = gui.winfo_screenwidth()          #Get the width of the screen
    heis = gui.winfo_screenheight()         #Get the height of the screen
    gui.geometry( "%dx%d+%d+%d" %(wids/2*1.2, heis/2*1.3, 0, 0) )       #Create the screen
    #print(wids, heis)
    
    #===========================================
    gen_Label(Font, "Total watts, q (W)", 0, 0, "yellow", "24")
    
    Pw_but = tk.Button( gui, text='Calculate q (W)', font=(Font, Font_size), bd=Label_bd, 
                       width = "14", relief="groove", fg = "white", bg = 
                       "green", command=Pw ).grid(row = 0 , column = 2, sticky=NSEW)
    
    gen_Label(Font, "                  ", 0, 1, "yellow", "24")    #Output of total watts, q(W)
    gen_Label(Font, "                  ", 1, 0, "Light grey", Input_width)
    
    #===========================================
    gen_Label(Font, "Ambient temperature T_∞ (°C)", 2, 0, "Light grey", "24")
    gen_Label(Font, "Initial temperature T_i (°C)", 3, 0, "Light grey", "24")
    gen_Label(Font, "Operating temperature T_s (°C)", 4, 0, "Light grey", "24")
    gen_Label(Font, "Heating time t_s (hr)", 5, 0, "Light grey", "24")

    #===========================================
    Input_T_inf = Entry(gui, width = Input_width, font=(Font, Font_size))
    Input_T_inf.grid(row = 2, column = 1, sticky=NSEW)
    Input_T_inf.insert(5, "22.6")
    
    Input_T_i = Entry(gui, width = Input_width, font=(Font, Font_size))
    Input_T_i.grid(row = 3, column = 1, sticky=NSEW)
    Input_T_i.insert(5, "22.6")  
    
    Input_T_s = Entry(gui, width = Input_width, font=(Font, Font_size))
    Input_T_s.grid(row = 4, column = 1, sticky=NSEW)
    Input_T_s.insert(5, "60.0") 
    
    TF_but = tk.Button( gui, text="T_s (°F)", font=(Font, Font_size), bd=Label_bd, 
                       width = "14", relief="groove", fg = "white", bg = 
                       "green", command=TF ).grid(row = 4 , column = 2, sticky=NSEW)
    
    gen_Label(Font, round(float(Input_T_s.get())*9/5+32, 2), 4, 3, "white", Input_width)
    
    
    Input_t_s = Entry(gui, width = Input_width, font=(Font, Font_size))
    Input_t_s.grid(row = 5, column = 1, sticky=NSEW)
    Input_t_s.insert(5, "2.41") 
    
    ts_but = tk.Button( gui, text="t_s (sec)", font=(Font, Font_size), bd=Label_bd, 
                       width = "14", relief="groove", fg = "white", bg = 
                       "green", command=ts ).grid(row = 5 , column = 2, sticky=NSEW)
    
    gen_Label(Font, round(float(Input_t_s.get())*3600, 2), 5, 3, "white", Input_width)
    
    #===========================================
    gen_Label(Font, "                  ", 6, 0, "Light grey", "24")   
    gen_Label("bold Times New Roman", "Heated object dimension", 7, 0, "Light grey", "24")
    
    
    gen_Label(Font, "Height, h (in)", 8, 0, "Light grey", "24")
    Input_h = Entry(gui, width = Input_width, font=(Font, Font_size))
    Input_h.grid(row = 8, column = 1, sticky=NSEW)
    Input_h.insert(5, "56")    
    
    gen_Label(Font, "Width, w (in)", 9, 0, "Light grey", "24")
    Input_w = Entry(gui, width = Input_width, font=(Font, Font_size))
    Input_w.grid(row = 9, column = 1, sticky=NSEW)
    Input_w.insert(5, "42") 
    
    gen_Label(Font, "Thickness, t (in)", 10, 0, "Light grey", "24")
    Input_t = Entry(gui, width = Input_width, font=(Font, Font_size))
    Input_t.grid(row = 10, column = 1, sticky=NSEW)
    Input_t.insert(5, "0.5") 

    V_but = tk.Button( gui, text='Calculate volume (m^3)', font=(Font, Font_size), bd=Label_bd, 
                       width = "14", relief="groove", fg = "white", bg = 
                       "green", command=V ).grid(row = 11 , column = 0, sticky=NSEW)
    
    gen_Label(Font, round(float(Input_h.get()) * float(Input_w.get()) * float(Input_t.get())*25.4**3/1.0E9, 6), 11, 1, "white", Input_width)
    
    #===========================================
    gen_Label(Font, "                  ", 12, 0, "Light grey", "24")
    gen_Label("bold Times New Roman", "Heated object properties", 13, 0, "Light grey", "24")
    
    gen_Label(Font, "Density \u03C1, (kg/m^3)", 14, 0, "Light grey", "24")
    Input_rho = Entry(gui, width = Input_width, font=(Font, Font_size))
    Input_rho.grid(row = 14, column = 1, sticky=NSEW)
    Input_rho.insert(5, "2700")     
    
    gen_Label(Font, "Specific heat C_p, (J/kg-°C)", 15, 0, "Light grey", "24")
    Input_Cp = Entry(gui, width = Input_width, font=(Font, Font_size))
    Input_Cp.grid(row = 15, column = 1, sticky=NSEW)
    Input_Cp.insert(5, "896")  
    
    #===========================================
    gen_Label(Font, "Insulation thickness, t_ins (in)", 16, 0, "Light grey", "24")
    Input_t_ins = Entry(gui, width = Input_width, font=(Font, Font_size))
    Input_t_ins.grid(row = 16, column = 1, sticky=NSEW)
    Input_t_ins.insert(5, "0")      
    #======================================================
    imgPath = "VacTabConfig.gif"                         # File name of the imported image   
    img_label(imgPath, 17, 2)    # Import the image
    # Start the GUI
    gui.mainloop()