
# Uber Fare Prediction

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error


# 1. Load Dataset
df = pd.read_csv("uber.csv/uber.csv")

print("First 5 rows:")
print(df.head())

# 2. Data Preprocessing

# Remove missing values
df = df.dropna()

# Remove invalid fare and passenger values
df = df[(df["fare_amount"] > 0) & 
        (df["passenger_count"] > 0)]

# Convert pickup_datetime into datetime format
df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"])


df["hour"] = df["pickup_datetime"].dt.hour
df["day"] = df["pickup_datetime"].dt.day



# 3. Calculate Distance using Haversine Formula

def calculate_distance(row):

    lat1 = np.radians(row["pickup_latitude"])
    lon1 = np.radians(row["pickup_longitude"])

    lat2 = np.radians(row["dropoff_latitude"])
    lon2 = np.radians(row["dropoff_longitude"])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (np.sin(dlat/2)**2 +
         np.cos(lat1) * np.cos(lat2) *
         np.sin(dlon/2)**2)

    c = 2 * np.arcsin(np.sqrt(a))

    return 6371 * c

df = df[
    df["pickup_latitude"].between(-90, 90) &
    df["dropoff_latitude"].between(-90, 90) &
    df["pickup_longitude"].between(-180, 180) &
    df["dropoff_longitude"].between(-180, 180)
]


df["distance"] = df.apply(calculate_distance, axis=1)


# 4. Outlier Detection using IQR

Q1 = df["fare_amount"].quantile(0.25)
Q3 = df["fare_amount"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df = df[
    (df["fare_amount"] >= lower) &
    (df["fare_amount"] <= upper)
]

print("\nData after preprocessing:")
print(df.shape)


# 5. Correlation Analysis

features = [
    "fare_amount", "passenger_count",
    "hour", "day", "distance"
]

correlation = df[features].corr()

print("\nCorrelation:")
print(correlation)

sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


# 6. Select Features and Target

X = df[[
    "passenger_count", "hour", "day", "distance"
]]

y = df["fare_amount"]


# 7. Split Dataset

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# 8. Linear Regression

lr = LinearRegression()

lr.fit(X_train, y_train)

lr_pred = lr.predict(X_test)

lr_r2 = r2_score(y_test, lr_pred)

lr_rmse = np.sqrt(mean_squared_error(y_test, lr_pred))


# 9. Random Forest Regression

rf = RandomForestRegressor(
    n_estimators=50,
    random_state=42,
    n_jobs=-1
)

rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

rf_r2 = r2_score(y_test, rf_pred)

rf_rmse = np.sqrt(mean_squared_error(y_test, rf_pred))


# 10. Compare Models

print("\nMODEL COMPARISON")

print("Linear Regression:")
print("R2 Score:", lr_r2)
print("RMSE:", lr_rmse)

print("\nRandom Forest:")
print("R2 Score:", rf_r2)
print("RMSE:", rf_rmse)


