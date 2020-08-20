#!/usr/bin/python

import ftplib

def anonLogin(hostName):
	try:
		ftp = ftplib.FTP(hostName)
		ftp.login('anonymous', 'anonymous')
		print "[+] Anonymous login succeeded on " + hostName
		ftp.quit()
		return True
	except Exception, e:
		print '[-] ' + hostName + ' FTP Anonymous login failed '

host = raw_input("Enter the IP Address: ")
anonLogin(host)
