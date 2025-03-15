import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import norm

mu = 3.4  #centroide gaussiana, ricavata dal grafico della funzione
sigma_norm = 1 #sigma gaussiana
sigma = 2 # sigma funzione

def function(x, sigma):  # Funzione da integrare
    return x**3 * np.exp(-(x**2) / (2 * sigma**2))

N = 100000 #numero di punti per l'integrazione

x_max = 5*sigma # max integrazione
x_min = 0 # min integrazione

ripetizioni = 100

area_uni = []
area_norm = []
pos = []
errore_rel_norm=[]
errore_rel_uni=[]

for i in range(ripetizioni):
    # --------------------------------- gen gaussiana --------------------
    X = [] #vettore delle x generate

    while len(X) < N : #array di punti distribuiti gaussianamente per una maggior efficienza
        X_i = np.random.normal(mu, sigma_norm)
        if (X_i >= x_min and X_i <= x_max):
            X.append(X_i)

    X = np.array(X) # boh, va convertito in array perchè python non lo legge sennò

    peso = norm.pdf(X, mu, sigma_norm)

    weighted_values = function(X, sigma) / peso # Moltiplichiamo la funzione per il peso, cioè per il reciproco della PDF

    integral = np.mean(weighted_values) # Calcoliamo l'integrale

    # ------------------------ gen uniforme --------------------

    Y = np.random.uniform(x_min, x_max, N)

    integral_uni = (x_max - x_min) * np.mean(function(Y, sigma))

    #----------------------------------------------------------------

    area_uni.append(integral_uni)
    area_norm.append(integral)
    pos.append(i+1)

    errore_rel_norm.append( np.abs(integral - 2 * sigma**4) / (2 * sigma**4))
    errore_rel_uni.append ( np.abs(integral_uni - 2 * sigma**4) / (2 * sigma**4))

    print ("Il risultato dell'integrale con gen normale è:" , integral )
    print ("Il risultato dell'integrale con gen uniforme è:" , integral_uni )
    print ("Il valore corretto è:" , 2*sigma**4)

plt.errorbar(pos, area_norm, yerr=errore_rel_norm, fmt='o', color='red', label='Normale', capsize=5)
plt.errorbar(pos, area_uni, yerr=errore_rel_uni, fmt='x', color='blue', label='Uniforme', capsize=5)

plt.plot(pos, area_norm, color='red', linewidth=0.5, label = "aree da dist normale")  # Linea sottile rossa
plt.plot(pos, area_uni, color='blue', linewidth=0.5, label = "aree da dist uniform")  # Linea sottile blu
 
plt.axhline(y=2 * sigma**4, color='black', linestyle='-', linewidth=2)  

plt.xlabel("ripetizioni")
plt.ylabel("valore")

plt.legend()
plt.show()