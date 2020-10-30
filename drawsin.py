#!/usr/bin/env python 

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import gridspec
import matplotlib.patches as patches
from matplotlib.backends.backend_pdf import PdfPages

####### some codes from stackoverflow
def multiple_formatter(denominator=2, number=np.pi, latex='\pi'):
	def gcd(a, b):
		while b:
			a, b = b, a%b
		return a
	def _multiple_formatter(x, pos):
		den = denominator
		num = np.int(np.rint(den*x/number))
		com = gcd(num,den)
		(num,den) = (int(num/com),int(den/com))
		if den==1:
			if num==0:
				return r'$0$'
			if num==1:
				return r'$%s$'%latex
			elif num==-1:
				return r'$-%s$'%latex
			else:
				return r'$%s%s$'%(num,latex)
		else:
			if num==1:
				return r'$\frac{%s}{%s}$'%(latex,den)
			elif num==-1:
				return r'$\frac{-%s}{%s}$'%(latex,den)
			else:
				return r'$\frac{%s%s}{%s}$'%(num,latex,den)
	return _multiple_formatter

class Multiple:
	def __init__(self, denominator=2, number=np.pi, latex='\pi'):
		self.denominator = denominator
		self.number = number
		self.latex = latex
	def locator(self):
		return plt.MultipleLocator(self.number / self.denominator)
	def formatter(self):
		return plt.FuncFormatter(multiple_formatter(self.denominator, self.number, self.latex))
####################


params = {'text.usetex': True,
          #'text.latex.preamble': r'\usepackage{newtxtext,newtxmath}',
          'legend.fontsize': 12, 'axes.labelsize': 12,
          'axes.titlesize': 12, 'xtick.labelsize' :12,
          'ytick.labelsize': 12, 'font.family': 'serif',
          'grid.color': 'k', 'grid.linestyle': ':',
          'grid.linewidth': 0.5,
         }
#plt.rcParams.update(params)

x_list=[] 
y_list=[] 

base = 10
fig = plt.figure(figsize = (base, 5/16*base))		# create a figure
ax = fig.add_subplot(111)					# create axes 
fig.subplots_adjust(bottom=0.3)

# PLOT options 
plt.xticks(fontsize=10) 
plt.yticks(fontsize=10) 

plt.title(r'$\omega = 60$')

omega = 60

# AXES helpers
ax.set_xlabel(r'$t \longrightarrow$', fontsize=12)
ax.set_ylabel(r'$x(t) \longrightarrow $', fontsize=12)
#ax.set_xlim([-0.1, 0.5])
#ax.set_ylim([])
tau = 2*np.pi
major = Multiple(omega*2, tau, r'2\pi')
minor = Multiple(omega*4, tau, r'2\pi')
ax.xaxis.set_major_locator(major.locator())
ax.xaxis.set_minor_locator(minor.locator())
ax.xaxis.set_major_formatter(major.formatter())
ax.grid(True)
ax.grid(c='gainsboro', zorder=3)

x_list = np.arange(-np.pi/60, 3*np.pi/60, 0.001)


### DATA PLOTTING 
ax.plot(x_list, np.sin(omega*x_list - np.pi/3),
	label = r'$\sin(\omega t - \pi/3)$', color = 'RED', linewidth = 0.8)
ax.plot(x_list, np.sin(omega*x_list - np.pi/6),
	label = r'$\sin(\omega t - \pi/6)$', color = 'BLUE', linewidth = 0.8)
ax.plot(x_list, np.sin(omega*x_list),
	label = r'$\sin\omega t$', color = 'black', linewidth = 0.8)

#ax.legend(loc='best') # legend
ax.legend(loc='upper right') 

# Publish a PDF in the same time.
#
pdf = PdfPages('snapshot.pdf')
pdf.savefig()
pdf.close()

plt.show()



