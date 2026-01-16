# Layer 2 Security Scripts

This repository contains a set of Python tools developed for educational purposes to study **Data Link Layer (Layer 2)** vulnerabilities and defenses.

## :file_folder: Included Tools

### 1. ARP Spoofer (`arp_spoofer.py`)
Demonstrates a **Man-in-the-Middle (MitM)** attack by sending forged ARP replies (`op=2`). It tricks both the victim and the router to redirect traffic through the attacker's machine.

### 2. Anti-ARP Spoofer (`anti_arp_spoofer.py`)
A defense tool that monitors the network for ARP poisoning attempts. It analyzes ARP traffic to detect inconsistencies in IP-MAC mappings.

### 3. MAC Flooder (`mac_flooder.py`)
A script designed to overflow the **CAM Table** of a switch by sending thousands of Ethernet frames with random MAC addresses, demonstrating how a switch can be forced into "fail-open" mode.

## :tools: Requirements
- Python 3.x
- Scapy Library (`pip install scapy`)
- Root/Admin privileges (to craft raw packets)

## :warning: Disclaimer
These scripts are for **educational and ethical hacking purposes only**. Never use these tools on networks you do not have explicit permission to test.
