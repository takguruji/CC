import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("sales_data_sample.csv", encoding="latin1")

X = df[["SALES", "QUANTITYORDERED"]].dropna()

sc = StandardScaler()
X_scaled = sc.fit_transform(X)

wcss = []

for k in range( 1 , 11):
    kmeans = KMeans(n_clusters = k)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)
    
plt.plot(range(1,11),wcss)
plt.xlabel("number of clusters")
plt.ylabel("wcss")
plt.title("elbow method")
plt.show()

# apply kmeans 

kmeans = KMeans(n_clusters = 3)
df["Cluster"] = kmeans.fit_predict(X_scaled)

print(df.head())
print("Number of cluster:", df["Cluster"].nunique())

plt.scatter(X["SALES"],X["QUANTITYORDERED"],c = df["Cluster"])
plt.xlabel('SALES')
plt.ylabel('QUANTITYORDERED')
plt.title('K-Means Clustering')
plt.show()
