#This checks whether the planets are still in resonance or not. 
import sys
import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.cm as cm
import re

colors=['b','g','m','r','c','y']

file_name=str(sys.argv[1])

fos = open(''+file_name, 'r')
time, dE, N, mig_rate, damp1, damp2, migtime, DT, a1, e1, a2, e2, phi1, phi2, phi3, m1, m2, taua1, taue1, taua2, taue2 = np.loadtxt(fos, delimiter=',', unpack=True)

ms=6
fig, axes = plt.subplots(nrows=5, ncols=1, figsize=(10,13), sharex=True)
plt.subplots_adjust(hspace = 0.2)

P1 = (a1[0]**3 /0.92)**0.5 * 2*np.pi
time /= P1

#plot
axes[0].plot(time, phi1, '.', ms=ms, markeredgecolor='none', label='phi 1')
axes[0].plot(time, phi2, '.', ms=ms, markeredgecolor='none', alpha=0.15, label='phi 2')
#axes[0].plot(time, phi3, '.', ms=ms, markeredgecolor='none', label='phi 3')
#axes[0].plot(time, dE,'o',ms=ms, markeredgecolor='none')
axes[1].plot(time, a1, 'o', ms=ms, markeredgecolor='none')
axes[1].plot(time, a2, 'o', ms=ms, markeredgecolor='none')
axes[2].plot(time, (a2/a1)**(1.5), 'o', ms=ms, markeredgecolor='none')
axes[3].plot(time, e1, 'o', ms=ms, markeredgecolor='none', label='planet 1')
axes[3].plot(time, e2, 'o', ms=ms, markeredgecolor='none', label='planet 2')

P2 = a2**1.5
axes[4].plot(time, taue1/P2, 'o', ms=2*ms, color='black', markeredgecolor='none', label='tau_e1')
axes[4].plot(time, taue2/P2, 'o', ms=ms, color='green', markeredgecolor='none', label='tau_e2')
axes[4].plot(time, taua2/P2, 'o', ms=ms/3, color='red', markeredgecolor='none', label='tau_a1 ')
axes[4].set_yscale('log')
axes[4].legend(loc='upper left', fontsize=10)

plot_bounds = 1
if plot_bounds == 1:
    mig_time = migtime[0]/P1
    D_T = DT[0]/P1
    axes[0].plot([mig_time, mig_time], [0, 2*np.pi], 'r--',lw=4)
    axes[0].plot([D_T, D_T], [0, 2*np.pi], 'c--',lw=4)
    axes[1].plot([mig_time, mig_time], [0, max(a2)], 'r--',lw=4)
    axes[1].plot([D_T, D_T], [0, max(a2)], 'c--',lw=4)
    axes[2].plot([mig_time, mig_time], [1, 3], 'r--',lw=4)
    axes[2].plot([D_T, D_T], [1, 3], 'c--',lw=4)
    axes[3].plot([mig_time, mig_time], [0, max([max(e1),max(e2)])], 'r--',lw=4)
    axes[3].plot([D_T, D_T], [0, max([max(e1),max(e2)])], 'c--',lw=4)

#labelling
#axes[0].set_xscale('log')
axes[0].legend(loc='upper left')
#axes[0].set_xlim([100,max(time)])
#axes[0].set_xlim([18000,19000])
axes[0].set_ylabel('Resonant Angle', fontsize=13)
axes[1].set_ylabel('Semi-major axis', fontsize=13)
axes[2].set_ylabel('Period Ratio', fontsize=13)
axes[3].set_ylabel('Eccentricity', fontsize=13)
axes[4].set_xlabel('Orbital Period of Inner Planet', fontsize=13)
axes[4].set_ylabel('Damping', fontsize=13)
axes[4].set_yscale('log')

#axes[0].set_xlim([1e4, 1.01e4])

file_output_name = re.sub('\.txt$', '', file_name)
plt.savefig(file_output_name+'_orbit.png')
#plt.show()
