import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from statistics import variance, stdev
HZ = 360

data = np.genfromtxt('100_V5.dat',
                     dtype=float,
                     delimiter='\n')

# plt.plot(data)
# plt.show()

# plt.plot(data[:1*HZ])
# plt.savefig('1sek_100_V5.jpg')
# plt.close()

# plt.plot(data[:2*HZ])
# plt.savefig('2sek_100_V5.jpg')
# plt.close()


a = 75
b = 370
# plt.plot(data[a:b])
# plt.savefig('okres_100_V5.jpg')
# plt.close()

beats_per_min = (HZ / (b - a)) * 60
print(beats_per_min)

indices, heights = find_peaks(data[:4*HZ], 0.2)


peak_heights = []
for indice in indices:
    peak_heights.append(data[indice])

# plt.plot(data[:4*HZ])
# plt.scatter(indices, peak_heights, c='red')
# plt.show()


def window_indices(seq, n=2):
    i = 0
    while i+1 < len(seq):
        yield seq[i:i+n]
        i += 1

def distances(seq):
    for i, j in window_indices(seq, 2):
        yield j-i

all_peaks_indices, _ = find_peaks(data, 0.2)

print(variance(distances(all_peaks_indices)))

print(stdev(distances(all_peaks_indices)))
