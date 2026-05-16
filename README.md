# Network Packet Analyzer

A command-line network sniffer built in Python using the Scapy library. This tool intercepts, decodes, and displays live network traffic for diagnostic and educational purposes.

## ⚠️ Ethical Use Notice
This tool is intended exclusively for *educational labs, self-guided security training, and legitimate network analysis*. Packet sniffing without explicit permission on networks you do not own or manage is unauthorized and unethical. 

## Features
* Captures real-time IPv4 network packets.
* Identifies protocol types including *TCP, UDP, and ICMP*.
* Extracts and displays source and destination IP addresses.
* Displays a sanitized snippet of localized packet payload strings.

## Prerequisites
This tool requires Python and the scapy library. 

1. Install scapy:
   ```bash
   pip install scapy
