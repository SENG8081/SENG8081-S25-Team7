import pandas as pd

# Load the dataset
df = pd.read_csv("student_sleep_patterns.csv")

# Drop NA and duplicates
df = df.dropna().drop_duplicates()

# Rename columns for consistency and SQL use
df.columns = df.columns.str.strip().str.replace(" ", "_").str.lower()

# Encode Gender
df["gender"] = df["gender"].map({"Male": 0, "Female": 1, "Other": 2})

# Encode University Year
year_map = {
    "1st Year": 1,
    "2nd Year": 2,
    "3rd Year": 3,
    "4th Year": 4
}
df["university_year"] = df["university_year"].map(year_map)

# Round float columns to 1 decimal
float_cols = [
    "sleep_duration", "study_hours", "screen_time",
    "weekday_sleep_start", "weekend_sleep_start",
    "weekday_sleep_end", "weekend_sleep_end"
]
df[float_cols] = df[float_cols].round(1)

# Save cleaned and normalized dataset
df.to_csv("cleaned_student_sleep_patterns_normalized.csv", index=False)
print("Data cleaned, encoded, and saved.")
