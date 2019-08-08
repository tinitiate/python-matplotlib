""" MARKDOWN
---
YamlDesc: CONTENT-ARTICLE
Title: Python MatPlotLib
MetaDescription: Python MatPlotLib
MetaKeywords: Python MatPlotLib Draw Graphs, line graph from python
Author: (c) Venkata Bhattaram / tinitiate.com
ContentName: python-matplotlib-linegraph
---
MARKDOWN """

""" MARKDOWN
# Line Graph
* Line Graph has a X and Y Axis
* Datasets are usually on the Y-Axis and the scale is the X-Axis
MARKDOWN """

# MARKDOWN ```
import numpy as np
from matplotlib import pyplot as plt

# Title Matplotlib demo
plt.title("SyntaxBoard Line Graph Demo")

# x axis caption
plt.xlabel("Years")

# y axis caption
plt.ylabel("Dollors")

# Data Set Values
y1 = [10, 12, 15, 16, 18, 19]
y2 = [2,3,5,6,8,9]
y3 = [12,23,35,16,8,19]

# Y-Axis data set
x = [2000, 2001, 2002, 2003, 2004, 2005]


# Plot a Line Graph, in red color
plt.plot(x,y1,'r')

# Plot another Line Graph, in blue color
plt.plot(x,y2,'b')

# Plot another Line Graph, in green color
plt.plot(x,y3,'g')

# Render the Graph
plt.show()
# MARKDOWN ```


""" MARKDOWN
# Line Graph Styles
* Markers, Line Width, Line Style and color
* Other graph level attributes like Legend
MARKDOWN """
# MARKDOWN ```
import numpy as np
from matplotlib import pyplot as plt

# Title Matplotlib demo
plt.title("SyntaxBoard Line Graph Demo")

# x axis caption
plt.xlabel("Years")

# y axis caption
plt.ylabel("Dollors")

# Data Set Values
y1 = [10, 12, 15, 16, 18, 19]
y2 = [2, 3, 5, 6, 8, 9]
y3 = [12, 23, 35, 56, 8, 9]

# Y-Axis data set
x = [2000, 2001, 2002, 2003, 2004, 2005]

# multiple line plot
plt.plot( x, y1, marker='o', markerfacecolor='blue', markersize=10, color='skyblue', linestyle=':', linewidth=4, label="travel")
plt.plot( x, y2, marker='^', color='g', linestyle='-.', linewidth=2, label="supplies")
plt.plot( x, y3, marker='H', color='olive', linewidth=2, linestyle='dashed', label="food")
plt.legend()

# Render the Graph
plt.show()

# MARKDOWN ```


""" MARKDOWN
# Line Graph SINE and COSINE waves
* Line Style and color and Label
* Graph with curve data
MARKDOWN """
# MARKDOWN ```
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 500)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1 - 0.2, color='y', linestyle=':', label='SINE Wave')
plt.plot(x, y2 - 0.2, color='r', linestyle='-.', label='COSINE Wave')

plt.legend()
plt.show()

# MARKDOWN ```
