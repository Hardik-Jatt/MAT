import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3.0, 3.0, 100)
y = np.linspace(-3.0, 3.0, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) ** 10 + np.cos(10 + Y * X) * np.cos(X)

plt.contour(X, Y, Z, levels=20, cmap='RdGy')
plt.title('Contour Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
