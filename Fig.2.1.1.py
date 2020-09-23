import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import gridspec
import matplotlib.patches as patches

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
				#return r'$\frac{%s}{%s}$'%(latex,den)
				return r'${%s}/{%s}$'%(latex,den)
			elif num==-1:
				#return r'$\frac{-%s}{%s}$'%(latex,den)
				return r'${-%s}/{%s}$'%(latex,den)
			else:
				#return r'$\frac{%s%s}{%s}$'%(num,latex,den)
				return r'${%s%s}/{%s}$'%(num,latex,den)
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


dt = np.pi / 32
t_start = -np.pi
t_end = 5 * np.pi
init_phase = np.pi/6

interval = np.arange(t_start, t_end, dt)

def wave(t, alpha):
    return np.sin(t + alpha)

def on_circle(t, alpha):
    x = np.cos(t + alpha)
    y = np.sin(t + alpha)
    return x, y

fig = plt.figure(figsize = (10, 2.5))
gs = gridspec.GridSpec(1, 2, width_ratios = [1, 3])
ax0 = plt.subplot(gs[0])
ax1 = plt.subplot(gs[1], sharey = ax0)

plt.title(r"$\omega = 1$")

# circle movement
circ = patches.Circle(xy=(0, 0), radius = 1.0, fc='w', ec='black')
ax0.add_patch(circ)
ax0.set_xlim(-1.0, 1.0)
ax0.set_ylim(-1.0, 1.0)
ax0.vlines(0, -1, 1, color="black", alpha = 0.5)
ax0.hlines(0, -1, 1, color="black", alpha = 0.5)

# Keep the axes as a square
ax0.set_aspect(1.0/ax0.get_data_ratio())
ax1.set_aspect(3.0/ax0.get_data_ratio())

# time response
ax1.plot(interval, wave(interval, init_phase), 
	ls = '--', c = "blue", alpha = 0.3)
ax1.set_xlim(t_start, t_end)
ax1.set_ylim(-1, 1)
ax1.xaxis.set_major_locator(plt.MultipleLocator(np.pi/2))
ax1.xaxis.set_major_formatter(plt.FuncFormatter(multiple_formatter()))
ax1.grid(True)

ax1.hlines(0, t_start, t_end, color ="black", alpha = 0.5)
ax1.vlines(0, -1, 1, color ="black", alpha = 0.5)
ax1.set_xlabel(r'$t \rightarrow$')
ax1.set_ylabel(r'$A_m \rightarrow$')

plt.subplots_adjust(top=0.9, bottom=0.2, right=0.9, left=0.1, wspace = 0.3)

ims = []
for t in interval:
	x0, y0 = on_circle(t, init_phase)
	p = ax0.plot([0, x0], [0, y0], c = 'black')\
		+ ax0.plot([0, 0], [0, y0], c = 'blue', lw = 3)\
		+ ax0.plot([0, x0], [y0, y0], ls = '--', c = 'black', lw = 1)\
		+ ax0.plot(0, y0, marker = 'o', c = 'blue', ms = 5)\
		+ ax0.plot(x0, y0, marker = 'o', c = 'black', ms = 5)\
		+ ax1.plot(t, wave(t, init_phase), marker = 'o', c ='blue', ms= 5)\
		+ ax1.plot([t, t], [0, wave(t, init_phase)], c = 'blue', lw = 3)
	ims.append(p)

ani = animation.ArtistAnimation(fig, ims, interval = 100, repeat=True)

#ani.save('pendulum.gif', writer='imagemagick')

plt.show()



