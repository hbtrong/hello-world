import numpy as np
from numpy import newaxis
# import lib

print(np.arange(10000))

r = np.random.random((2, 3))
print(r)
print(r.dtype)

np.exp(r)

a = np.ones((3, 4))
print("array a is: \r\n", a)
b = a.ravel()
print("array a is: \r\n", a)
print("array b is: \r\n", b)
print("reshape array b to array c:")
c = b.reshape((2, 6))
print(c)
print("resize b to (3, 4)")
b.resize((3, 4))
print(b)
print("create array e")
e = np.floor(10*np.random.random((3, 4)))
print(e)
f = np.vstack((b, e))
print("f is vetical stack if b and e")
print(f)
g = np.hstack((b, e))
print("g is horizontal stack if b and e")
print(g)

print("=========================================")
a = np.floor(10*np.random.random((2, 12)))
print(a)
b = np.hsplit(a, [3, 6])
print(b)

index = np.floor(10*np.random.random((2, 3)))
print("index ==================")
print(index)
r = 0
c = 0
for row in index:
    for col in row:
        if (index[r, c] > 3):
            index[r, c] = 3
        c += 1
    c = 0
    r += 1
print("index ================== after fix value")
print(index)

def printMsg(msg):
    print(msg)

print(__name__)

if __name__ == '__main__':
    printMsg("Hello : Tristin")
    # print(lib.add(20, 30))
    pass