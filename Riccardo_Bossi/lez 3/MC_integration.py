import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm

mu = 3.4  #centroide gaussiana, ricavata dal grafico della funzione
sigma_norm = 1 #sigma gaussiana
sigma = 2 # sigma funzione

def function(x, sigma):  # Funzione da integrare
    return x**3 * np.exp(-(x**2) / (2 * sigma**2))

N = 1000000 #numero di punti per l'integrazione
X = [] #vettore delle x generate

x_max = 20 # max integrazione
x_min = 0 # min integrazione


# --------------------------------- gen gaussiana --------------------

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

print ("Il risultato dell'integrale con gen normale è:" , integral )
print ("Il risultato dell'integrale con gen uniforme è:" , integral_uni )
print ("Il valore corretto è:" , 2*sigma**4)

punti = np.linspace(0,20,1000)

plt.plot(punti,20*norm(mu,sigma_norm).pdf(punti), label = "PDF gaussiana NON norm" )
plt.plot(punti, function(punti,sigma), label= "function" , color ="Black")

plt.xlabel("x")
plt.ylabel("y")

plt.legend()
plt.show()