import numpy as np
from sklearn.linear_model import LinearRegression

np.random.seed(42)
x = 3 * np.random.rand(100, 2)
y = 4 + 2 * x[:, 0] + x[:, 1] + np.random.randn(100)

model = LinearRegression()
model.fit(x,y)
coefficients =- model.coef_
intercept = model.intercept_

print(f"coefficients : {coefficients}")
print(f"intercept : {intercept}")

"""import numpy as np
from sklearn.linear_model import LinearRegression

np.random.seed(42)

x=3*np.random.randn(100, 2)
y=4+2*x[:, 0]+x[:,1]+ np.random.randn(100)

model=LinearRegression()
model.fit(x,y)
a = model.coef_
b =  model.intercept_
print(a)
print(b)"""