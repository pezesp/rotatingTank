from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import numpy as np

def main():
	r = np.linspace(0, 23, 23)
	theta = np.linspace(0, 2*np.pi, 120)
	R, THETA = np.meshgrid(r, theta)
	# Express the mesh in the cartesian system.
	X, Y = R*np.cos(THETA), R*np.sin(THETA)
	path = 'Vdata/'

	for m in range(1,30,1):
		Z = np.fromfile(path+'V'+str('%02d' % m)+'.dat', dtype=float, sep='   ').reshape(23,120)
		Z = Z.T
		
		fig = plt.figure(m)
		ax = fig.add_subplot(111)
		# Plot the surface.
		ax1 = ax.contourf(X, Y, Z, cmap = plt.cm.winter)
		cb1 = plt.colorbar(ax1)

		ax.set_xlabel(r'$x$')
		ax.set_ylabel(r'$y$')
		ax.set_title(r'Componente V, layer Z='+str('%02d' % m))

		plt.savefig( path+'ComponenteV'+str('%02d' % m)+'.png' , bbox_inches = 'tight' ,\
		  transparent = 0 )
		plt.close(m)

	from subprocess import Popen
	#requiere instalacion de ImageMagick para crear GIF
	program = 'convert' # o bien poner el path que aparece on $ which convert
	image = [program, '-delay', '18','-loop','3',path+'*.png', 'Vlayers.gif']
	Popen(image)
	#plt.show()

if __name__ == '__main__':
    main()