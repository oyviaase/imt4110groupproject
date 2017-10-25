# Author: Øyvind Jensen
import hashlib

with open('passwords.txt', 'r') as pwfile, open('hashedpws.txt', 'w') as outfile:
	for password in pwfile:
		pwhash = hashlib.md5(password)
		pwhash = pwhash.hexdigest()
		#pwhash.strip()
		password = password + ':' + pwhash
		password = password.replace('\n', '')
		print password
		outfile.write(password)
		outfile.write('\n')