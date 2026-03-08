import math

# Dataset
data = [
    (2, 60, "Fail"),
    (5, 80, "Pass"),
    (6, 85, "Pass"),
    (1, 50, "Fail")
]

# User input
study_hours = float(input("Enter Study Hours: "))
attendance = float(input("Enter Attendance: "))

distances = []

# Step 1: Calculate Euclidean distance
for sh, att, result in data:
    dist = math.sqrt((study_hours - sh)**2 + (attendance - att)**2)
    distances.append((dist, result))

# Step 2: Sort distances
distances.sort()

# Step 3: Select K nearest neighbors
k = 3
neighbors = distances[:k]

# Step 4: Majority voting
votes = {"Pass":0, "Fail":0}

for d in neighbors:
    votes[d[1]] += 1

# Step 5: Prediction
prediction = max(votes, key=votes.get)

print("\nPredicted Result:", prediction)