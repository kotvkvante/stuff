from math import *
import scipy as sp
from scipy.interpolate import UnivariateSpline
from scipy.interpolate import interp1d
from scipy.integrate import simps, trapz
from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt

def msimple_integral(x, y):
    if(len(x) != len(y)):
        print("ERROR: msimple_integral")
        return
    S = 0
    for i in range(len(x)-1):
        dx = x[i+1]-x[i]
        if(y[i] < 0):
            print("msimple_integral: y<0")
            return
        S+= dx * (y[i]+y[i+1])/2
    if (y[len(x)-1]) < 0:
        print("msimple_integral: y<0")
        return
    return S

def test1():
    x = np.array([0, 15, 30, 45, 60, 75, 100])
    y = np.array([1, 0.9, 0.72, 0.6, 0.5, 0.43, 0.35])
    x = np.radians(x)
    plt.plot(x, y, marker='o', color='b')
    
    f2 = interp1d(x, y, kind='cubic')
    xnew = np.linspace(min(x), max(x), num=41, endpoint=True)
    plt.plot(xnew, f2(xnew))
    print("s", integrate.simpson(y, x))
    print("s", simps(y, x=x))
##    print(quad(y, x=x))
    print("t", trapz(y, x=x))

    print("t2", trapz(f2(xnew), x=xnew))

    _x2 = [0, 30, 30, 60]
    _k2 = [1, 1, 0.8, 0.8]
    x2 = np.array([radians(elem) for elem in _x2])
    y2 = np.array([elem[1] * uq23(elem[0]) for elem in list(zip(x2, _k2))])

    print(x2, y2)
##    spl = UnivariateSpline(x, y)
##    xs = np.linspace(-3, 3, 1000)
##    plt.plot(xnew, spl(xnew), 'g', lw=3)
    

if __name__ == "__main__":
    print("math_integral module")
    print("scipy version: ", sp.__version__)
    x = [0, 1, 2, 4]
    y = [1, 2, 1, 3]
    s = msimple_integral(x, y)

    x1 = np.linspace(0, 3, 11)
    y1 = x1**2
##    print(x, y)
    spl = UnivariateSpline(np.array(x), np.array(y))
    print(spl)
    print(spl.integral(0, 3))
    
    print(s)


##    spl = UnivariateSpline(x, y)
##    xs = np.linspace(-3, 3, 1000)
##    plt.plot(xs, spl(xs), 'g', lw=3)

##    rng = np.random.default_rng()
##    x = np.linspace(-3, 3, 50)
##    y = np.exp(-x**2) + 0.1 * rng.standard_normal(50)
##    plt.plot(x, y, 'ro', ms=5)

##    spl = UnivariateSpline(x, y)
##    xs = np.linspace(-3, 3, 1000)
##    plt.plot(xs, spl(xs), 'g', lw=3)
    
##    f2 = interp1d(x, y, kind='cubic')
##    xnew = np.linspace(min(x), max(x), num=41, endpoint=True)
##    plt.plot(xnew, f2(xnew))

    
##    spl.set_smoothing_factor(0.5)
##    plt.plot(xs, spl(xs), 'b', lw=3)
    test1()
    plt.show()
