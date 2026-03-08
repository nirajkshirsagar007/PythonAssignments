import math

# Dataset
dataset = [
    ("A", 1, 2, "Red"),
    ("B", 2, 3, "Red"),
    ("C", 3, 1, "Blue"),
    ("D", 6, 5, "Blue")
]

# New point
x = 2
y = 2

# Calculate Euclidean distances
distances = []

for point, px, py, label in dataset:
    distance = math.sqrt((x - px)**2 + (y - py)**2)
    distances.append((point, distance, label))

# Sort distances
distances.sort(key=lambda d: d[1])

# Function to predict class for given K
def predict(k):
    neighbors = distances[:k]

    votes = {}
    for n in neighbors:
        label = n[2]
        votes[label] = votes.get(label, 0) + 1

    predicted = max(votes, key=votes.get)
    return predicted

print("Prediction Results\n")

for k in [1, 3, 5]:
    print("K =", k, "->", predict(k))