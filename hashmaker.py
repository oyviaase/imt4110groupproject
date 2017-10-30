#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Øyvind Jensen
from passlib.hash import md5_crypt

with open('passwords.txt', 'r') as pwfile, open('hashedpws.txt', 'w') as outfile:
	for password in pwfile:
		pwhash = md5_crypt.encrypt(password)
		#pwhash.strip()
		password = password + ':' + pwhash
		password = password.replace('\n', '')
		print password
		outfile.write(password)
		outfile.write('\n')