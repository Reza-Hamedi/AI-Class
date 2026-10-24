# K-Nearest Neighbors
# سیب، با برچسب 0
# موز، با برچسب 1

import numpy as np
import matplotlib.pyplot as plt

# Generate data for Apple
apple_weight = np.random.randint(60, 100, 50)
apple_height = np.random.randint(50, 80, 50)

# Generate data for Banana
banana_weight = np.random.randint(20, 60, 50)
banana_height = np.random.randint(60, 100, 50)

# Combine Weights and Heights
apple_data = list(zip(apple_weight, apple_height))
banana_data = list(zip(banana_weight, banana_height))

# X_Train
X_Train = apple_data + banana_data

# Y_Train
Y_Train = [0 for _ in range(50)] + [1 for _ in range(50)]


# Draw data diagram with matplotlib.pyplot
for i in range(0, 50):
    plt.scatter(X_Train[i][0], X_Train[i][1], color ='red')

for i in range(50, 100):
    plt.scatter(X_Train[i][0], X_Train[i][1], color ='yellow')


# ....................................................
# Test Data (new fruit)
new_fruit = [np.random.randint(20, 101),np.random.randint(50, 101)]
plt.scatter(new_fruit[0], new_fruit[1], color='blue',marker='*')


plt.xlabel("Weight")
plt.ylabel("Height")
plt.title("Apple vs Banana")
plt.show()

# ....................................................
#  Calculate Euclidean distance
distances = []

def euclidean_distance(data, new_fruit):
    sigma = ((data[0] - new_fruit[0]) ** 2 ) + ((data[1] - new_fruit[1]) ** 2 )
    distance = np.sqrt(sigma)
    return distance

for data in X_Train:
    distances.append(euclidean_distance(data, new_fruit))


# ....................................................
def selection(distanceList, n):
    if n < 1 or n > len(distanceList):
        return False
    else:
        minimum_list = []
        index_list = []
        while n > 0:
            minimum_index = -1
            minimum = float('inf')
            for index, value in enumerate(distanceList):
                if index in index_list:
                    continue
                if  value < minimum:
                    minimum = value
                    minimum_index = index

            minimum_list.append({"index" : minimum_index , "distance" : minimum})
            index_list.append(minimum_index)
            n -= 1
        return minimum_list

# for index, value in enumerate(distances):
#     print(f"{index}: {value}")


# ....................................................
# KNN
def knn():
    final_decision = ""
    label = ""
    knn_result = []
    apple = 0
    banana = 0
    distanceList = distances.copy()
    the_nearest_points = selection(distanceList, 5)
    for value in the_nearest_points:
        if Y_Train[value.get("index")] == 0:
            label = "Apple"
            apple += 1
        else:
            label = "Banana"
            banana += 1
        knn_result.append({"label": label, "distance": value.get("distance")})
    final_decision = "apple" if apple > banana else "banana"
    knn_result.append({"apple": apple, "banana": banana, "final_decision": final_decision})
    return knn_result

# .................................

result = knn()
print("KNN Classification Result")
print("-" * 30)

for i, item in enumerate(result[:-1], start=1):
    print(
        f"Neighbor {i}: "
        f"{item['label']} | "
        f"Distance: {float(item['distance']):.2f}"
    )

final_result = result[-1]

print("-" * 30)
print(f"Apple votes : {final_result['apple']}")
print(f"Banana votes: {final_result['banana']}")
print(f"Prediction  : {final_result['final_decision'].capitalize()}")