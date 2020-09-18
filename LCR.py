import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from numpy import sin

R = 2
C = 0.03
L = 0.01
f = 60
omega = 2.0 * np.pi * f
Em = 1

def func(t, x):
	f = []
	f.append(x[1]/C)
	f.append((-R * x[1] - x[0] + Em * sin(omega * t))/L)
	return f

dt = 0.001
t_start = 0.0
t_end = 0.5
t_interval = (t_start, t_end)

x0 = [0.1, 0]
y = []

solved = solve_ivp(func, t_interval, x0, dense_output=True)
t = np.linspace(t_start, t_end, 1000)
y = solved.sol(t)

fig = plt.figure(figsize=(10,3))
ax = fig.add_subplot(111)
ax.plot(t, y[0], label = "$v$")
ax.plot(t, y[1], label = "$i$")
plt.xlabel("$t$")
plt.ylabel("$x$")
plt.legend()

plt.show()
