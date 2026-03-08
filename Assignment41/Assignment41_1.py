import math

# Dataset
data = [
    ("A", 1, 2, "Red"),
    ("B", 2, 3, "Red"),
    ("C", 3, 1, "Blue"),
    ("D", 6, 5, "Blue")
]

# Take input from user
x = float(input("Enter X coordinate: "))
y = float(input("Enter Y coordinate: "))

distances = []

# Step 1: Calculate Euclidean distance
for point, px, py, label in data:
    dist = math.sqrt((x - px)**2 + (y - py)**2)
    distances.append((point, dist, label))

# Step 2: Sort distances
distances.sort(key=lambda d: d[1])

# Step 3: Select K nearest neighbors
k = 3
neighbors = distances[:k]

print("\nNearest Neighbors:")
for n in neighbors:
    print(f"{n[0]} - Distance: {round(n[1],2)}")

# Step 4: Majority voting
votes = {}

for n in neighbors:
    label = n[2]
    if label in votes:
        votes[label] += 1
    else:
        votes[label] = 1

# Step 5: Predict class
predicted_class = max(votes, key=votes.get)

print("\nPredicted Class:", predicted_class)