import numpy as np

#Integer Division function
def intdiv(x,y):
    return x/float(y)

#Numpy division function
def numdiv(x,y):
    return np.array([x])/np.array([float(y)])

def test_intdiv():
    assert intdiv(2,8) == 0.25
    
def test_numdiv():
    assert numdiv(2,8) == 0.25