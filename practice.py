from sympy import *
x=symbols('x')
f=2**x+x**2
print(f.diff(x))
