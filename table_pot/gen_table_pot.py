import numpy as np
import matplotlib.pyplot as plt

'''
 table potential for LJ
			c12		 c6
	Vlj(r)=	- 	 - 	 -
			r^12	 r^6


For table potential,
format is V(r) = q1q2*f(rij)/const + c12*g(rij)+ c6*h(rij)
here q1=q2=f(rij)=0,
c12 = 4e(sig)^12
c6  = -4e(sig)^6
g(rij) = 1/r^12
h(rij) = 1/r^6
'''

r = np.linspace(0, 4.0, 500)

f = np.zeros(r.shape[0]); fp = np.zeros(r.shape[0])
g = 1/np.power(r, 12); gp = -12/np.power(r, 13)
h = -1/np.power(r, 6) ; hp = 6/np.power(r, 7)

f[0] = f[1]
fp[0] = fp[1]
g[0] = g[1]
gp[0] = gp[1]
h[0] = h[1]
hp[0] = hp[1]

V = np.array([r, f, -fp, g, -gp, h, -hp])
np.savetxt("table.xvg", V.T, fmt="%.6e", delimiter="\t")


ch = input("Do you want to view non-electronic terms? [y/N]")
if(ch=='Y' or ch=='y'):
	plt.plot(r, g+h)
	plt.xlim(0, r.max())
	plt.ylim((g+h).min(), 2)
	plt.show()