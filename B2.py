```python
# Email Spam Classification using KNN and SVM

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# 1. Create Dataset

data = {
    "email": [
        "Win a free lottery prize now",
        "Congratulations you won a free gift",
        "Claim your cash reward today",
        "Free entry in lucky draw",
        "Click here to win money",
        "You have won a lottery",
        "Get free offers now",
        "Urgent claim your prize",
        "Win a free mobile phone",
        "Congratulations claim your reward",
        "Earn money from home",
        "Limited time free offer",

        "Meeting scheduled for tomorrow",
        "Please submit your assignment",
        "Let's have lunch today",
        "Your project report is ready",
        "Can we meet this evening",
        "Please check your email",
        "The class starts at 10 AM",
        "Your appointment is confirmed",
        "Please send me the documents",
        "I will call you tomorrow",
        "The meeting is postponed",
        "Thank you for your help"
    ],

    "label": [
        "spam", "spam", "spam", "spam",
        "spam", "spam", "spam", "spam",
        "spam", "spam", "spam", "spam",

        "ham", "ham", "ham", "ham",
        "ham", "ham", "ham", "ham",
        "ham", "ham", "ham", "ham"
    ]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df.head())

# 2. Separate Features and Target

X = df["email"]
y = df["label"]

# 3. Convert Text into Numerical Data

vectorizer = TfidfVectorizer()

# 4. Split Dataset

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# 5. KNN Model

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(X_train, y_train)

knn_pred = knn.predict(X_test)

# 6. SVM Model

svm = SVC()

svm.fit(X_train, y_train)

svm_pred = svm.predict(X_test)

# 7. Performance Evaluation

def evaluate_model(name, actual, predicted):

    print("\n", name)

    print("Accuracy Score:")
    print(accuracy_score(actual, predicted))

    print("\nConfusion Matrix:")
    print(confusion_matrix(actual, predicted, labels=["spam", "ham"]))

    print("\nClassification Report:")
    print(classification_report(actual, predicted, zero_division=0))

# 8. Compare Both Models

evaluate_model("KNN Performance", y_test, knn_pred)

evaluate_model("SVM Performance", y_test, svm_pred)
```
