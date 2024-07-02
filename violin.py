import matplotlib.pyplot as plt
import numpy as np

data = [np.random.normal(0, std, 100) for std in range(1, 4)]

plt.violinplot(data)
plt.title('Violin Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
