import json
import csv
from datetime import datetime

# 1. Load JSON
date_str = datetime.now().strftime("%Y%m%d")
json_file = f"var/data/data_{date_str}.json"
csv_file = f"var/data/ETL_{date_str}.csv"

with open(json_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

users = data['users']

# 2. Flatten & write CSV
fields = [
    'id','firstName','lastName','age','gender','email','phone','username','birthDate',
    'bloodGroup','height','weight','eyeColor','hairColor','hairType','city','state','country',
    'university','companyName','companyDept','companyTitle','cryptoCoin','cryptoWallet','cryptoNetwork','role', 
    'cardExpire','cardNumber','cardType','currency','iban'
]

with open(csv_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()

    for user in users:
        writer.writerow({
            'id': user.get('id',''),
            'firstName': user.get('firstName',''),
            'lastName': user.get('lastName',''),
            'age': user.get('age',''),
            'gender': user.get('gender',''),
            'email': user.get('email',''),
            'phone': user.get('phone',''),
            'username': user.get('username',''),
            'birthDate': user.get('birthDate',''),
            'bloodGroup': user.get('bloodGroup',''),
            'height': user.get('height',''),
            'weight': user.get('weight',''),
            'eyeColor': user.get('eyeColor',''),
            'hairColor': user.get('hair',{}).get('color',''),
            'hairType': user.get('hair',{}).get('type',''),
            'city': user.get('address',{}).get('city',''),
            'state': user.get('address',{}).get('state',''),
            'country': user.get('address',{}).get('country',''),
            'university': user.get('university',''),
            'companyName': user.get('company',{}).get('name',''),
            'companyDept': user.get('company',{}).get('department',''),
            'companyTitle': user.get('company',{}).get('title',''),
            'cryptoCoin': user.get('crypto',{}).get('coin',''),
            'cryptoWallet': user.get('crypto',{}).get('wallet',''),
            'cryptoNetwork': user.get('crypto',{}).get('network',''),
            'role': user.get('role',''),
            # BANK DETAILS
            'cardExpire': user.get('bank',{}).get('cardExpire',''),
            'cardNumber': user.get('bank',{}).get('cardNumber',''),
            'cardType': user.get('bank',{}).get('cardType',''),
            'currency': user.get('bank',{}).get('currency',''),
            'iban': user.get('bank',{}).get('iban','')
        })
