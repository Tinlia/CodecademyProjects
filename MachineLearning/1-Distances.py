from scipy.spatial import distance

def euclidean_distance(pt1, pt2): # Calculates the Euclidean Distance between two coordinates
  distance = 0
  for i in range(len(pt1)):
    distance += (pt1[i] - pt2[i]) ** 2
  return distance ** 0.5

def manhattan_distance(pt1, pt2):  # Calculates the Manhattan Distance between two coordinates
  distance = 0
  for i in range(len(pt1)):
    distance += abs(pt1[i] - pt2[i])
  return distance

def hamming_distance(pt1, pt2):  # Calculates the Hamming Distance between two coordinates
  distance = 0
  for i in range(len(pt1)):
    if pt1[i] != pt2[i]:
      distance += 1
  return distance

# Above shows the math required to calculate three forms of distance measurement in arrays: Euclidean, Manhattan, and Hamming.
# Below shows how to use scipy to shorten the blocks of code down to one function

print(distance.euclidean([1,2],[4,0]))
print(distance.cityblock([1,2],[4,0])) # Manhattan distance is renamed to cityblock distance in scipy
print(distance.hamming([5,4,9],[1,7,9]))

print(euclidean_distance([1, 2], [4, 0]))
print(manhattan_distance([1, 2], [4, 0]))
print(hamming_distance([5, 4, 9], [1, 7, 9]))
