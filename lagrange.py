import operator
from functools import reduce

from pip._vendor.msgpack.fallback import xrange


def LagrangeInter(x, x_list, y_list):
    def polinom(j):
        P = [(x - x_list[m]) / (x_list[j] - x_list[m]) for m in xrange(k) if m != j]
        print("L(%.d)= "%(j),"%.9f"%(reduce(operator.mul, P)))
        return reduce(operator.mul, P)

    k = len(x_list)
    return sum(polinom(j) * y_list[j] for j in xrange(k))

x_list=[0.2,0.35,0.45,0.6,0.75,0.85,0.9]
y_list=[13.7241,13.9776,14.0625,13.9776,13.7241,13.3056,12.7281]
print("result:",LagrangeInter(0.65,x_list,y_list))
