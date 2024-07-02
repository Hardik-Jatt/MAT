import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import parallel_coordinates

# Sample data
data = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [2, 3, 4, 5, 6],
    'C': [3, 4, 5, 6, 7],
    'Class': ['X', 'X', 'Y', 'Y', 'Z']
})

parallel_coordinates(data, 'Class')
plt.title('Parallel Coordinates')
plt.show()
