import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(10, 100)
colors = ['C{}'.format(i) for i in range(10)]

plt.eventplot(data, colors=colors)
plt.title('Event Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
