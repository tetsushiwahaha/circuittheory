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

total = -Em/z * np.sin(psi - np.arctan(omega * L/R)) * np.exp(-R/L * x_list)\
	+ Em/z * np.sin(omega * x_list + psi - np.arctan(omega * L /R))

first = -Em / z * np.sin(psi - np.arctan(omega * L / R))\
	* np.exp(-R/L * x_list) 
second = Em / z * np.sin(omega * x_list + psi - np.arctan(omega * L /R)) 

e = Em * np.sin(omega * x_list + psi)/1000



### DATA PLOTTING 
ax.plot(x_list, total, label = 'total', color = 'BLUE', linewidth = 0.8)
ax.plot(x_list, first, label = '1st', color = 'RED', linewidth = 0.8)
ax.plot(x_list, second, label = '2nd', color = 'GREEN', linewidth = 0.8)
ax.plot(x_list, e, label = r'$E(t)$', color = 'black', linewidth = 0.5)
#ax.plot(x_list, y_list) 
#ax.plot(x_list, y_list, color='RED',linewidth=4.0) 
#ax.plot(x_list, y_list, marker='o') 
#ax.plot(x_list, y_list,'o') 
#ax.hlines([y1,y2], xmin, xmax, linestyles="dashed")  

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

