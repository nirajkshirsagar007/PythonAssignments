import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import euclidean

data = np.array([
[25,20000],
[30,40000],
[35,80000]
])

# Distance before scaling
dist_before = euclidean(data[0],data[1])

# Feature scaling
scaler = StandardScaler()
scaled = scaler.fit_transform(data)

# Distance after scaling
dist_after = euclidean(scaled[0],scaled[1])

print("Distance before scaling:",dist_before)
print("Distance after scaling:",dist_after)