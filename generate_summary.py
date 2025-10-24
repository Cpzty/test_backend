import json
import csv
from datetime import datetime
from collections import Counter

# 1. File paths
date_str = datetime.now().strftime("%Y%m%d")
json_file = f"var/data/data_{date_str}.json"
summary_file = f"var/data/summary_{date_str}.csv"

# 2. Load JSON
with open(json_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

users = data['users']

# 3. Prepare summary
total_users = len(users)
genders = Counter(u.get('gender','Unknown') for u in users)
average_age = sum(u.get('age',0) for u in users)/total_users if total_users else 0
average_height = sum(u.get('height',0) for u in users)/total_users if total_users else 0
average_weight = sum(u.get('weight',0) for u in users)/total_users if total_users else 0


# 4. Write CSV
with open(summary_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Metric','Value'])
    writer.writerow(['Total Users', total_users])
    writer.writerow(['Average Age', round(average_age,2)])
    writer.writerow(['Average Height', round(average_height,2)])
    writer.writerow(['Average Weight', round(average_weight,2)])
    
    # Gender counts
    for gender, count in genders.items():
        writer.writerow([f'Gender: {gender}', count])
    

print(f"Summary CSV saved: {summary_file}")
