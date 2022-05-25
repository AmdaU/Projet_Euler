from sympy import *

V,omega,c,R = 10,2000*pi,40e-9,5000
T = 2*pi/omega

((c*R*omega/(2))*V**2*omega*c/(1 + R**2*omega**2*c**2)).evalf()
