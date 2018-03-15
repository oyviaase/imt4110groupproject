#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Øyvind Jensen
from passlib.hash import md5_crypt

with open('passwords.txt', 'r') as pwfile, open('hashedpws.txt', 'w') as outfile, open('hashes.txt', 'w') as hashfile:
	for password in pwfile:
		password = password.replace('\n', '')
		password = password.strip()
		pwhash = md5_crypt.encrypt(password)
		#pwhash.strip()
		password = password + ':' + pwhash
		password = password.replace('\n', '')
		print password
		outfile.write(password)
		outfile.write('\n')
		pwhash = pwhash.replace('\n', '')
		hashfile.write(pwhash)
		hashfile.write('\n')