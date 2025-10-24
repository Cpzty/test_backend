import csv
import mysql.connector
from datetime import datetime

# Database connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='etl_db'
)
cursor = conn.cursor()

# 1. Insert into process_header
date_str = datetime.now().strftime("%Y-%m-%d")
summary_file = f"var/data/summary_{datetime.now().strftime('%Y%m%d')}.csv"
detail_file = f"var/data/ETL_{datetime.now().strftime('%Y%m%d')}.csv"

cursor.execute(
    "INSERT INTO process_header (execution_date, summary_file, detail_file, created_at) VALUES (%s,%s,%s,NOW())",
    (date_str, summary_file, detail_file)
)
process_id = cursor.lastrowid

# 2. Insert summary CSV
with open(summary_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute(
            "INSERT INTO summary_table (process_id, metric, value, created_at) VALUES (%s,%s,%s,NOW())",
            (process_id, row['Metric'], row['Value'])
        )

# 3. Insert detail CSV (ETL)
with open(detail_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        columns = ','.join(row.keys())
        placeholders = ','.join(['%s']*len(row))
        values = list(row.values())
        cursor.execute(
            f"INSERT INTO detail_table (process_id, user_id, {columns}, created_at) VALUES (%s,%s,{placeholders},NOW())",
            [process_id, row.get('id')] + values
        )

conn.commit()
cursor.close()
conn.close()
print("Database insertion completed.")
