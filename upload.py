import paramiko
from pathlib import Path

host = "localhost"
port = 22
username = "sftpuser"
password = "MyPassword123"  # if not using key
remote_dir = "."  # change to your home or target folder

files_to_upload = [
    Path("var/data/ETL_20251023.enc"),
    Path("var/data/summary_20251023.enc"),
    Path("var/data/data_20251023.enc")
    
]

transport = paramiko.Transport((host, port))
transport.connect(username=username, password=password)
sftp = paramiko.SFTPClient.from_transport(transport)

for f in files_to_upload:
    remote_file = remote_dir + f.name
    sftp.put(str(f), remote_file)
    print(f"Uploaded {f} -> {remote_file}")

sftp.close()
transport.close()
