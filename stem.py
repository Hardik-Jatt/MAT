import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.1, 2 * np.pi, 10)
y = np.cos(x)

plt.stem(x, y)
plt.title('Stem Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
