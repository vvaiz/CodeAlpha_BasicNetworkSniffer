from scapy.all import sniff, IP, TCP, UDP, Raw

def process_packet(packet):
    print("\n=== Packet Captured ===")

    # check for IP layer
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")

    # check for TCP
    if packet.haslayer(TCP):
        tcp_layer = packet[TCP]
        print("Protocol: TCP")
        print(f"Source Port: {tcp_layer.sport}")
        print(f"Destination Port: {tcp_layer.dport}")

    # check for UDP
    elif packet.haslayer(UDP):
        udp_layer = packet[UDP]
        print("Protocol: UDP")
        print(f"Source Port: {udp_layer.sport}")
        print(f"Destination Port: {udp_layer.dport}")

    # payload (raw data)
    if packet.haslayer(Raw):
        payload = packet[Raw].load
        print(f"Payload: {payload[:50]}")  # limit output
# sniffing
print("Starting packet capture... Press Ctrl+C to stop.")
sniff(prn=process_packet, store=False)