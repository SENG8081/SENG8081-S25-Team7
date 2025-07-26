import pandas as pd
import re

# Load dataset
file_path = "Student Insomnia and Educational Outcomes Dataset_version-2.csv"
df = pd.read_csv(file_path)

# Step 1: Rename columns for easier handling
df.columns = [
    "Timestamp", "Year", "Gender", "Sleep_Difficulty", "Avg_Sleep_Hours",
    "Wake_Frequency", "Sleep_Quality", "Concentration_Issue",
    "Daytime_Fatigue", "Missed_Classes", "Sleep_Impact_Assignments",
    "Device_Use_Before_Sleep", "Caffeine_Use", "Physical_Activity",
    "Academic_Stress", "Academic_Performance"
]

# Step 2: Drop the Timestamp column (not needed)
df.drop("Timestamp", axis=1, inplace=True)

# Step 3: Simplify category labels by removing descriptions like "(5-6 times a week)"
def simplify_response(val):
    if isinstance(val, str):
        return re.sub(r"\s*\(.*?\)", "", val).strip()
    return val

df = df.applymap(simplify_response)

# Step 4: Convert selected columns to ordered categorical types
ordered_levels = {
    "Sleep_Difficulty": ["Never", "Rarely", "Sometimes", "Often", "Always"],
    "Wake_Frequency": ["Never", "Rarely", "Sometimes", "Often", "Always"],
    "Sleep_Quality": ["Very poor", "Poor", "Average", "Good", "Very good"],
    "Concentration_Issue": ["Never", "Rarely", "Sometimes", "Often", "Always"],
    "Daytime_Fatigue": ["Never", "Rarely", "Sometimes", "Often", "Always"],
    "Missed_Classes": ["Never", "Rarely", "Sometimes", "Often", "Always"],
    "Sleep_Impact_Assignments": ["No impact", "Minor impact", "Moderate impact", "Major impact"],
    "Device_Use_Before_Sleep": ["Never", "Rarely", "Sometimes", "Often", "Always"],
    "Caffeine_Use": ["Never", "Rarely", "Sometimes", "Often", "Always"],
    "Physical_Activity": ["Never", "Rarely", "Sometimes", "Often", "Every day"],
    "Academic_Stress": ["No stress", "Low stress", "Moderate stress", "High stress", "Extremely high stress"],
    "Academic_Performance": ["Very poor", "Below Average", "Average", "Good", "Excellent"]
}

for col, levels in ordered_levels.items():
    df[col] = pd.Categorical(df[col], categories=levels, ordered=True)

# Step 5: Fill missing/null values using mode (most common value) for each column
for col in df.columns:
    if df[col].isnull().sum() > 0:
        most_common = df[col].mode()[0]
        df[col].fillna(most_common, inplace=True)

# Step 6: Save the cleaned dataset
df.to_csv("Fully_Cleaned_Student_Insomnia_Dataset.csv", index=False)
print("Dataset cleaned and saved as 'Fully_Cleaned_Student_Insomnia_Dataset.csv'")
