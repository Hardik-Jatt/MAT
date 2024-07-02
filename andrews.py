import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import andrews_curves

# Sample data
data = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [2, 3, 4, 5, 6],
    'C': [3, 4, 5, 6, 7],
    'Class': ['X', 'X', 'Y', 'Y', 'Z']
})

andrews_curves(data, 'Class')
plt.title('Andrews Curves')
plt.show()
