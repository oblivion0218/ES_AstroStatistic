import numpy as np
import matplotlib.pyplot as plt


sample = np.random.uniform(0.1, 10, size=1000000)

sample_log = np.log10(sample)

plt.figure(figsize=(10, 5))

plt.hist(sample, bins=np.arange(0.1, 10, 0.1), color='blue', alpha=0.7)
plt.hist(sample_log, bins=np.arange(0.1, 10, 0.1), color='green', alpha=0.7)
plt.title(' Sample')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.xticks(np.arange(0, 10, 0.5))

mean_uniform = np.log10(np.mean(sample))
mean_log = np.mean(sample_log)

median_uniform = np.log10(np.median(sample))
median_log = np.median(sample_log)

print(" il logaritmo della media uniforme è :", mean_uniform)
print(" la media log è :", mean_log)
print(" il logaritmo della mediana uniforme è :", median_uniform)
print(" la mediana log è :", median_log)

plt.show()