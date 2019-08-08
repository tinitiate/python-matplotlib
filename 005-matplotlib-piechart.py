""" MARKDOWN
---
YamlDesc: CONTENT-ARTICLE
Title: Python MatPlotLib
MetaDescription: Python MatPlotLib
MetaKeywords: Python MatPlotLib Draw Graphs, pie chart
Author: (c) Venkata Bhattaram / tinitiate.com
ContentName: python-matplotlib-piechart
---
MARKDOWN """

""" MARKDOWN
# Pie Chart
* 
* 
MARKDOWN """

# MARKDOWN ```
import matplotlib.pyplot as plt

# Data to plot
labels = 'Desktops', 'Laptops', 'SmartPhones', 'SmartWatches'
sizes = [215, 130, 545, 20]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
# explode = (0.1, 0, 0, 0)  # explode 1st slice

# Plot
# plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
patches, text = plt.pie(sizes, labels=labels, colors=colors)

plt.legend(patches, labels, loc="upper left")

plt.axis('equal')
plt.show()

"""
import matplotlib.pyplot as plt

labels = ['Cookies', 'Jellybean', 'Milkshake', 'Cheesecake']
sizes = [38.4, 40.6, 20.7, 10.3]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.show()
"""
# MARKDOWN ```
