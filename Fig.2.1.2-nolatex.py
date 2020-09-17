import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import gridspec

dt = 0.1
t_start = -np.pi
t_end = 5 * np.pi

lead = np.pi/3
lag =  -np.pi/3

interval = np.arange(t_start, t_end, dt)

def wave(t, alpha):
    return np.sin(t + alpha)

def on_circle(t):
    x = np.cos(t)
    y = np.sin(t)
    return x, y

fig = plt.figure(figsize = (10, 2.5))
gs = gridspec.GridSpec(1, 2, width_ratios = [1, 3])
ax0 = plt.subplot(gs[0])
ax1 = plt.subplot(gs[1])

# circle movement
ax0.set_xlim(-1.2, 1.2)
ax0.set_ylim(-1.2, 1.2)
ax0.vlines(0, -1, 1, color="black", alpha = 0.5)
ax0.hlines(0, -1, 1, color="black", alpha = 0.5)
# Keep the axes as a square
ax0.set_aspect(1.0/ax0.get_data_ratio())

# time response
ax1.plot(interval, wave(interval, 0), ls = '--', c = "red", alpha = 0.3)
ax1.plot(interval, wave(interval, lead), ls = '--', 
	c = "blue", alpha = 0.3)
ax1.plot(interval, wave(interval, lag), ls = '--', 
	c = "green", alpha = 0.3)
ax1.set_xlim(t_start, t_end)
ax1.set_ylim(-1, 1)
ax1.grid(True)

ax1.hlines(0, t_start, t_end, color ="black", alpha = 0.5)
ax1.vlines(0, -1, 1, color ="black", alpha = 0.5)
ax1.set_xlabel('t')
ax1.set_ylabel('Am')

major_ticks = np.arange(t_start, t_end, np.pi/2)
minor_ticks = np.arange(t_start, t_end, np.pi)
ax1.set_xticks(major_ticks)
ax1.set_xticks(minor_ticks, minor=True)




plt.subplots_adjust(top=0.9, bottom=0.2, right=0.9, left=0.1, wspace = 0.3)

ims = []
for t in interval:
	x0, y0 = on_circle(t)
	x1, y1 = on_circle(t + lead)
	x2, y2 = on_circle(t + lag)
	p = ax0.plot([0, x0], [0, y0], c = 'red')\
		+ ax0.plot([0, x1], [0, y1], c = "blue")\
		+ ax0.plot([0, x2], [0, y2], c = "green")\
		+ ax0.plot(x0, y0, marker = 'o', c = 'red', ms = 5)\
		+ ax0.plot(x1, y1, marker = 'o', c = 'blue', ms = 5)\
		+ ax0.plot(x2, y2, marker = 'o', c = 'green', ms = 5)\
		+ ax1.plot(t, wave(t, 0), marker = 'o', c ='red', ms= 8)\
		+ ax1.plot(t, wave(t + lead, 0), marker ='o', c ='blue', ms = 8)\
		+ ax1.plot(t, wave(t + lag, 0), marker ='o', c ='green', ms = 8)
	ims.append(p)

ani = animation.ArtistAnimation(fig, ims, interval = 100, repeat=True)

#ani.save('pendulum.gif', writer='imagemagick')

plt.show()



