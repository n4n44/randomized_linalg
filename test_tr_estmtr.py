import numpy as np
import matplotlib.pyplot as plt
from tr_estmtr import tr_estmtr, interval_estmt

dim = 100

B = np.random.uniform(0,1,size=(dim, dim))

print(B)

A = B@B.T

print(A)
tr_a = np.trace(A)
print(f"trace : {tr_a}")

# w = np.random.standard_normal((300,dim))
sum = 0
data = []
for i in range(1000):
    x_bar, lo_bnd, up_bnd = interval_estmt(A, 10, 0.05)
    conf_intvl=(lo_bnd, up_bnd)
    res =  (conf_intvl[0] <= tr_a and conf_intvl[1] >= tr_a)
    print(f"{conf_intvl} : {res}")
    data = np.append(data,res)

correct = np.sum(data)/len(data)*100
print(f"正解率{correct}%")
# plt.hist(data, bins=30, color='blue', alpha=0.7)

# plt.title('Histogram')
# plt.xlabel('Value')
# plt.ylabel('Frequency')

# plt.show()
