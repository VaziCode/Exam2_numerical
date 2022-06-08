import math
import sympy as sp
import numpy as np

import sympy as sp

def toDerivative(polynomial):
    x = sp.symbols('x')
    derivative = sp.diff(polynomial(x))
    return sp.lambdify(x, derivative, 'math')

def newtonRaphson(polynomial,left,right,epsilon):
    derivative = toDerivative(polynomial)
    xr = (left+right)/2
    iteration = 0
    xrOld = 0
    while abs(xr - xrOld)> epsilon:
        xrOld = xr
        xr = xr - (polynomial(xr)/derivative(xr))
        iteration +=1
    print('Root:', xr)
    print('iteration:',iteration)

def secantMethod(polynomial, left, right, epsilon):
    iteration = 0
    xr, xr1 = left, right
    while abs(xr-xr1) > epsilon:
        xrTemp = xr1
        xr1 = (xr*polynomial(xr1)-xr1*polynomial(xr))/(polynomial(xr1)-polynomial(xr))
        xr = xrTemp
        iteration += 1
    print('Root:', xr1)
    print('iterations:', iteration)

def findRoots(polynomial, left, right):
    epsilon = 0.0001
    leftOld = left
    step = 0.1
    print('Finding roots using the Newton-Raphson method:')
    while left < right:
        if polynomial(left)*polynomial(left + step)<0:
            newtonRaphson(polynomial, left, left + step, epsilon)
        left += step
    left = leftOld

    print('\nFinding roots using the Secant method:')
    while left < right:
        if polynomial(left)*polynomial(left + step)<0:
            secantMethod(polynomial, left, left + step, epsilon)
        left += step

polynomial = lambda x: (sp.sin(x**4+5*x-6))/(2*np.e**(-2*x+5))
findRoots(polynomial,-1.5,1.5)
# print("result: ",simpsonrule(polynomial,-0.5,0.5,6))