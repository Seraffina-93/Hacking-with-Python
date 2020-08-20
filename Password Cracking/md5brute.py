#!usr/bin/python

from termcolor import colored
import hashlib

def tryOpen(wordlist):
	global passFile
	try:
		passFile = open(wordlist, "r")
	except:
		print ("[!!] No such file at that path")
		quit()

passHash = input("[*] Enter MD5 hash value: ")
wordlist = input("[*] Enter path to the password file: ")
tryOpen(wordlist)

for word in passFile:
	print(colored("[-] Trying: " + word.strip('\n'), 'red'))
	enc_wrd = word.encode('utf-8')
	md5digest = hashlib.md5(enc_wrd.strip()).hexdigest()

	if md5digest == passHash:
		print (colored("[+] Password found: " + word, 'green'))
		exit(0)

print ("Password not in list!")

