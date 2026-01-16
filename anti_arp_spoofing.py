from scapy.all import sniff, ARP

GATEWAY_IP = "" # Enter your gateway IP here
GATEWAY_MAC = "" # Enter your real gateway MAC address here

def detect_spoof(pkt):
    if pkt.haslayer(ARP) and pkt[ARP].op == 2:
        ip_origin = pkt[ARP].psrc
        mac_origin = pkt[ARP].hwsrc

        if ip_origin == GATEWAY_IP and GATEWAY_MAC != mac_origin:
            print(f"[!] WARNING: ARP Spoofing Detected!")
            print(f"    Possible Attacker MAC: {mac_origin}")
            print(f"    Gateway IP {ip_origin} is being spoofed.")

print("[*] Monitoring ARP traffic for poisoning...")
sniff(filter="arp", prn=detect_spoof, store=0)
