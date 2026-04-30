Basic Network Packet Sniffer (Python)
Description

A simple network packet sniffer built using Python and Scapy.
This project captures live network traffic and analyzes packets to display key information such as source and destination IP addresses, protocols, ports, and payload data.

It is designed as an educational tool to help understand how data flows across networks and how common protocols like TCP and UDP work.

Features
Capture live network packets in real-time
Extract and display:
Source IP address
Destination IP address
Protocol (TCP/UDP)
Source & destination ports
Packet payload (when available)
Handles missing payloads safely
Works with encrypted and unencrypted traffic (limited visibility for HTTPS)
Technologies Used
Python
Scapy
Requirements

Before running the project, make sure you have:

Python 3.x installed

scapy installed:

pip install scapy
On Windows:
Install Npcap
Enable WinPcap compatibility mode during installation
How to Run
Clone the repository:
git clone https://github.com/yourusername/packet-sniffer.git
cd packet-sniffer
Run the script:
python sniffer.py
Stop execution:
Ctrl + C
Example Output
=== Packet Captured ===
Source IP: 192.168.1.5
Destination IP: 142.250.183.78
Protocol: TCP
Source Port: 51523
Destination Port: 443
Payload: GET / HTTP/1.1...
Limitations
HTTPS traffic is encrypted, so payloads may not be readable
Requires administrator/root privileges
Captures only traffic visible to your network interface
Learning Outcomes

This project helps you:

Understand packet structure and layers
Learn basics of network protocols (TCP/IP, UDP)
Explore real-time network traffic analysis
Gain hands-on experience with packet sniffing
Future Improvements
Add packet filtering (by IP, port, protocol)
Save captured packets to a file
Build a graphical user interface (GUI)
Display statistics and traffic summaries
Disclaimer

This project is for educational purposes only.
Do not use it to intercept or analyze network traffic without proper authorization.



A Python-based network packet sniffer using Scapy that captures and analyzes live traffic, displaying IP addresses, protocols, ports, and payload data for educational purposes.
