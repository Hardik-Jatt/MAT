import matplotlib.pyplot as plt

# Data
categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]

# Plot
plt.bar(categories, values, color='blue')
plt.title('Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()
