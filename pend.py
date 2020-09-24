import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

alpha = 0
g = 9.8  #m/s2
L = 0.1  #m
omega = np.sqrt(g/L)
theta_max = np.pi / 6
dt = 0.01
t = np.arange(0, 2 + dt, dt)

#位相の計算
def theta(ts):
    return theta_max*np.cos(omega*ts + alpha)

#位置の計算
def theta_position(ts):
    x = L * np.sin(theta(ts))
    z = -L * np.cos(theta(ts))
    return x, z


fig, ax = plt.subplots(1,2, figsize = (14,6))
#axes_set_linewidth(ax[0], t=0, b=0, r=0, l=0)
#axes_set_linewidth(ax[1], t=0, b=2, r=0, l=2)

ax[0].set_xticks([])
ax[0].set_yticks([])
ax[0].set_xlim(-0.06, 0.06)
ax[0].set_ylim(-0.12, 0.02)
ax[0].vlines(0, -0.1, 0, linestyle = '--')
ax[0].hlines(0, -1, 1)

ax[1].plot(t, theta(t))
ax[1].set_xlim(0,2.2)
ax[1].set_ylim(-0.6,0.6)
ax[1].hlines(0,0,2.2, color='black', linestyle='--')
ax[1].set_xlabel('Time [s]')
ax[1].set_ylabel(r'$\theta$ [rad]')

plt.subplots_adjust(top=0.9, bottom=0.2, right=0.9, left=0.2, wspace = 0.3)

ims = []
for i in t:
	x, y = theta_position(i)
	p = ax[0].plot([0,x], [0,y], color = 'black')\
	+ ax[0].plot(x, y, marker = 'o', color = 'red', markersize = 15)\
	+ ax[1].plot(i, theta(i), marker='o', color='darkblue', markersize=10)
	ims.append(p)

ani = animation.ArtistAnimation(fig, ims, interval=50, repeat=True)

#ani.save('pendulum.gif', writer='imagemagick')

plt.show()



