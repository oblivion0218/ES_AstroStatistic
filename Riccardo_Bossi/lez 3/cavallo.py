import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import poisson

# Dati
morti = np.array([0, 1, 2, 3, 4])
N = np.array([109, 65, 22, 3, 1]) / 200  # Normalizziamo le frequenze

def poisson(k, mu):
    return poisson.pmf(k, mu) 

p0 = [0] # Stima iniziale del parametro

param, cov = curve_fit(poisson, morti, N, p0=p0) #curva fit restituisce il parametro ottimale del fit e la matrice di covarianza
mu_opt = param

# Creiamo i punti per plottare la spezzata
y_fit = poisson(morti, mu_opt)

# Grafico
plt.scatter(morti, N, color='red', marker='o', label="Dati")  
plt.plot(morti, y_fit, color='blue', label="Fit Poissoniano")
plt.xlabel("N° morti")
plt.ylabel("Frequenza")
plt.legend()
plt.show()


