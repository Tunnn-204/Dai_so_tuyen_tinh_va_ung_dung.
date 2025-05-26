import numpy as np 
from numpy import *
vec1 = np.array([1., 3., 5.])
c = vec1 * 2
print(c)
d = vec1 * vec1
print(d)
e = vec1 / 2
print(e)
f = vec1 + vec1
print(f)
vec2 = array([2., 4.])
g = vec1 + vec2
print(g)
vec3 = array([2., 4., 6.])
h = vec1 + vec3
print(h)
j = vec1 / vec3 
print(j)
k = vec1 * vec3
print(k)
l = 2*vec1 + 5*vec3
print(l)
n = vec3[2]
print(n)
vec4 = np.linspace(0, 20, 5)
print(vec4)
vec5 = np.zeros(5)
print(vec5)
vec6 = np.ones(5)
print(vec6)
vec7 = np.empty(5)
print(vec7)
vec8 = np.random.random(5)
print(vec8)
v = np.array([1.,3.,5.])
v1 = np.sum(v)
print(v1)
v2 = v.shape 
print(v2)
v3 = v.transpose()
print(v3)
v4 = v[:2]
print(v4)
v[0] = 5 
print(v)
v4[:2] = [1.,2.,3.]
print(v4)

