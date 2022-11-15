import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as si
import math as math
plt.style.use('bmh')

#Defining Constants
E  = 50000000000
m = 150000.
pi4 = math.pi*math.pi*math.pi*math.pi
W = 1.
L =30.
b = 4.
I = 0.05
sinpibl = math.sin(math.pi*b/L)
phifactor = math.sqrt(2/(m*L))
l4 = L*L*L*L
l3 = L*L*L
l2 = L*L
#Don't wana use pows in ilteration so making them constants
e = np.linspace(0,0.9,50) #crack ratio

#F
def f(e):
    return 2*(e/(1-e))*(e/(1-e))*(5.93 - 19.69*e + 37.14*e*e - 35.84*e*e*e + 13.12*e*e*e*e)

#Potential Energy
def u_max(f0):
    return pi4*E*I*.5/m/l4 * (1 + f0*2*W/L*sinpibl*sinpibl)

#Mode shape before crack
def phi1(x,f0):
    ph = phifactor*(math.sin(math.pi*x/L) - x*b*W/l3*f0*math.pi*math.pi*sinpibl*(1-L/b))
    return ph*ph

#Mode shape after crack
def phi2(x,f0):
    ph =  phifactor*(math.sin(math.pi*x/L) + b*W/l2*f0*math.pi*math.pi*sinpibl*(1-x/L))
    return ph*ph

crack_factor = f(e)
max_kinetic_energy = np.zeros(len(crack_factor)) #kinetic energy
max_potential = u_max(crack_factor)
omega_n = np.zeros(len(crack_factor))
for i in range(len(crack_factor)):
    f0 = crack_factor[i]
    max_kinetic_energy[i] = .5 * m * (si.quad(phi1, 0, b, args=(f0))[0] + si.quad(phi2, b, L, args=(f0))[0])
    omega_n[i] = math.sqrt(max_potential[i] / max_kinetic_energy[i])

fig,ax1 = plt.subplots(1,1, figsize=(16, 9))
ax1.plot(e, omega_n)
ax1.set_title("$\omega_n$ with crack")
ax1.set_xlabel("Crack Ratio $\\frac{a}{W}$")
ax1.set_ylabel("Natural Frequency $\omega_n$")

plt.show()


