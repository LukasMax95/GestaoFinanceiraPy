import numpy as np
import matplotlib.pyplot as plt

def VTL(c0, fc, tma, tf):
    roi = []
    vtl = 0
    for i in range(0,tf):
        r = fc/((1 + tma)**(i+1))
        roi.append(r)
        vtl = vtl + r
    vtl = vtl - c0
    return np.array(roi), vtl

def plot_VTL(c0, fc, tma, tf):
    r1 = []
    s1 = []
    for i in range(0,tf):
        a, b = VTL(c0, fc, tma, (i+1))
        r1.append(b)
        s1.append(i+1)
    r1 = np.array(r1)
    z1 = np.array([0]*tf)
    plt.scatter(s1, r1, color="k")
    plt.plot(s1, r1, color='b')
    plt.plot(s1, z1 , color='k')
    plt.xlabel("Tempo até o prazo")
    plt.ylabel("Valor Presente Líquido")
    plt.title("Variação do VPL")
    plt.grid()
    plt.show()

