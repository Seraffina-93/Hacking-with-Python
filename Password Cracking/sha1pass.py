
#!/usr/bin/python

from urllib.request import urlopen
import hashlib
from termcolor import colored

sha1hash = input("[*] Enter sha1 hash value: ")

passlist = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read(), 'utf-8')

for password in passlist.split('\n'):
	hashguess = hashlib.sha1(bytes(password, 'utf-8')).hexdigest()
	if hashguess == sha1hash:
		print (colored("[+] The password is: " + str(password), 'green'))
		quit()
	else:
		print (colored("[-] Password guess: " + str(password) + " is incorrect, trying next...", 'red')) 
print("Password not in list")

