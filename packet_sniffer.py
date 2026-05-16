from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_callback(packet):
    # Check if the captured packet contains an IP layer
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        # Map protocol numbers to their names
        if protocol == 6:
            proto_name = "TCP"
        elif protocol == 17:
            proto_name = "UDP"
        elif protocol == 1:
            proto_name = "ICMP"
        else:
            proto_name = "Other"

        print(f"\n[+] Packet Captured:")
        print(f"    Source IP      : {ip_src}")
        print(f"    Destination IP : {ip_dst}")
        print(f"    Protocol       : {proto_name}")

        # If it's a TCP or UDP packet, show a snippet of payload data if it exists
        if packet.haslayer(TCP) or packet.haslayer(UDP):
            payload = bytes(packet[TCP].payload) if packet.haslayer(TCP) else bytes(packet[UDP].payload)
            if payload:
                # Show only the first 30 characters of raw data for clarity
                print(f"    Payload Data   : {payload[:30]}")

def main():
    print("--- Network Packet Analyzer ---")
    print("[!] EDUCATIONAL PURPOSES ONLY")
    print("[*] Monitoring network traffic... Press Ctrl+C to stop.")
    
    # Start sniffing packets indefinitely. 
    # store=False keeps it memory efficient by dropping packets after handling them
    sniff(prn=packet_callback, store=False)

if __name__ == "__main__":
    main()