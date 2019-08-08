""" MARKDOWN
---
YamlDesc: CONTENT-ARTICLE
Title: Python MatPlotLib Scatter Graph
MetaDescription: Python MatPlotLib scatterplot
MetaKeywords: Python MatPlotLib Draw Graphs, scatter Plot
Author: (c) Venkata Bhattaram / tinitiate.com
ContentName: python-matplotlib-scatterplot
---
MARKDOWN """

""" MARKDOWN
# Scatter Plot
* A Scatterplot displays dot representation of, the position on the 
  X (horizontal) and Y (vertical) axis
* Multiple values from a sets of TWO DOTS can indicate the properties of data, 
  each data set can be assigned a different color for analysis.
MARKDOWN """

# MARKDOWN ```
import numpy as np 
from matplotlib import pyplot as plt 

# Data Set 1
x1 = np.random.randn(3000)
y1 = np.random.randn(3000)

# Data Set 2
x2 = np.random.randn(6000)
y2 = np.random.randn(6000)

# get Axes object from subplots
fig, ax = plt.subplots()

# s is dot size on graph, c is color
ax.scatter(x1, y1, s=.7, c='b')
ax.scatter(x2, y2, s=.7, c='r')

# ax.set_xlim(1, 6.5)
# Show the grid lines
plt.grid(True)

# Show the graph
plt.show()

# MARKDOWN ```
