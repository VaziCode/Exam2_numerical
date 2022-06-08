
import math

import sympy as sp
import numpy as np

from math import sin


def simpsonrule(func,start,end,intervals):
    length = (end - start) / intervals
    x = start
    result = (func(start) + func(end))
    print("i     x       f(x)")
    print("___________________")
    for i in range(0, intervals):
        print(i,"|","%.3f"%(x+i*length),"|","%.4f"%func(x + i * length))
        result += (int(True) if i % 2 == 0 else int(False)+2)*2 *func(x + i * length)

    print("\n")
    result = (1/3)*length * result
    En= (1/math.pi)*(length**intervals)*(0.5-(-0.5))*result
    print("En= ",En)
    return result


polynomial = lambda x: (sp.sin(x**4+5*x-6))/(2*np.e**(-2*x+5))
print("result: ",simpsonrule(polynomial,-0.5,0.5,6))

