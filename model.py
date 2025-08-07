import argparse
from pathlib import Path

import polars as pl
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder

parser = argparse.ArgumentParser()
parser.add_argument("--train-data", type=Path, default=Path("data/train.csv"))
args = parser.parse_args()

df_train = pl.read_csv(args.train_data)
df_test = pl.read_csv("data/test.csv")

target = "Survived"
num_cols = ["Age", "Fare"]
cat_cols = ["Sex", "Pclass"]
feature_cols = num_cols + cat_cols

X_train = df_train.select(feature_cols)
y_train = df_train[target]

X_test = df_test.select(feature_cols)
y_test = df_test[target]

preprocess = ColumnTransformer([
    ("num", SimpleImputer(strategy="median"), num_cols),
    (
        "cat",
        make_pipeline(
            SimpleImputer(strategy="most_frequent"),
            OneHotEncoder(handle_unknown="ignore"),
        ),
        cat_cols,
    ),
])

clf = make_pipeline(preprocess, LogisticRegression(max_iter=1000))

clf.fit(X_train, y_train)

test_accuracy = accuracy_score(y_test, clf.predict(X_test))
print(f"{test_accuracy:.4f}")
