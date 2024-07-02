import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 6)
y1 = np.array([1, 2, 4, 8, 16])
y2 = np.array([1, 3, 6, 10, 15])

plt.fill_between(x, y1, label='Series 1', alpha=0.5)
plt.fill_between(x, y2, label='Series 2', alpha=0.5)
plt.title('Area Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()
