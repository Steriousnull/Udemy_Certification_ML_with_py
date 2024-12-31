# train and test

from sklearn.model_selection import train_test_split
import numpy as np

a = np.random.seed(422)

x = np.random.rand(100,1)
y = 2 * x.squeeze() + 1 + 0.1 * np.random.randn(100)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print(x)

print(f"Training set size : {len(x_train)}")
print(f"Testing set size : {len(x_test)}")
