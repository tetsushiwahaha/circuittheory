#!/usr/bin/env python 
'''

'''
import numpy as np
import matplotlib.pyplot as plt  
from scipy.integrate import solve_ivp
from matplotlib.backends.backend_pdf import PdfPages

base = 10
fig = plt.figure(figsize = (base, base/16*5))		# create a figure
ax = fig.add_subplot(111)					# create axes 
fig.subplots_adjust(bottom=0.3)

# PLOT options 
plt.xticks(fontsize=10) 
plt.yticks(fontsize=10) 

# AXES helpers
ax.set_xlabel(r'$t \longrightarrow$', fontsize=12)
ax.set_ylabel(r'$\varphi(t) \longrightarrow $', fontsize=12)
#ax.set_xlim([0, 3])
#ax.set_ylim([-0.5, 3.0])

x_list = np.arange(0, 0.3, 1e-4)

R = 2
omega = 377
L = 0.1
psi = 1.0
Em = 1
z = np.sqrt(R * R + omega*omega);



def func(t, x):
	f = (-R * x + Em * np.sin(omega * t + psi))/L
	return f


dt = 0.001
t_start = 0.0
t_end = 0.3
t_interval = (t_start, t_end)

x0 = [0, 0]
y = []

solved = solve_ivp(func, t_interval, x0, dense_output=True)

t = np.linspace(t_start, t_end, 1000)

y = solved.sol(t)


### DATA PLOTTING 
ax.plot(t, y[0], label = 'total', color = 'BLUE', linewidth = 0.8)

ax.legend(loc='best') # legend
#ax.legend(loc=0)
ax.grid(c='gainsboro', zorder=2)
#ax.grid(True)

# Publish a PDF in the same time.
#
pdf = PdfPages('snapshot.pdf')
pdf.savefig()
pdf.close()

plt.show()

