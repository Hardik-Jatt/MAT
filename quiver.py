import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2, 0.2)
y = np.arange(0, 2, 0.2)
X, Y = np.meshgrid(x, y)
U = np.cos(X) * Y
V = np.sin(Y) * X

plt.quiver(X, Y, U, V)
plt.title('Quiver Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
