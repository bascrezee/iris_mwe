import dask
import iris
import numpy as np
import iris.plot as iplot
import matplotlib.pyplot as plt

print("Dask version: {0}".format(dask.__version__))
print("Iris version: {0}".format(iris.__version__))
print("Numpy version: {0}".format(np.__version__))
testfile = './testdata.nc'
cube = iris.load_cube(testfile)
# Try out commenting out the below line
#assert type(cube.data)==type(cube.data)
cube = cube[:,0,0]
plt.title('Plot of iris cube data')
iplot.plot(cube)
plt.show()
