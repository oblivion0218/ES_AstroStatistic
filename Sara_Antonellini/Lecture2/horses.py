import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import poisson

N=200  #Number of observations
n_deaths=np.array([0,1,2,3,4])
n_groups=np.array([109,65,22,3,1])

prob=n_groups/N

mu=np.sum(n_deaths*n_groups)/N
model=poisson.pmf(n_deaths, mu)

plt.scatter(n_deaths, prob, color='red', s=40, marker='o', label='Data')
plt.plot(n_deaths, model, linestyle='-', color='blue', label="Poisson Fit")
plt.title("Probability Distribution")
plt.xlabel("Number of Deaths")
plt.ylabel("Probability")
plt.legend()

plt.savefig("Horses.png")
