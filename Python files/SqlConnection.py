import pandas as pd
import pyodbc

# 1. Load data from GitHub (RAW link)
csv_files = {
'CleanSleepStudy': 'https://raw.githubusercontent.com/SENG8081/SENG8081-S25-Team7/refs/heads/main/Clean%20data/Fully%20clean_SleepStudy.csv',
'Clean_Student_Insomnia_Dataset': 'https://raw.githubusercontent.com/SENG8081/SENG8081-S25-Team7/refs/heads/main/Clean%20data/Fully_Cleaned_Student_Insomnia_Dataset.csv',
'Clean_student_sleep_patterns_normalized': 'https://raw.githubusercontent.com/SENG8081/SENG8081-S25-Team7/refs/heads/main/Clean%20data/cleaned_student_sleep_patterns_normalized.csv'
}


# 2. SQL Server connection 
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=SHIVANI\\SQLEXPRESS01;' #change server name as according to ur sql server name
    'DATABASE=Sleeping_pattern_database;' #you can change the database name as per your database
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()
# Using for loop to go through each file and insert
for table_name, url in csv_files.items():
    print(f" Loading {table_name} from GitHub...")
    df = pd.read_csv(url)

    # Drop table if it exists and create a new one
    columns = df.columns
    create_query = f"IF OBJECT_ID('{table_name}', 'U') IS NOT NULL DROP TABLE {table_name};\nCREATE TABLE {table_name} (\n"
    create_query += ',\n'.join([f"[{col}] VARCHAR(255)" for col in columns])
    create_query += "\n);"
    cursor.execute(create_query)
    conn.commit()

    # Prepare insert query
    col_names = ', '.join(f"[{col}]" for col in columns)
    placeholders = ', '.join(['?'] * len(columns))
    insert_query = f"INSERT INTO {table_name} ({col_names}) VALUES ({placeholders})"

    for _, row in df.iterrows():
        cursor.execute(insert_query, tuple(row))
    conn.commit()

    print(f" {table_name} uploaded successfully.")

# Close connection
cursor.close()
conn.close()

print(" All CSV files uploaded to SQL Server successfully!")
