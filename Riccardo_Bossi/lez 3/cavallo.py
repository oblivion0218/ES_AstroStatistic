import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import poisson

# Data
morti = np.array([0, 1, 2, 3, 4])
N = np.array([109, 65, 22, 3, 1]) / 200  # Normalize the frequencies

def poisson(k, mu):
    return poisson.pmf(k, mu) 

p0 = [0] # Initial estimate of the parameter

param, cov = curve_fit(poisson, morti, N, p0=p0) # curve fitting returns the optimal fit parameter and the covariance matrix
mu_opt = param

# Create points to plot the curve
y_fit = poisson(morti, mu_opt)

# Plot
plt.scatter(morti, N, color='red', marker='o', label="Data")  
plt.plot(morti, y_fit, color='blue', label="Poisson Fit")
plt.xlabel("Number of deaths")
plt.ylabel("Frequency")
plt.legend()
plt.show()


