import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.step(x, y, where='mid')
plt.title('Step Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
