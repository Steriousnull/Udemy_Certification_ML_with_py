import numpy as np
from sklearn.preprocessing import MinMaxScaler
np.random.seed(42)
data = np.random.rand(100,1) * 100 + 500
scaler = MinMaxScaler
scaled_data = scaler.fit_transform(data)
print("Original data")
print(data[:,s])
print("\nscaled data : ")
print*scaled_data[:5]