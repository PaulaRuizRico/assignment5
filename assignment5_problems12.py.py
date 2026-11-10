import matplotlib.pyplot as pp
import numpy as np
#Problem 1:
A = 10
a = 2
k = 0.4

x = np.arange(0, 20.1, 0.1)
E = A * np.cos((np.pi * x)/a) * np.e**(-k * x)

pp.figure(figsize=(10, 5))
pp.plot(x, E, label='E(x)', color='red')
pp.title('Problem 1')
pp.xlabel('Position x (m)')
pp.ylabel('E (V/m)')
pp.grid(True)
pp.legend()
pp.savefig('problem1.png', dpi=300)

#Problem 2:
dx = 0.1
def E_func(x):
    return A * np.cos(np.pi * x /a) * np.exp(-k * x)
def dE(x):
    return A * np.exp(-k * x) * (-(np.pi/a) * np.sin(np.pi * x /a) - k * np.cos(np.pi*x/a))
#Forward differencing
dE_forward = (E[1:] - E[:-1]) / dx
x_forward = x[:-1]
#Central differencing
dE_central = (E[2:] - E[:-2]) / (2 * dx)
x_central = x[1:-1]

#Plot
pp.figure(figsize=(10, 5))
pp.plot(x, dE(x), label='analytic', color='black', linewidth=2)
pp.plot(x_forward, dE_forward, label='Foward difference', color='red')
pp.plot(x_central, dE_central, label='Central difference', color='blue')
pp.title('Problem 2: dE/dx')
pp.xlabel('Position x (m)')
pp.ylabel('dE/dx (V/m$^2$)')
pp.legend()
pp.savefig('problem2.png', dpi=300)

#Absolute error
err_forward = np.abs(dE_forward - dE(x_forward))
err_central = np.abs(dE_central - dE(x_central))

pp.figure(figsize=(10, 5))
pp.semilogy(x_forward, err_forward, label='Forward difference', color='red')
pp.semilogy(x_central, err_central, label = 'Central difference', color='blue')
pp.title('Absolute error ($\\Delta x$ = 0.1 m)')
pp.xlabel('Position x (m)')
pp.ylabel('|Numerical - analytic| (V/m$^2$)')
pp.legend()
pp.savefig('problem2_error.png', dpi=300)
#Which method is more accurate? The central difference method is more accurate. It can be seen on the plot that its absolute error is about one to two orders of magnitude smaller than the forward differencing method.

#dx=0.05 m
dx2 = 0.05
x2 = np.arange(0, 20 + dx2/2, dx2)
E2 = E_func(x2)

dE_forward2 = (E2[1:] - E2[:-1]) / dx2
dE_central2=  (E2[2:] - E2[:-2]) / (2 * dx2)
err_forward2= np.abs(dE_forward2 - dE(x2[:-1]))
err_central2=np.abs(dE_central2 - dE(x2[1:-1]))

pp.figure(figure=(10, 5))
pp.semilogy(x2[:-1], err_forward2, label='Forward difference', color='red')
pp.semilogy(x2[1:-1], err_central2, label= 'Central difference', color='blue')
pp.title('Absolute error, $\\Delta x = 0.05m$')
pp.xlabel('Position x (m)')
pp.ylabel('|Numerical - Analytic| (V/m$^2$)')
pp.legend()
pp.savefig('problem2_error2.png', dpi=300)
#The error of the forward difference method decreased by a factor of about 2; whereas the error of the central difference method decreased by a factor of about 4. In terms of truncation error, the forward difference has error O(dx), and the central difference method has error O(dx^2), which after dx being halved (dx/2) produce the results we observe.

#x=1m vs. dx, log-log
x0 = 1.0
dxs = 10.0 ** -np.arange(1,16)
error_dx = np.abs((E_func(x0 + dxs) - E_func(x0)) / dxs - dE(x0))

pp.figure(figsize=(10, 5))
pp.loglog(dxs, error_dx, color='red', label='Forward difference error')
pp.title('Error vs $\\Delta x$ at x = 1m')
pp.xlabel('$\\Delta x$ (m)')
pp.ylabel('|Numerical - Analytic| (V/m$^2$)')
pp.legend()
pp.savefig('problem2_bonus.png', dpi=300)
#As dx gets very small, the error eventually increases as E(x + dx) and E(x) become almost the same and the computer doesn't store enough significant digits for their difference to be correct and at the time of dividing by dx, that error becomes amplified.
