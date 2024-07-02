import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(1000)
y = np.random.randn(1000)

plt.hexbin(x, y, gridsize=30, cmap='Blues')
plt.colorbar(label='count in bin')
plt.title('Hexbin Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
