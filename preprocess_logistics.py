"""
Week 2 - Logistics Data Collection, Cleaning and Preprocessing
Project: Logistics Data Quality and Preprocessing Pipeline
"""

import pandas as pd
import numpy as np

RAW_FILE = "data/logistics_raw.csv"
OUTPUT_FILE = "data/logistics_cleaned.csv"

# 1. Data collection / loading
df = pd.read_csv(RAW_FILE)
print("Shape:", df.shape)
print(df.head())
print(df.info())

# 2. Initial quality checks
print("Missing values:\n", df.isna().sum())
print("Duplicate shipment IDs:", df["Shipment_ID"].duplicated().sum())
print("Numeric summary:\n", df.describe())

# 3. Standardize data types and text
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
df["Transport_Mode"] = df["Transport_Mode"].astype(str).str.strip().str.title()
df["Carrier"] = df["Carrier"].astype(str).str.strip().str.title()

# 4. Remove duplicate shipment records
df = df.drop_duplicates(subset=["Shipment_ID"], keep="first")

# 5. Handle invalid values
df.loc[df["Distance_km"] <= 0, "Distance_km"] = np.nan

# 6. Handle missing values
numeric_cols = [
    "Distance_km", "Shipment_Weight_kg", "Transportation_Cost_INR",
    "Shipment_Volume_units", "Promised_Delivery_Days",
    "Actual_Delivery_Days"
]
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

for col in ["Transport_Mode", "Carrier"]:
    df[col] = df[col].fillna(df[col].mode()[0])

# 7. Detect and cap outliers using IQR
for col in ["Distance_km", "Shipment_Weight_kg",
            "Transportation_Cost_INR", "Actual_Delivery_Days"]:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    df[col] = df[col].clip(lower, upper)

# 8. Recalculate status after cleaning
df["Delivery_Status"] = np.where(
    df["Actual_Delivery_Days"] <= df["Promised_Delivery_Days"],
    "On Time", "Delayed"
)

# 9. Min-Max normalization for comparable analysis
normalize_cols = [
    "Distance_km", "Shipment_Weight_kg", "Shipment_Volume_units",
    "Actual_Delivery_Days", "Transportation_Cost_INR"
]
for col in normalize_cols:
    df[col + "_Normalized"] = (
        (df[col] - df[col].min()) /
        (df[col].max() - df[col].min())
    )

# 10. Final validation
print("Final shape:", df.shape)
print("Final missing values:\n", df.isna().sum())
print("Final duplicate IDs:", df["Shipment_ID"].duplicated().sum())

df.to_csv(OUTPUT_FILE, index=False)
print("Saved:", OUTPUT_FILE)
