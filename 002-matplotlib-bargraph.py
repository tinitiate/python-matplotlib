""" MARKDOWN
---
YamlDesc: CONTENT-ARTICLE
Title: Python MatPlotLib
MetaDescription: Python MatPlotLib
MetaKeywords: Python MatPlotLib Draw Graphs bar graph
Author: (c) Venkata Bhattaram / tinitiate.com
ContentName: python-matplotlib-bargraph
---
MARKDOWN """

""" MARKDOWN
# Bar Graph Vertical
* BarGraph shows relationship between a numerical values and a
  categorical variable.
* Here we demonstrate values on X and Y Axis with color and alignment, where
  the data is on the Y axis and category(lables) is on the X Axis
MARKDOWN """
# MARKDOWN ```
from matplotlib import pyplot as plt

x = [6 ,8 ,10,12,14,16,18,20]
y = [12,16,6 ,2 ,4 ,5 ,6 ,19]

plt.bar(x, y, color = 'y', align = 'center')

plt.title('Bar graph')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()

# MARKDOWN ```


""" MARKDOWN
# Bar Graph Horizontal
* BarGraph shows relationship between a numerical values and a
  categorical variable.
* Here we demonstrate values on X and Y Axis with color and alignment, where
  the data is on the X axis and category(lables) is on the Y Axis
MARKDOWN """
# MARKDOWN ```
import numpy as np
import matplotlib.pyplot as plt

#
data = [300, 1200, 1100]
labels = ('USA', 'China', 'India')
y_pos = np.arange(len(labels))

# Create horizontal bars
plt.barh(y_pos, data)

# Create names on the y-axis
plt.yticks(y_pos, labels)

# Show graphic
plt.show()

# MARKDOWN ```


""" MARKDOWN
# Bar Graph Comparision
* Here we demonstrate comparision values on X and Y Axis with color and
  alignment, where the data is on the Y axis and category(lables) is on the X Axis
  and a comparision data is on the  Y axis and category(lables) is on the X Axis
MARKDOWN """
# MARKDOWN ```
import numpy as np
import matplotlib.pyplot as plt

# width of the bars
barWidth = 0.3

# Bar Graph data sets to compare
comparision_dataset1 = [10, 9, 2]
comparision_dataset2 = [4, 7, 5]

# The x position of bars with spacing
bar_spacing1 = np.arange(len(comparision_dataset1))
bar_spacing2 = [x + barWidth for x in bar_spacing1]

# Create blue bars
plt.bar(bar_spacing1, comparision_dataset1, width = barWidth, color = 'blue', edgecolor = 'black', label='Last-Year')

# Create red bars
plt.bar(bar_spacing2, comparision_dataset2, width = barWidth, color = 'red', edgecolor = 'black', label='This-Year')

# general layout
plt.xticks([c + barWidth for c in range(len(comparision_dataset1))], ['Apples', 'Oranges', 'Peaches'], rotation=90)
plt.ylabel('Data')
plt.legend()

# Show graphic
plt.show()

# MARKDOWN ```


""" MARKDOWN
# Bar Graph Percentage Ratio
* This is a demonstration of Bar Graph that has varying colors to display 
  ratios or percentages of values in the same bar.
MARKDOWN """
# MARKDOWN ```
# libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
 
# Data
r = [0,1,2,3,4]

stock_data = { 'instock': [20, 2, 3, 15, 7]
              ,'sold': [5, 15, 6, 11, 5]
              ,'ordered': [2, 15, 18, 5, 10] }

df = pd.DataFrame(stock_data)

# From raw value to percentage
totals = [i+s+o for i,s,o in zip(df['instock'], df['sold'], df['ordered'])]
inStockData = [t / i * 100 for t,i in zip(df['instock'], totals)]
soldData = [t / s * 100 for t,s in zip(df['sold'], totals)]
orderedData = [t / o * 100 for t,o in zip(df['ordered'], totals)]
 
# plot
barWidth = 0.5
names = ('Cell Phones','Laptops','TVs','Watches','Lamps')
# Create green Bars
plt.bar(r, inStockData, color='red', width=barWidth)
# Create orange Bars
plt.bar(r, soldData, bottom=inStockData, color='#f9bc86', width=barWidth)
# Create blue Bars
plt.bar(r, orderedData, bottom=[i+j for i,j in zip(inStockData, soldData)], color='blue', width=barWidth)
 
# Custom x axis
plt.xticks(r, names)
plt.xlabel("product status")
plt.legend()

# Show graphic
plt.show()


# MARKDOWN ```
