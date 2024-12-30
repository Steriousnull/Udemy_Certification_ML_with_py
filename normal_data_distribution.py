import numpy as np
import matplotlib.pyplot as plt

mean = 50
std_dev = 10
sample_size = 1000


normal_data = np.random.normal(loc=mean, scale=std_dev, size = sample_size)
plt.hist(normal_data, bins=30, edgecolor='black', density=True)
plt.title("Norml Distribution - Generated")
plt.xlabel('Values')
plt.ylabel('Probabilit Density')
plt.show()
