# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 22:15:27 2020

@author: abdoarafa
"""


import numpy as np

name=input('name')
print('welcome'+ str(name))
Length=int(input('Lenght of Cylinder'))
Diameter=int(input('Diameter of Cylinder'))
valueofpi =input('Do you want value of pi to be original or shortened? ')
volume=input('Do you want volume of Cylinder to be  meter or feet ?')

if valueofpi== 'original':
        if volume == 'meter':
            print(np.pi*(Diameter/2)**2*Length)

        else:
            print(np.pi*(Diameter/2)**2*Length*35)
else:
    if volume == 'meter':    
        print(22/7*(Diameter/2)**2*Length)
    else:
        print(22/7*(Diameter/2)**2*Length*35)            
