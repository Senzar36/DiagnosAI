import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)

print("Loading dataset...")

df = pd.read_csv("Training.csv")

print("Dataset loaded successfully.")
print("Dataset shape:", df.shape)

if "Unnamed: 133" in df.columns:
    df = df.drop(columns=["Unnamed: 133"])

if "fluid_overload" in df.columns:
    if df["fluid_overload"].nunique() == 1:
        df = df.drop(columns=["fluid_overload"])


print("\nDataset shape after cleaning:", df.shape)

X = df.drop(columns=["prognosis"])
y = df["prognosis"]


print("\nNumber of symptom features:", X.shape[1])
print("Number of disease classes:", y.nunique())

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

model = RandomForestClassifier(
    n_estimators=300,
    random_state=42
)

print("\nTraining Random Forest...")

model.fit(X_train, y_train)

print("Training completed.")

print("\nTesting model...")

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(
    y_test,
    y_pred,
    average="weighted",
    zero_division=0
)

recall = recall_score(
    y_test,
    y_pred,
    average="weighted",
    zero_division=0
)

f1 = f1_score(
    y_test,
    y_pred,
    average="weighted",
    zero_division=0
)


print("\n" + "=" * 50)
print("MODEL PERFORMANCE")
print("=" * 50)

print("Accuracy :", round(accuracy, 4))
print("Precision:", round(precision, 4))
print("Recall   :", round(recall, 4))
print("F1 Score :", round(f1, 4))

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    zero_division=0
))

joblib.dump(
    model,
    "diagnosai_model.pkl"
)

print("Model saved as: diagnosai_model.pkl")


symptom_columns = X.columns.tolist()

joblib.dump(
    symptom_columns,
    "symptom_columns.pkl"
)

print("Symptom list saved as: symptom_columns.pkl")

print("\n" + "=" * 50)
print("ML TRAINING COMPLETE")
print("=" * 50)