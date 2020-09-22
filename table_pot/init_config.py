import numpy as np
import sys
from numpy.random import random

n = 216
if(len(sys.argv)>1):
	n = int(sys.argv[1])

if((np.cbrt(n)-int(np.cbrt(n)))>1e-6):
	n = int(pow(np.ceil(np.cbrt(n)),3))

mass = 1
rho = 0.8842
side = np.cbrt(n*mass/rho)

x = np.zeros(n)
y = np.zeros(n)
z = np.zeros(n)

cube_root = int(np.cbrt(n))
ctr = 0

for i in range(cube_root):
	for j in range(cube_root):
		for k in range(cube_root):
			x[ctr] = i*side/cube_root
			y[ctr] = j*side/cube_root
			z[ctr] = k*side/cube_root

			ctr += 1

x = x + (side-x.max())/2
y = y + (side-y.max())/2
z = z + (side-z.max())/2

ctr = 0

with open("init.gro","w") as f:
	f.write("LJ gas simulation\n%d\n" %(n))

	for i in range(n):
		f.write("%5d%-5s%5s%5d%8.3f%8.3f%8.3f\n" %(i+1, f"P","He",(i+1),x[i],y[i],z[i]))

	f.write("  %.5lf %.5lf %.5lf\n" %(side, side, side))