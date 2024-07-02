import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.1, 4, 0.5)
y = np.exp(-x)
error = y * 0.1

plt.errorbar(x, y, yerr=error, fmt='o')
plt.title('Error Bar Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
