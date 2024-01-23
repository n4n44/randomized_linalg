import numpy as np
import matplotlib.pyplot as plt

def sampling(A,sample_size=30):# 標本からtrace estimatorを計算
    x = []
    w = np.random.standard_normal((sample_size,dim))
    for i in range(1,sample_size):
        x_k = w[i]@A@w[i].T
        x = np.append(x,x_k)
    return x

def tr_estmtr(A, sample_size=30):# trace estimatorの標本平均を計算
    ret = sampling(A, sample_size)
    x_bar = np.sum(ret)/sample_size
    return x_bar
