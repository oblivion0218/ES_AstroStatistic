import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import norm

mu = 3.4  #centroide gaussiana, ricavata dal grafico della funzione
sigma = 2 # sigma funzione
sigma_norm = 1 #sigma gaussina norm

def function(x, sigma):  # Funzione da integrare
    return x**3 * np.exp(-(x**2) / (2 * sigma**2))

N_max = 10000 #numero di punti per l'integrazione

x_max = 5*sigma # max integrazione
x_min = 0 # min integrazione

area_uni = []
area_norm = []
err_norm = []
err_uni = []

number =[]

expected = 2 * sigma**4

for N in range(N_max):
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

    number.append(N)
    area_uni.append(integral_uni)
    area_norm.append(integral)
    err_norm.append( abs(integral - expected)/expected )
    err_uni.append( abs(integral_uni - expected)/expected )

    #print ("Il risultato dell'integrale con gen normale è:" , integral )
    #print ("Il risultato dell'integrale con gen uniforme è:" , integral_uni )
    #print ("Il valore corretto è:" , 2*sigma**4)

plt.figure(figsize=(10, 5))
plt.xscale('log')
plt.plot(number, area_norm, label = "importance sampling")
plt.plot(number, area_uni, label ="uniform sampling")
plt.xlabel("point for integral")
plt.ylabel("value")
plt.axhline(y=2 * sigma**4, color='black', linestyle='-', linewidth=1, label ="true values")
plt.legend() 

plt.show()




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


mean_norm = np.mean(area_norm)
median_norm = np.median(area_norm)
std_norm = np.std(area_norm)

mean_uni = np.mean(area_uni)
median_uni = np.median(area_uni)
std_uni = np.std(area_uni)

plt.figure(figsize=(10, 5))

# Istogramma per la distribuzione normale
plt.subplot(1,2,1)
plt.hist(area_norm, bins=30, color='red', alpha=0.6, edgecolor='black')
plt.xlabel("Valore dell'integrale")
plt.ylabel("Frequenza")
# Aggiungi testo con le statistiche
plt.text(0.95, 0.95, 
          f"Distribuzione: Normale\nMedia: {mean_norm:.2f}\nMediana: {median_norm:.2f}\nDev std: {std_norm:.2f}",
         transform=plt.gca().transAxes,
         verticalalignment='top',
         horizontalalignment='right',
         fontsize=10,
         bbox=dict(boxstyle="round", facecolor="white", alpha=0.8))

# Istogramma per la distribuzione uniforme
plt.subplot(1,2,2)
plt.hist(area_uni, bins=30, color='blue', alpha=0.6, label='Uniforme', edgecolor='black')
plt.xlabel("Valore dell'integrale")
plt.ylabel("Frequenza")
# Aggiungi testo con le statistiche
plt.text(0.95, 0.95, 
        f"Distribuzione: Uniforme\nMedia: {mean_uni:.2f}\nMediana: {median_uni:.2f}\nDev std: {std_uni:.2f}",
         transform=plt.gca().transAxes,
         verticalalignment='top',
         horizontalalignment='right',
         fontsize=10,
         bbox=dict(boxstyle="round", facecolor="white", alpha=0.8))

plt.tight_layout()
plt.show()