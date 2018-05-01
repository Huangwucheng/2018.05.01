# #作业：请采用leastsq拟合一条曲线
# y=a*x*x + b*x +c
#
# X:  0,1,2,3,-1,-2,-3
# Y: -1.22,1.85,3.22,10.29,2.21,3.72,8.7
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

plt.figure(figsize=(9,9))

x = np.linspace(-10,10,100)
X = np.array([0.,1., 2., 3., -1.,-2.,-3.])
Y = np.array([-1.22,1.85,3.22,10.29,2.21,3.72,8.7])

def f(p):
    k, b,c= p
    return(Y-(k*X*X+b*X+c))
r = leastsq(f, [1,0,0])
k, b,c = r[0]
print("k=",k,"b=",b,"c=",c)

plt.scatter(X,Y, s=100, color='b',alpha=1.0, marker='o',label='Datapoint')
#
y=k*x*x+b*x+c
plt.plot(x,y,linewidth=5, color='r',linestyle=":",markersize=20, label='Fitting curve')
# #
plt.legend(loc=0, numpoints=1)
leg = plt.gca().get_legend()
ltext  = leg.get_texts()
plt.setp(ltext, fontsize='xx-large')
# #
plt.xlabel(u'/A')
plt.ylabel(u'/V')
# #
plt.xlim(-x.max() * 1.1, x.max() * 1.1)
plt.ylim(-y.max() * 0.1, y.max() * 1.1)
#
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
# #刻度字体大小
plt.legend(loc='upper left')
#
plt.show()