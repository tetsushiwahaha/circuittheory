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
ax.set_ylabel(r'$v(t) \longrightarrow $', fontsize=12)

t_end = 1.0
x_list = np.arange(0, t_end, 1e-3)

R1 = 2
R2 = 3
C = 0.1
E = 1

v = E * R2 / (R1 + R2) * (1 - np.exp (-(R1+R2)* x_list / (C*R1*R2)))

vf = E * R2 / (R1 + R2)

### DATA PLOTTING 
ax.plot(x_list, v, label = r'$v(t)$', color = 'BLUE', linewidth = 2)
ax.plot([0, 0], [0, vf], c = 'orange', ls = '--', lw = 1)
ax.plot([0, t_end], [vf, vf], c = 'orange', ls = '--', lw = 1)
ax.legend(loc='best') # legend
ax.grid(c='gainsboro', zorder=2)

# Publish a PDF in the same time.
pdf = PdfPages('snapshot.pdf')
pdf.savefig()
pdf.close()

plt.show()

