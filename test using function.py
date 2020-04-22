# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 00:47:43 2020

@author: abdoarafa
"""

while True:
    try:
        import numpy as np

        name=str(input('name'))
        print('welcome'+ str(name))
        Length=int(input('Lenght of Cylinder'))
        Diameter=int(input('Diameter of Cylinder'))
        valueofpi =input('Do you want value of pi to be original or shortened? ')
        volume=input('Do you want volume of Cylinder to be  meter or feet ?')

        def Calc_volume(pi,r,h):
            v=pi*r**2*h
            if valueofpi== 'original':
                if volume == 'meter':
                    print(v)
                else:
                    print(v*35)
        Calc_volume(np.pi,Diameter/2,Length)
        def Calc_volume1(pi,r,h):
            v=pi*r**2*h
            if valueofpi== 'shortened':
                if volume == 'meter':    
                    print(v)
                else:
                    print(v*35)
        Calc_volume1(22/7,Diameter/2,Length)
        break
    except:
       print('wrong format')
       break
    finally:
       print('end')