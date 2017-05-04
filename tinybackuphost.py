import os
from base64 import b64decode
print("TinyBackup")
if os.path.exists("backup"):
	print("Backup directory exists already...")
	exit()
filename = raw_input("File name: ")
backup_file = ""
with open(filename, 'r') as backup:
	backup_file = backup.read()
backup_file = backup_file.split('@')
for i in range(len(backup_file)):
	backup_file[i] = backup_file[i].split('!')
for i in backup_file:
	print(i[0])
	directory = "backup"+'/'.join(i[0].split('/')[:-1])
	print(directory)
	if not os.path.exists(directory):
		os.makedirs(directory)
	with open("backup"+'/'.join(i[0].split('/')), 'w') as writefile:
		writefile.write(b64decode(i[1]))
