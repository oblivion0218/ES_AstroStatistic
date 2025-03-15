import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

# Dati
morti = np.array([0, 1, 2, 3, 4])
N = np.array([109, 65, 22, 3, 1]) / 200  # Normalizziamo le frequenze

# Definizione della funzione gaussiana
def gauss(x, A, mu, sigma):
    return A * np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

# Stima iniziale dei parametri (A, media, deviazione standard)
p0 = [max(N), 0 , 1]

# Fit dei dati
param , cov = curve_fit(gauss, morti, N, p0=p0) #curve fit restituisce i parametri ottimali del fit e la matrice di covarianza
A_opt, mu_opt, sigma_opt = param

# Creiamo i punti per plottare la curva gaussiana
x_fit = np.linspace(min(morti), max(morti), 1000)
y_fit = gauss(x_fit, *param)

# Grafico
plt.scatter(morti, N, color='red', marker='o', label="Dati")  
plt.plot(x_fit, y_fit, color='blue', label="Fit Gaussiano")
plt.xlabel("N° morti")
plt.ylabel("Frequenza")
plt.legend()
plt.show()

# Stampiamo i parametri trovati
print(f"Parametro A (altezza): {A_opt}")
print(f"Media (mu): {mu_opt}")
print(f"Deviazione standard (sigma): {sigma_opt}")
