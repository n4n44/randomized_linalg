import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t
def sampling(A,sample_size=30 , dist = np.random.standard_normal):# 標本からtrace estimatorを計算
    dim = A.shape[0]
    x = []
    w = dist((sample_size,dim))
    for i in range(1,sample_size):
        x_k = w[i]@A@w[i].T
        x = np.append(x,x_k)
    return x

def tr_estmtr(A, sample_size=30, dist = np.random.standard_normal):# trace estimatorの標本平均を計算
    ret = sampling(A, sample_size, dist)
    x_bar = np.sum(ret)/sample_size
    s_bar = 0
    for x in ret:
        s_bar+=(x-x_bar)**2
    s_bar/=(sample_size-1)
    return x_bar,s_bar

def interval_estmt(A, sample_size=30, alpha = 0.05):
    x_bar, s_bar = tr_estmtr(A, sample_size)
    t_val = t.ppf(1-alpha,sample_size-1)
    return x_bar,x_bar-t_val*np.sqrt(s_bar),x_bar+t_val*np.sqrt(s_bar)
    
