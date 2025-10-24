from datetime import datetime

key = None
with open(".env") as f:
    for line in f:
        if line.startswith("ENCRYPTION_KEY="):
            key = int(line.strip().split("=")[1])
            break

#read files
date_str = datetime.now().strftime("%Y-%m-%d")
summary_file = f"var/data/summary_{datetime.now().strftime('%Y%m%d')}.csv"
detail_file = f"var/data/ETL_{datetime.now().strftime('%Y%m%d')}.csv"
json_file = f"var/data/data_{datetime.now().strftime('%Y%m%d')}.json"

#write to .enc files
summary_file_enc = summary_file[:-3] + 'enc'
detail_file_enc = detail_file[:-3] + 'enc'
json_file_enc = json_file[:-4] + 'enc'


with open(summary_file, "rb") as f:
    data = f.read()
    encrypted_data = bytes([b ^ key for b in data])
with open(summary_file_enc, "wb") as f:
    f.write(encrypted_data)

with open(detail_file, "rb") as f:
    data = f.read()
    encrypted_data = bytes([b ^ key for b in data])
with open(detail_file_enc, "wb") as f:
    f.write(encrypted_data)


with open(json_file, "rb") as f:
    data = f.read()
    encrypted_data = bytes([b ^ key for b in data])
with open(json_file_enc, "wb") as f:
    f.write(encrypted_data)

