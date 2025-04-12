import numpy as np
import matplotlib.pyplot as plt

sample = np.random.uniform(0.1, 10, size=1000000) #uniform sampling

sample_log = np.log10(sample) #logarithm of the sample

plt.figure(figsize=(10, 5))

plt.hist(sample, bins=np.arange(0.1, 10, 0.1), color='blue', alpha=0.7) #uniform plot
plt.hist(sample_log, bins=np.arange(0.1, 10, 0.1), color='green', alpha=0.7) #logarithmic plot
plt.title(' Sample')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.xticks(np.arange(0, 10, 0.5))

mean_uniform = np.log10(np.mean(sample)) # logarithm of the uniform mean
mean_log = np.mean(sample_log) # mean of the logarithm of the sample

median_uniform = np.log10(np.median(sample)) # logarithm of the uniform median
median_log = np.median(sample_log) # median of the logarithm

print(" the logarithm of the uniform mean is:", mean_uniform)
print(" the log mean is:", mean_log)
print(" the logarithm of the uniform median is:", median_uniform)
print(" the log median is:", median_log)

plt.show()
