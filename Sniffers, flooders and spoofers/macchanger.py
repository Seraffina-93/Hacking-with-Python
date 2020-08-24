#!/usr/bin/python

import subprocess
from termcolor import colored

def changer(interface, mac):
	subprocess.call(["ifconfig",interface,"down"])
	subprocess.call(["ifconfig",interface,"hw","ether",mac])
	subprocess.call(["ifconfig",interface,"up"])


def main():
	interface = str(input("[*] Enter interface to change MAC address on: "))
	newMAC = input("[*] Enter the new MAC address: ")

	beforeChanger = subprocess.check_output(["ifconfig",interface])
	changer(interface, newMAC)
	afterChanger = subprocess.check_output(["ifconfig",interface])

	if (beforeChanger == afterChanger):
		print(colored("[!!] Failed to change mac address", 'red'))
	else:
		print(colored("[+] MAC address changed to: " + newMAC + " on interface: " + interface, 'green'))

main()
