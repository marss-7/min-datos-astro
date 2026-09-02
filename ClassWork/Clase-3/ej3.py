import numpy as np
import matplotlib.pyplot as plt

# sin + cos
x = np.linspace(0, 10, 100)
sin = np.sin(x)
cos = np.cos(x)

# 3, histograms
dist = np.random.randn(1000)

#graph!

figs, axs = plt.subplots(2,2)
axs[0,0].plot(x, sin)
axs[0,1].plot(x, cos)
axs[1,0].hist(dist, bins=10, color='magenta')
axs[1,1].hist(dist, bins=50, color='purple')
axs[0,0].set_title("sin")
axs[0,1].set_title("cos")
axs[1,0].set_title("hist, bins = 10")
axs[1,1].set_title("hist, bins = 50")

plt.tight_layout()
plt.show()
