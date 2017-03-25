import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# read data into a numpy array
data = np.genfromtxt("../Data/abaqus_1.rpt", comments="X")

column = 450

time = data[:,0]
acc = data[:,column]

# determine sample frequency and Nyquist frequency
sample_freq = round(len(time) / time[-1], 0)
Nyquist_freq = sample_freq / 2

# design Butterworth filter
N  = 8                        # filter order
Wn = 40.0 / Nyquist_freq      # normalized cut-off frequency

# numerator (b) and denominator (a) polynomials of transfer function
b, a = signal.butter(N, Wn, btype="low", analog=False, output="ba")

# apply filter
accf = signal.lfilter(b, a, acc)

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(1,1,1)

# plot data
ax.plot(time, acc, linewidth=.5, color="#999999", label="raw")
ax.plot(time, accf, linewidth=2, color="darkred", label="filtered")

ax.axhline(0, linestyle="--", color="black")

# set ticks manually
ax.set_xticks(np.arange(0.0, 1.1, 0.2))
ax.set_xticks(np.arange(0.0, 1.1, 0.1), minor=True)
#ax.set_yticks(np.arange(-10000, 10001, 5000))
#ax.set_yticks(np.arange(-10000, 10001, 2500), minor=True)

# display both major and minor ticks
ax.grid(which='major', alpha=1.0)
ax.grid(which='minor', alpha=1.0)

ax.tick_params(labelsize=13, pad=8)

# set labels for the axes
ax.set_xlabel(r"time [s]", fontsize=14)
ax.set_ylabel(r"acceleration [$\mathregular{m/s^2}$]", fontsize=14)

# set limits for the axes
ax.set_xlim(None, None)
ax.set_ylim(None, None)

# show legend in the top right corner
ax.legend(loc=1, fontsize=None)

# show plot with tight layout and save it
plt.tight_layout()
plt.savefig("../graphs/img.svg", dpi=150)
plt.show()

print len(time), min(time), max(time)
print len(acc), min(acc), max(acc)
print len(accf), min(accf), max(accf)