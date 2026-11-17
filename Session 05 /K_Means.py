# K-Means
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


Data = [
    [22, 2.5], [25, 5.0], [29, 8.5], [32, 2.5], [55, 60.0], [45, 35.0],
    [19, 1.5], [27, 7.0], [35, 12.0], [40, 25.0], [21, 3.0], [30, 9.5],
    [52, 55.0], [48, 42.0], [23, 4.0], [28, 6.5], [33, 15.0], [38, 20.0],
    [60, 70.0], [26, 5.5], [24, 3.5], [31, 10.0], [42, 30.0], [50, 48.0],
    [20, 2.0], [34, 13.0], [37, 18.0], [46, 38.0], [57, 65.0], [29, 7.5],
    [18, 1.0], [22, 2.8], [27, 6.0], [36, 16.0], [41, 27.0], [53, 58.0],
    [49, 45.0], [25, 4.5], [30, 8.0], [32, 11.0], [44, 33.0], [58, 68.0],
    [21, 2.2], [28, 7.2], [35, 14.0], [39, 22.0], [47, 40.0], [54, 62.0],
    [23, 3.2], [26, 5.8], [19, 1.8], [24, 4.2], [33, 12.5], [37, 19.0],
    [43, 29.0], [51, 52.0], [56, 63.0], [20, 2.5], [29, 9.0], [31, 10.5],
    [34, 13.5], [40, 24.0], [45, 36.0], [59, 72.0], [22, 3.5], [27, 6.8],
    [32, 9.0], [36, 17.0], [42, 28.0], [48, 44.0], [55, 59.0],[18, 1.2],
    [25, 5.2], [30, 8.8], [35, 15.5], [39, 21.0], [46, 39.0], [52, 54.0],
    [21, 2.7], [28, 7.8], [33, 11.5], [38, 19.5], [44, 32.0], [50, 47.0],
    [57, 66.0], [23, 3.8], [26, 6.2], [31, 9.8], [37, 18.5], [41, 26.0],
    [49, 46.0], [53, 57.0], [20, 1.7], [24, 4.8], [29, 8.2], [34, 14.5],
    [43, 31.0], [56, 64.0], [60, 75.0]
]

model = KMeans(n_clusters= 3,init="k-means++", random_state=42)

# n_clustersint, default=8
# The number of clusters to form as well as the number of centroids to generate.

# init: 
# Method for initialization: ‘k-means++’, ‘random’

# random_state : Determines random number generation for centroid initialization.
# Use an int to make the randomness deterministic

model.fit(Data)
print(f"Model Labels:\n {model.labels_}")
for index ,cluster in enumerate(model.cluster_centers_):
    print(f"{index} Model Clusters: {cluster}")

# Plot
for i in model.labels_:
    plt.scatter(i, color ='red')

for j in model.cluster_centers_:
    plt.scatter(j, color ='yellow')


plt.xlabel("labels")
plt.ylabel("cluster")
plt.title("Plot by Labels and Cluster")
plt.show()
