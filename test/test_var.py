from Urutu import *
import numpy as np

@Urutu("CL")
def divmul(a, b, c, d):
	Tx, Ty, Tz = 100, 1, 1
	Bx, By, Bz = 1, 1, 1
	w, x, y, z = 11, 1.3, 'open.cl', "o.pen.cl"
	c[tx] = a[tx] / b[tx]
	d[tx] = a[tx] * b[tx]
	return c, d

@Urutu("CU")
def addsub(a, b, e, f):
	Tx, Ty, Tz = 100, 1, 1
	Bx, By, Bz = 1, 1, 1
	w, x, y, z = 10, 1.2, 'cu.da', "c.uda"
	e[tx] = a[tx] + b[tx]
	f[tx] = a[tx] - b[tx]
	return e, f

a = np.random.randint(10, size = 100)
b = np.random.randint(10, size = 100)
c = np.array(a, dtype = 'f')
d = np.empty_like(a)
e = np.empty_like(a)
f = np.empty_like(a)

print "The Array A is: \n", a
print "The Array B is: \n", b
print "Running on OpenCL.. \n", divmul(a, b, c, d)
print "Running on CUDA.. \n", addsub(a, b, e, f)
