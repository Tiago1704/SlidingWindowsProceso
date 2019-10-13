# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 18:21:39 2019

@author: Tiago Ibacache
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves

archivo = input('Archivo de sonido : ' )
archivo = 'iuuu 2,53.wav' #Acà cargamos el audio que queremos utilizar
muestreo, sonido = waves.read(archivo) #Muestreo es la frecuencia del sonido
                                        #sonido me tira un array

tamano = np.shape(sonido) #Tamano del audio cargado
muestras = tamano[0]
m = len(tamano) #m es el tamaño en segundos
canales = 1 #Canales dice si es monofonico o estereo
if (m > 1):
    canales = tamano[1]
    
if (canales > 1):
    canal = 0
    unCanal = sonido[: , canal]
else:
    unCanal = sonido
    
parte = unCanal[muestreo]

#Parte Grafica
plt.plot(parte)
plt.show()