import numpy as np
import matplotlib as mpt
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
from scipy.special import jv

U = np.linspace(0.1, 8, 100)

"lol".upper()

I = []

for i in U:
    machin, err = integrate.quad(lambda x: jv(1,x)/(x*(1+np.exp(i*x/2))) ,0 ,np.inf)
    I.append(i/2-2+4*machin)

gap = np.genfromtxt('TP1/gap.dat')
gapc = np.genfromtxt('TP1/gapc.dat')

x,x2 = gap[:, [0]], gapc[:, [0]]
y_12,y_inf = gap[:, [5]], gap[:, [6]]
y_12a,y_infa = gapc[:,[5]],gapc[:,[6]]

exact = plt.plot(U,I,'k', label = '$exact$')
L_12 = plt.plot(x,y_12,'ro',mfc="w", label = '$L = 12$')[0]
L_inf = plt.plot(x,y_inf,'ro', mfc ='r', label = r'$L \rightarrow \infty$')[0]
L_12a = plt.plot(x2,y_12a,'bo', mfc = 'w', label = '$L = 12(amas)$')[0]
L_infa = plt.plot(x2,y_infa,'bo',mfc = 'b' , label = r'$L = \rightarrow \infty(amas)$')[0]
plt.xlabel('$U$')
plt.ylabel('$\Delta$')
plt.legend(loc = 'lower right', edgecolor = 'w')
plt.axes([0.25,0.55,0.3,0.3])
L_12 = plt.plot(x,y_12,'ro',mfc="w", label = '$L = 12$')[0]
L_inf = plt.plot(x,y_inf,'ro', mfc ='r', label = '$L = \infty$')[0]
L_12a = plt.plot(x2,y_12a,'bo', mfc = 'w', label = '$L = 12(amas)$')[0]
L_infa = plt.plot(x2,y_infa,'bo',mfc = 'b' , label = '$L = \infty(amas)$')[0]
plt.xlim((-0.01,0.6))
plt.ylim((-0.001,0.02))
plt.show()
