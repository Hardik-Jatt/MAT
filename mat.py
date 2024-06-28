import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Basic plot
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='Sine wave')
plt.plot(x, y2, label='Cosine wave')
plt.xlabel('X axis label')
plt.ylabel('Y axis label')
plt.title('Basic Plot')
plt.legend()
plt.grid(True)
plt.savefig('basic_plot.png')
plt.show()

# Customizing plots with colors, markers, and line styles
plt.figure(figsize=(10, 6))
plt.plot(x, y1, color='blue', linestyle='-', linewidth=2, marker='o', label='Sine wave')
plt.plot(x, y2, color='red', linestyle='--', linewidth=2, marker='x', label='Cosine wave')
plt.xlabel('X axis label')
plt.ylabel('Y axis label')
plt.title('Customized Plot')
plt.legend()
plt.grid(True)
plt.savefig('customized_plot.png')
plt.show()

# Creating subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Subplot 1
axs[0, 0].plot(x, y1, 'tab:blue')
axs[0, 0].set_title('Sine Wave')
axs[0, 0].grid(True)

# Subplot 2
axs[0, 1].plot(x, y2, 'tab:orange')
axs[0, 1].set_title('Cosine Wave')
axs[0, 1].grid(True)

# Subplot 3
axs[1, 0].plot(x, y1 + y2, 'tab:green')
axs[1, 0].set_title('Sine + Cosine')
axs[1, 0].grid(True)

# Subplot 4
axs[1, 1].plot(x, y1 - y2, 'tab:red')
axs[1, 1].set_title('Sine - Cosine')
axs[1, 1].grid(True)

fig.tight_layout(pad=3.0)
plt.savefig('subplots.png')
plt.show()

# Scatter plot
np.random.seed(0)
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
area = (30 * np.random.rand(50))**2

plt.figure(figsize=(10, 6))
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.xlabel('X axis label')
plt.ylabel('Y axis label')
plt.title('Scatter Plot')
plt.grid(True)
plt.savefig('scatter_plot.png')
plt.show()

# Histogram
data = np.random.randn(1000)

plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, alpha=0.7, color='blue', edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.grid(True)
plt.savefig('histogram.png')
plt.show()

# Bar plot
categories = ['A', 'B', 'C', 'D']
values = [3.5, 7.2, 5.8, 6.1]

plt.figure(figsize=(10, 6))
plt.bar(categories, values, color=['blue', 'orange', 'green', 'red'])
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot')
plt.grid(True)
plt.savefig('bar_plot.png')
plt.show()

# Pie chart
labels = 'A', 'B', 'C', 'D'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)

plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Pie Chart')
plt.savefig('pie_chart.png')
plt.show()

# Box plot
data = np.random.randn(100, 4)

plt.figure(figsize=(10, 6))
plt.boxplot(data, patch_artist=True)
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Box Plot')
plt.grid(True)
plt.savefig('box_plot.png')
plt.show()
