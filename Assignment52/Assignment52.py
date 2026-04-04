import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def StudentClustering(DataPath):

    border = "-"*50

    # Step 1: Load Dataset
    print(border)
    print("Step 1: Load Dataset")
    print(border)

    df = pd.read_csv(DataPath)
    print(df.head())

    # Step 2: Select Features
    print(border)
    print("Step 2: Select Features")
    print(border)

    features = ['StudyHours','Attendance','PreviousScore','AssignmentsCompleted','SleepHours'] 
    X = df[features]

    print("Selected Features:",features)

    # Step 3: Handle Missing Values
    print(border)
    print("Step 3: Data Cleaning")
    print(border)

    X = X.dropna()
    print("Total records after cleaning:",X.shape[0])

    # Step 4: Feature Scaling
    print(border)
    print("Step 4: Feature Scaling")
    print(border)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Step 5: Apply KMeans Clustering
    print(border)
    print("Step 5: Apply KMeans")
    print(border)

    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(X_scaled)

    clusters = kmeans.predict(X_scaled)

    # Add cluster column
    df = df.loc[X.index]
    df['Cluster'] = clusters

    print("Cluster values assigned:")
    print(df[['StudyHours','Attendance','PreviousScore','AssignmentsCompleted','SleepHours','Cluster']].head())

    # Step 6: Cluster Interpretation
    print(border)
    print("Step 6: Cluster Interpretation")
    print(border)

    print("Cluster 0 → Top Performers")
    print("Cluster 1 → Average Students")
    print("Cluster 2 → Struggling Students")

    print("--------------------------------------------------")
    print("Step 7: Visualization")
    print("--------------------------------------------------")

    plt.figure(figsize=(8,6))
    plt.scatter(df['StudyHours'], df['PreviousScore'], c=df['Cluster'], cmap='viridis')

    plt.title("Student Clusters Based on Study Hours and Previous Score")
    plt.xlabel("Study Hours")
    plt.ylabel("Previous Score")

    plt.colorbar(label="Cluster")
    plt.show()


def main():
    StudentClustering("student_performance_ml.csv") 


if __name__ == "__main__":
    main()