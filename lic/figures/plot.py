import numpy as np
import matplotlib.pyplot as plt

alphaY_obs = 0.00939052984
beta2 = 41/(12*np.pi)

def alphaf(logk):
    return alphaY_obs/(1-beta2*alphaY_obs*logk)

x = np.linspace(0.1, 97.3, num=500)
print(x)
y = [alphaf(kk) for kk in x]
x = [np.e**a for a in x]
print(y)
plt.style.use("ggplot")
fig, ax = plt.subplots(figsize=(9, 6), dpi=100)
plt.xlabel(r'$\Lambda \ / \ m_r$')
plt.ylabel(r'effective $\alpha_Y$', rotation="horizontal")
plt.xlim([1, 1000*max(x)])
plt.ylim([0.006, 1.05])
ax.yaxis.set_label_coords(0.02, 1.02)
# ax.xaxis.set_label_coords(1.05, 0.02)
ax.set_xscale("log")
ax.set_yscale("log")

ax.plot(x,y, color=(216/255, 79/255, 0), linewidth=3, label =r'effective $\alpha_Y$')
ax.axvline(x = 3.1623e42, color = 'firebrick', label = 'pole location', linestyle="dashed", linewidth=1.7)
plt.legend()
plt.savefig("plot.jpg", dpi=600)
plt.show()