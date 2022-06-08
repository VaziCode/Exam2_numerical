from sympy import *

x = Symbol('x')

def L(i, f, x0):

    L1 = ""
    num = 1
    for j in range(len(f)):
        if j != i:
            num *= ((x0 - f[j][0]) / (f[i][0] - f[j][0]))
            L1 += "((x - " + str(f[j][0]) + ") / (" + str(f[i][0]) + " - " + str(f[j][0]) + "))"
            if i == len(f) - 1:
                if j != len(f) - 2:
                    L1 += " + "
            elif j != len(f) - 1:
                L1 += " + "
    return num, L1


def lagrange_interpolation(f, x0):


    sum = 0
    P = ""
    l = list()
    for i in range(len(f)):
        if i != 0:
            P += " + "
        num, L1 = L(i, f, x0)
        P += "L" + str(i) + " * " + str(f[i][1])
        l.append(('L' + str(i), L1, num))
        sum += num * f[i][1]
    return sum, l, P


x0 = 0.65
f = [(0.2, 13.7241), (0.35, 13.9776), (0.6,14.0625), (0.75, 13.9776), (0.85, 13.7241),(0.9,12.7281)]
ans, l, P = lagrange_interpolation(f, x0)
print("P: " + str(P) + "\n")
print("L array:")
for i in l:
    print(i)
print("\nf(" + str(x0) + ") = " + str(ans))
x_list=[0.2,0.35,0.45,0.6,0.75,0.85,0.9]
y_list=[13.7241,13.9776,14.0625,13.9776,13.7241,13.3056,12.7281]
