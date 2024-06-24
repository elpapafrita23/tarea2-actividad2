# PROCESAMIENTO 
# Creo el vector utilizando la función 
# arange de numpy 
import matplotlib.pyplot as plotter
from numpy import arange
vector = arange(0, 101, 100) 
# Realizo el calculo de la función 
resultado_funcion = vector ** 4
# SALIDA
# Dibujo el gráfico 
plotter.plot(vector, resultado_funcion) 
# Muestro el gráfico por pantalla 
plotter.show()
