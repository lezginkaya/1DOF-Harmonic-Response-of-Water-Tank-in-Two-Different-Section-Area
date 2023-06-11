import numpy as np
import matplotlib.pyplot as plt

E=210000000000 #modulus of elasticity of stractures,pa
H=10 #hight of structure,m
m=100 # mass of water tank, kg

#1 scenario  is rectangular cross section area structure
h=0.700
b=0.300
I_r=(b*h**3)/12

k_r=(3*E*I_r)/H**3  #N/m
w_r=(1/(2*np.pi))*np.sqrt(k_r/m) #rad/s
wn_r=w_r/60
wn_r=round(wn_r,3)
T_r=1/wn_r
T_r=round(T_r,3)

#assumed that structure moves 50mm on lateral direction
x0=50
xt_r=x0*np.cos(w_r*np.linspace(x0,0.05*np.pi,150)+(np.pi/2))

#2. scenario is circular cross section area structure
D=0.7
d=0.3
I_c=((np.pi*(D**4-d**4)))/64

k_c=(3*E*I_c)/H**3
w_c=(1/(2*np.pi))*np.sqrt(k_c/m) #rad/s
wn_c=w_c/60
wn_c=round(wn_c,3)
T_c=1/wn_c
T_c=round(T_c,3)
x_0=30
xt_c=x_0*np.cos(w_c*np.linspace(x_0,0.05*np.pi,100)+(np.pi/2))

plt.plot(np.linspace(7.5,0.05*np.pi,150),xt_r, color="red", label="Wt")
plt.plot(np.linspace(7.5,0.05*np.pi,100),xt_c, color="blue", label="Wc")
plt.ylabel("X(mm)")
plt.xlabel("T(sn)")
plt.text(-1,-70,f'Natural Freq(rectangular column):{wn_r} Hz', color="red")
plt.text(-1,-74,f'Period(rectangular column:{T_r} Sn',color="red")
plt.text(-1,-78,f'Natural Freq(circular column):{wn_c} Hz',color="blue")
plt.text(-1,-82,f'Period(circular column):{T_c} Sn',color="blue")
plt.legend()
plt.show()



