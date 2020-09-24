import numpy as np
import matplotlib.pyplot as plt

def plot_cp(func): 
	fig, ax = plt.subplots(figsize = (8, 8))
	ax.grid()

	lim = [-2.5, 2.5]
	ax.set_xlim(lim)
	ax.set_ylim(lim)

	plt.quiver(lim[0],0,lim[1]-lim[0], 0,
		angles='xy', scale_units='xy',
		width=0.005, headwidth=10, headlength=10, 
		headaxislength=5, scale=1)
	plt.text(1.05*lim[1],0.02*lim[0], 'Re')

	plt.quiver(0,lim[0],0,lim[1]-lim[0],
		angles='xy', scale_units='xy',
		width=0.005, headwidth=10, headlength=10,
		headaxislength=5, scale=1)
	plt.text(0.03*lim[0],1.05*lim[1], 'Im')

	plt.text(0.1*lim[0],0.1*lim[0], '$O$')

	xt = list(ax.get_xticks())
	for i in [0, np.floor(lim[0]), np.ceil(lim[1])]:
		xt.remove(i)
	ax.set_xticks(xt)
	ax.set_yticks(xt)

	imlabel=[]
	for ticks in ax.get_yticks():
		imlabel.append(str(ticks)+" j")
	ax.set_yticklabels(imlabel)

	ax.spines['bottom'].set_position('center')
	ax.spines['left'].set_position('center')
	ax.spines['right'].set_visible(False)
	ax.spines['top'].set_visible(False)
	return


theta=np.linspace(-np.pi, np.pi, 1000) # theta=omega*T
func = 1+np.exp(-2j*theta)

plot_cp(func) # 複素平面上に描く

plt.plot(np.real(func),np.imag(func))

func = 1.3 + 0.5j
plt.plot(np.real(func),np.imag(func))


plt.show()


'''
	referred:
	https://qiita.com/ikets/items/67e03c9cdf1d873d7f2f
'''
