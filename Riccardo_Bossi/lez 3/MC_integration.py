import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import norm

mu = 3.4  #centroide gaussiana, ricavata dal grafico della funzione
sigma = 2 # sigma funzione
sigma_norm = 1 #sigma gaussina norm

def function(x, sigma):  # Funzione da integrare
    return x**3 * np.exp(-(x**2) / (2 * sigma**2))

N = 10000 #numero di punti per l'integrazione

x_max = 5*sigma # max integrazione
x_min = 0 # min integrazione

ripetizioni = 1000

area_uni = []
area_norm = []

for i in range(ripetizioni):
    # --------------------------------- gen gaussiana -------------------- IMPORTANCE SAMPLING
    
    X = [] #vettore delle x generate   
    X = np.random.normal(mu, sigma_norm,N) #array di punti distribuiti gaussianamente per una maggior efficienza
    X = np.array(X) # boh, va convertito in array perchè python non lo legge sennò
    X = X[X > 0]

    peso = (1 / (np.sqrt(2 * np.pi) * sigma_norm)) * np.exp(-((X - mu) ** 2) / (2 * sigma_norm ** 2))

    weighted_values = function(X, sigma) / peso # Qui entra in gioco il concetto di importance sampling:
        # Se campionassimo direttamente da una distribuzione uniforme, ogni punto conterebbe in modo uguale.
        # Qui invece i punti sono estratti da una distribuzione gaussiana.
        # Per compensare questa scelta, dividiamo per la densità della distribuzione di campionamento (la PDF della gaussiana).

    integral = np.mean(weighted_values) # Calcoliamo l'integrale

    # ------------------------ gen uniforme --------------------

    Y = np.random.uniform(x_min, x_max, N) #metodo crude

    integral_uni = (x_max - x_min) * np.mean(function(Y, sigma))

    #-----------------------------------------------------------

    area_uni.append(integral_uni)
    area_norm.append(integral)

    #print ("Il risultato dell'integrale con gen normale è:" , integral )
    #print ("Il risultato dell'integrale con gen uniforme è:" , integral_uni )
    #print ("Il valore corretto è:" , 2*sigma**4)


plt.figure(figsize=(10, 5))

# istogramma per le aree calcolate con distribuzione normale
plt.subplot(1,2,1)
plt.hist(area_norm, bins=30, color='red', alpha=0.6, label='Normale', edgecolor='black')
plt.xlabel("Valore dell'integrale")
plt.ylabel("Frequenza")
plt.legend()

# istogramma per le aree calcolate con distribuzione uniforme
plt.subplot(1,2,2)
plt.hist(area_uni, bins=30, color='blue', alpha=0.6, label='Uniforme', edgecolor='black')
plt.xlabel("Valore dell'integrale")
plt.ylabel("Frequenza")
plt.legend()

plt.show()


"""" plot dei punti
plt.errorbar(pos, area_norm, yerr=errore_rel_norm, fmt='o', color='red', label='Normale', capsize=5)
plt.errorbar(pos, area_uni, yerr=errore_rel_uni, fmt='x', color='blue', label='Uniforme', capsize=5)

plt.plot(pos, area_norm, color='red', linewidth=0.5, label = "aree da dist normale")  # Linea sottile rossa
plt.plot(pos, area_uni, color='blue', linewidth=0.5, label = "aree da dist uniform")  # Linea sottile blu
 
pip 
plt.axhline(y=2 * sigma**4, color='black', linestyle='-', linewidth=2)  
"""