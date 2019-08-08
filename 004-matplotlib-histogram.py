""" MARKDOWN
---
YamlDesc: CONTENT-ARTICLE
Title: Python MatPlotLib
MetaDescription: Python MatPlotLib
MetaKeywords: Python MatPlotLib Draw Graphs, histogram
Author: (c) Venkata Bhattaram / tinitiate
ContentName: python-matplotlib-histogram
---
MARKDOWN """

""" MARKDOWN
# Histogram
* Histogram, has TWO parts, Data Frequency (Height of the Bars in the Graph)
  and Data Interval (Width of the Bars in the Graph).
* Interval is also called as the **BIN** (or "bucket") the range of values.
* Intervals (BINs) are usually specified as consecutive, non-overlapping values
  of a  variable. They are adjacent, and are often of equal size.
* Frequency, is the value of data over the Interval, this forms the height
  of the bar.
MARKDOWN """


""" MARKDOWN
# Histogram Linear Data
* 2D Histogram with random integer values, and their value counts in a range
  of intervals
MARKDOWN """

# MARKDOWN ```
import numpy as np
import random
import matplotlib.pyplot as plt

# Generate 20, Random Integers
x =  random.sample(range(1, 100), 20)
print(x)

# Divide the distrubution into 5 intervals or bins
num_bins = 5

# Plot the intervals in a histogram
n, bins, patches = plt.hist(x, num_bins, facecolor='b')

plt.xlabel('Occurrence Data Values')
plt.ylabel('Data Values')
plt.title('Values and Counts Distrubution Histogram')
plt.grid(True)
plt.show()
# MARKDOWN ```
