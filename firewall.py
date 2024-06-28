from scapy.all import *

def packet_callback(packet):
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        print(f"IP Packet: {ip_src} -> {ip_dst}")

# Sniff packets
sniff(prn=packet_callback, count=10)
