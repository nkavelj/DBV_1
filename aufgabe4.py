# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 22:54:29 2018

@author: Nikola Kavelj
"""
import math
import numpy as np

eing=np.array([[72,159,182,56],[170,134,178,165],[185,177,84,241],[221,222,240,223]])
ausg_nachb=np.zeros((4,4))
r_temp=0
c_temp=0
for i in range(4):
    for j in range(4):
        r_temp=round(1.065*(i-0.312)+1.341*(j-0.312)+0.312)
        c_temp=round(0.711*(i-0.312)+0.999*(j-0.312)+0.312)
        if r_temp>=0 and r_temp<=3 and c_temp>=0 and c_temp<=3:
            ausg_nachb[i,j]=eing[i,j]
        else:
            ausg_nachb[i][j]=math.nan
print("Transformation des Bildes mit der Methode der naechsten Nachbarschaft")
for x in ausg_nachb:
    print(*x, sep=" ")
ausg_interp=np.zeros((4,4))
for i in range(4):
    for j in range(4):
        r_temp=1.065*(i-0.312)+1.341*(j-0.312)+0.312
        c_temp=0.711*(i-0.312)+0.999*(j-0.312)+0.312
        if r_temp>=0 and r_temp<=3 and c_temp>=0 and c_temp<=3:
            #Quelle fuer Interpolationsformel:Notizen zur DBV_Vorlesung von Prof. Stilla
            ausg_interp[i,j]=(eing[math.ceil(r_temp),math.floor(c_temp)]-eing[math.floor(r_temp),math.floor(c_temp)])*r_temp+(eing[math.floor(r_temp),math.ceil(c_temp)]-eing[math.floor(r_temp),math.floor(c_temp)])*c_temp+(eing[math.ceil(r_temp),math.ceil(c_temp)]+eing[math.floor(r_temp),math.floor(c_temp)]-eing[math.floor(r_temp),math.ceil(c_temp)]-eing[math.ceil(r_temp),math.floor(c_temp)])*r_temp*c_temp+eing[math.floor(r_temp),math.floor(c_temp)]
        else:
            ausg_interp[i,j]=math.nan
        if ausg_interp[i,j]<0:
            ausg_interp[i,j]=0
        elif ausg_interp[i,j]>255:
            ausg_interp[i,j]=255
print("Transformation des Bildes mit Hilfe der bilinearen Interpolation")
for x in ausg_interp:
    print(*x, sep=" ")
