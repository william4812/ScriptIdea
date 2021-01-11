# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 16:24:37 2020

@author: 2311wiwe
"""

OpTxt = open('PW.txt'); pd = OpTxt.read(); #print(pd);


tmax = 3
for i in range(0, tmax):
    print('Enter the password'); pdin = input()
    if pdin == pd:
        print('Correct password. Authorized')
        break
    else:
        print('Not correct and remaining times of trial:', tmax - 1 -i)