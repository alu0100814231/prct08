#!/usr/bin/python
#!encoding: UTF-8
#moduloerror2.py
import moduloP8
import sys

n_test=(100,1000,10000,100000,1000000) #Declaro las dos t_uplas
n_umbral=(0.1,0.01,0.001,0.0001,0.00001)

for i in n_test:    #utilizo dos for porque tengo dos tuplas
  for j in n_umbral:
    a = moduloP8.aprox(i)
    b = moduloP8.aprox(j)
    c = moduloP8.aprox(i,j)#invoco la funcion
    print c #imprimo
   