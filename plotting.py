from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111)
r = np.linspace(0, 22, 23)
theta = np.linspace(0, 2*np.pi, 120)
R, THETA = np.meshgrid(r, theta)

Z = np.fromfile('V7.dat', dtype=float, sep='   ').reshape(23,120)
Z = Z.T
#print(Z[0:24])
# Express the mesh in the cartesian system.
X, Y = R*np.cos(THETA), R*np.sin(THETA)

# Plot the surface.
ax1 = ax.contourf(X, Y, Z, cmap=plt.cm.YlGnBu_r)
plt.colorbar(ax1)
#ax.set_zlim(0, 1)
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
ax.set_title(r'Componente V')
#ax.set_zlabel(r'$V$')
plt.savefig( 'ComponenteV.pdf' , bbox_inches = 'tight' , pad_inches = 0 ,\
  transparent = True )
plt.show()
