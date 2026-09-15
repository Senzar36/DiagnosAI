# import pandas as pd

# class machine_learning_health:
#     def __init__(self):
#         self.model = None
#         self.data = None

#     def load_data(self, data_path):
#         self.data = pd.read_csv(data_path)
#         for i in self.data:
#             for j in self.data[i]:
#                 if self.data[i][j] != 0 and self.data[i][j] != 1:
#                     self.data[i][j] = self.data[i].mean()

#     def preprocess_data(self):
#         self.preprocess_data()

#     def clean_dataset(self):
#         for i in self.data:
#              self.data[i] = self.data[i].fillna(self.data[i].mode()[0])


#     def evaluate_model(self):
#         pass

#     def save_model(self, model_path):
#         pd.to_pickle(self.model, model_path)
#         pass

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split, StratifiedKFold, cross_validate
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

#1)Loading dataset

print("Loading dataset...")

df = pd.read_csv("Training.csv")

print("\nOriginal dataset shape:")
print(df.shape)


# 2. BASIC DATASET INSPECTION

print("\nFirst 5 rows:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum().sum())

print("\nNumber of disease classes:")
print(df["prognosis"].nunique())

print("\nDisease distribution:")
print(df["prognosis"].value_counts())


# 3. REMOVE EMPTY COLUMN


if "Unnamed: 133" in df.columns:
    df = df.drop(columns=["Unnamed: 133"])

print("\nShape after removing empty column:")
print(df.shape)


# 4. REMOVE CONSTANT FEATURE

if "fluid_overload" in df.columns:
    if df["fluid_overload"].nunique() <= 1:
        df = df.drop(columns=["fluid_overload"])
        print("\nRemoved constant feature: fluid_overload")


# 5. SEPARATE FEATURES AND TARGET

symptom_columns = [
    column for column in df.columns
    if column != "prognosis"
]

X = df[symptom_columns]
y = df["prognosis"]


print("\nNumber of symptom features:")
print(len(symptom_columns))

print("\nFeature matrix X shape:")
print(X.shape)

print("\nTarget y shape:")
print(y.shape)


# 6. CHECK DUPLICATE SYMPTOM PATTERNS

duplicate_count = X.duplicated().sum()

print("\nDuplicate symptom patterns:")
print(duplicate_count)

print("\nUnique symptom patterns:")
print(X.drop_duplicates().shape[0])


# 7. REMOVE DUPLICATE SYMPTOM PATTERNS

combined = X.copy()
combined["prognosis"] = y.values

combined = combined.drop_duplicates(
    subset=symptom_columns
)

X = combined[symptom_columns]
y = combined["prognosis"]

print("\nShape after removing duplicate symptom patterns:")
print(X.shape)


# 8. TRAIN / TEST SPLIT

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining samples:")
print(len(X_train))

print("\nTesting samples:")
print(len(X_test))

# 9. DEFINE MODELS

models = {

    "Decision Tree": DecisionTreeClassifier(
        random_state=42
    ),

    "Random Forest": RandomForestClassifier(
        n_estimators=300,
        random_state=42
    ),

    "Logistic Regression": LogisticRegression(
        max_iter=5000,
        random_state=42
    ),

    "SVM": SVC(
        kernel="rbf",
        random_state=42
    ),

    "KNN": KNeighborsClassifier(
        n_neighbors=5
    )
}


# 10. TRAIN AND COMPARE MODELS

print("\n")
print("=" * 60)
print("MODEL COMPARISON")
print("=" * 60)

results = {}

for name, model in models.items():

    print("\nTraining:", name)

    model.fit(X_train, y_train)

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

    results[name] = {
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1
    }

    print("Accuracy :", round(accuracy, 4))
    print("Precision:", round(precision, 4))
    print("Recall   :", round(recall, 4))
    print("F1 Score :", round(f1, 4))



# 11. DISPLAY MODEL COMPARISON

print("\n")
print("=" * 60)
print("FINAL MODEL COMPARISON")
print("=" * 60)

results_df = pd.DataFrame(results).T

print(results_df)


# 12. CROSS-VALIDATION

print("\n")
print("=" * 60)
print("5-FOLD CROSS-VALIDATION")
print("=" * 60)

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

for name, model in models.items():

    scores = cross_validate(
        model,
        X,
        y,
        cv=cv,
        scoring=[
            "accuracy",
            "precision_weighted",
            "recall_weighted",
            "f1_weighted"
        ]
    )

    print("\n", name)

    print(
        "Mean Accuracy :",
        round(scores["test_accuracy"].mean(), 4)
    )

    print(
        "Mean Precision:",
        round(scores["test_precision_weighted"].mean(), 4)
    )

    print(
        "Mean Recall   :",
        round(scores["test_recall_weighted"].mean(), 4)
    )

    print(
        "Mean F1 Score :",
        round(scores["test_f1_weighted"].mean(), 4)
    )


# 13. SELECT RANDOM FOREST AS FINAL MODEL

print("\n")
print("=" * 60)
print("TRAINING FINAL MODEL")
print("=" * 60)

final_model = RandomForestClassifier(
    n_estimators=300,
    random_state=42
)

final_model.fit(X, y)

print("Final Random Forest model trained.")


# 14. SAVE TRAINED MODEL

joblib.dump(
    final_model,
    "diagnosai_model.pkl"
)

print("\nSaved model as:")
print("diagnosai_model.pkl")


# 15. SAVE SYMPTOM COLUMN ORDER

joblib.dump(
    symptom_columns,
    "symptom_columns.pkl"
)

print("\nSaved symptom list as:")
print("symptom_columns.pkl")


# 16. FINISHED

print("\n")
print("=" * 60)
print("TRAINING COMPLETE")
print("=" * 60)