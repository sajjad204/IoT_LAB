import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

pltInterval = 50

t = np.arange(0.01, 10.0, 0.01)
ss1 = np.sin(2 * np.pi * t)
ss2 = np.sin(3 * np.pi * t)
ss3 = np.sin(4 * np.pi * t)
ss4 = np.sin(5 * np.pi * t)
yy = [ss1,ss2,ss3,ss4]
color = ['r', 'g', 'b', 'y'] 
title = ['Detector A', 'Detector B', 'Detector C', 'Detector D']

def example_plot(ax,i,y,k):
    ax.plot(t[:i], y[:i], color=color[k], linestyle='--')
    ax.set_xlabel('Time', fontsize=12)
    ax.set_ylabel('Detector Output', fontsize=12)
    ax.set_title(title[k], fontsize=14)
    
fig, axs = plt.subplots(nrows=2, ncols=2, constrained_layout=True)

def update(i):
    for k,(ax,y) in enumerate(zip(axs.flat,yy)):
        example_plot(ax,i,y,k)

anim = FuncAnimation(fig, update, frames=50, interval=pltInterval, repeat=False)
plt.show()