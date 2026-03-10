from scapy.all import sniff, IP, TCP, UDP, ICMP

# Function to process captured packets
def packet_analysis(packet):

    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dest_ip = packet[IP].dst
        protocol = packet[IP].proto

        print("\n--- Packet Captured ---")
        print("Source IP:", src_ip)
        print("Destination IP:", dest_ip)

        # Identify protocol
        if packet.haslayer(TCP):
            print("Protocol: TCP")
            print("Source Port:", packet[TCP].sport)
            print("Destination Port:", packet[TCP].dport)

        elif packet.haslayer(UDP):
            print("Protocol: UDP")
            print("Source Port:", packet[UDP].sport)
            print("Destination Port:", packet[UDP].dport)

        elif packet.haslayer(ICMP):
            print("Protocol: ICMP")

        # Display payload if available
        if packet.payload:
            print("Payload:", packet.payload)

# Capture packets
print("Starting packet capture...\n")
sniff(prn=packet_analysis, count=20)
