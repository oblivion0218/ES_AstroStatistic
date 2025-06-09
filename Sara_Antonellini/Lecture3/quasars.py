import numpy as np
from matplotlib import pyplot as plt
from astroML.datasets import fetch_dr7_quasar

#Rejection sampling
def rejection(val, bin, N):
    x=np.random.uniform(min(bin), max(bin), N)
    y=np.random.uniform(min(val), max(val), N)
    x_accepted = []
    y_accepted = []
    for i in range(N):
        bin_index = np.digitize(x[i], bin) - 1  # Find the corresponding bin for x[i]
        if y[i] < val[bin_index]:  # Accept point if y[i] is less than the histogram value
            x_accepted.append(x[i])
            y_accepted.append(y[i])

    return x_accepted, y_accepted


N=100000 #Number of uniformly generated numbers
data = fetch_dr7_quasar() # Fetch the quasar data
data = data[:10000] # select the first 10000 points
z = data['redshift']

plt.hist(z, int(len(z)/50), label="AstroMLdataset")
values, bins =np.histogram(z,int(len(z)/50))
x_accepted, y_accepted= rejection(values, bins, N)

plt.scatter(x_accepted,y_accepted, color='red', s=10, marker='o')
plt.savefig("Quasars.png")