'''
Traveling Salesperson Problem plotter
'''

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

coords_list = [(1, 1, 'A'), (3, 2, 'B'), (5, 1, 'C'), (5, 4, 'D'), #(x cood, y cood, city id)
               (4, 5, 'E'), (2, 6, 'F'), (1, 5, 'G'), (2, 3, 'H')] # cities, you can add more

X = [coords_list[i][0] for i in range(len(coords_list))] # cood x
Y = [coords_list[i][1] for i in range(len(coords_list))] # cood y
S = [coords_list[i][2] for i in range(len(coords_list))] # city id ('A', 'B', 'C', ...)

plt.figure(figsize = (18, 8)) # plot size

for i, j, k in coords_list:
    for w, x, z in coords_list:
        plt.plot((i, w), (j, x), color = 'black', alpha = 0.08) # ploting the ways
        

ax = sns.scatterplot(X, Y, alpha = 0) # ploting the cities, you can add the circles to representate the cities
for i in range(len(coords_list)): # write the id cities
     ax.text(X[i], Y[i], S[i], fontsize = 35, color = 'black', 
             horizontalalignment = 'center', 
             verticalalignment = 'center')
