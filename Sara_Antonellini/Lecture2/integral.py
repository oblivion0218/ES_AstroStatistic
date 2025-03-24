import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm

def f(x,sigma):
    return x**3 * np.exp(-(x**2) / (2 * sigma**2))

def montecarlo1(func, sigma, N, xmin, xmax):
    xi=np.random.normal(3.4,1, N)
    #xi = xi[(xi > xmin) & (xi <= xmax)]
    peso = norm.pdf(xi, 3.4, 1)
    integral=np.mean(func(xi,sigma)/peso)
    return integral


def montecarlo2(func, xmin,xmax, N):
    xi=np.random.uniform(xmin,xmax,N)
    integral=np.mean(func(xi,sigma))
    return integral


sigma=2
N=1000000 #Number of samples
xmin=0
xmax=10*sigma
n=1000 #Number of integrals
integral_gauss=[]
integral_unif=[]
for i in range(n):
    integral_gauss.append(montecarlo1(f, sigma, N, xmin, xmax))
    integral_unif.append((xmax-xmin)*montecarlo2(f,xmin,xmax,N))


fig, ax = plt.subplots(1, 2, figsize=(10, 5))

# Primo grafico
ax[0].hist(integral_gauss, bins=70, density=True, alpha=0.7, color='blue')
ax[0].set_xlabel('Valore dell\'integrale (Gauss)')
ax[0].set_ylabel('Frequenza')

# Secondo grafico
ax[1].hist(integral_unif, bins=70, density=True, alpha=0.7, color='green')
ax[1].set_xlabel('Valore dell\'integrale (Uniforme)')
ax[1].set_ylabel('Frequenza')

plt.tight_layout()
plt.savefig("integral.png")

"""integral_gauss=montecarlo1(f, sigma, N, xmin, xmax)
integral_uniform=(xmax-xmin)*montecarlo2(f,xmin,xmax,N)
print("The Monte Carlo integral value with the uniform distribution is", integral_uniform)
print("The Monte Carlo integral value with the normal distribution is", integral_gauss)

print("The true integrale value is", 2*sigma**4)"""


