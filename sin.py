import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import gridspec

fig = plt.figure(figsize = (10,2))

gs = gridspec.GridSpec(1, 2, width_ratios = [3, 1])
ax1 = fig.add_subplot(gs[0])
ax2 = fig.add_subplot(gs[1])

x = np.arange(0, 4 * 2 * np.pi, 0.1)

ims = []
for a in range(50):
    y = np.sin(x)
    line, = ax1.plot(x, y, "blue")
    line, = ax1.plot(x, y, "blue")
    ims.append([line])

ani = animation.ArtistAnimation(fig, ims)

#ani.save('anim.gif', writer="imagemagick")
#ani.save('anim.mp4', writer="ffmpeg")

plt.show()
