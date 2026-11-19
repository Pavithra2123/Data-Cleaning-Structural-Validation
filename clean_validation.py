
import pandas as pd
import os

# Load dataset
file_path = "data/sample_data.csv"

df = pd.read_csv(file_path)

print("Original Dataset:")
print(df)

# DATA CLEANING

# 1. Clean column names
df.columns = df.columns.str.strip().str.lower()

# 2. Remove duplicate records
df = df.drop_duplicates()

# 3. Remove extra spaces
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

# 4. Handle missing values
if "age" in df.columns:
    df["age"] = df["age"].fillna(df["age"].median())

# STRUCTURAL VALIDATION

required_columns = ["name", "age", "city", "salary"]

print("\nStructural Validation:")

missing_columns = [
    col for col in required_columns
    if col not in df.columns
]

if missing_columns:
    print("Missing columns:", missing_columns)
else:
    print("All required columns are present.")

# Check data types
print("\nData Types:")
print(df.dtypes)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check invalid records
if all(col in df.columns for col in required_columns):
    invalid_records = df[
        (df["age"] < 0) |
        (df["salary"] < 0) |
        (df["name"].isnull()) |
        (df["city"].isnull())
    ]

    print("\nInvalid Records:")
    print(invalid_records)

# Save cleaned dataset
os.makedirs("output", exist_ok=True)

df.to_csv("output/cleaned_data.csv", index=False)

print("\nData cleaning completed successfully!")
