
# Bank Customer Churn Prediction using Neural Network

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# 1. Load Dataset

df = pd.read_csv("Churn_Modelling.csv")

print(df.head())


# 2. Data Preprocessing

df = df.drop(
    ["RowNumber", "CustomerId", "Surname"],
    axis=1,
    errors="ignore"
)

# Remove missing and duplicate records
df = df.dropna()
df = df.drop_duplicates()

# Convert categorical columns into numerical values
df = pd.get_dummies(
    df,
    columns=["Geography", "Gender"],
    drop_first=True,
    dtype=int
)


# 3. Separate Input and Output

X = df.drop("Exited", axis=1)
y = df["Exited"]


# 4. Split Dataset (80% Training, 20% Testing)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,random_state=42
)


# 5. Normalize the Data

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# 6. Build Neural Network

model = Sequential()

model.add(Dense(16, activation="relu",
                input_shape=(X_train.shape[1],)))

model.add(Dense(8, activation="relu"))

model.add(Dense(1, activation="sigmoid"))


# 7. Compile the Model

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)


# 8. Train the Model

model.fit(
    X_train,
    y_train
)


# 9. Predict on Test Data

predictions = model.predict(X_test)

# Convert probabilities into 0 or 1
y_pred = (predictions > 0.5).astype(int)


# 10. Calculate Accuracy

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy * 100, "%")


# 11. Confusion Matrix

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)
