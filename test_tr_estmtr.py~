import numpy as np
import matplotlib.pyplot as plt

dim = 100

B = np.random.uniform(0,1,size=(dim, dim))

print(B)

A = B@B.T

print(A)
print(f"trace : {np.trace(A)}")

w = np.random.standard_normal((30,dim))
sum = 0
data = []
for i in range(1000):
    x = tr_estmtr(A)
    data = np.append(data,x)

plt.hist(data, bins=30, color='blue', alpha=0.7)

plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.show()
