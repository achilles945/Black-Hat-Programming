# Black Hat Python


## Notes

### Basic Networking Tools

- TCP Client
    - tcp-client.py
    - tcp client can be used to test for services, send garbage data, fuzz, etc.
- UDP Client
    - udp-client.py
    - udp client can be used to test for services, send garbage data, fuzz, etc.
- TCP Server
    - tcp-server.py
    - tcp server can be used when writing shells or crafting a proxy
- Netcat
    - netcat.py
    - netcat can be used to read and write data accross the network.
    - can be used to execute remote commands, pass files back and forth, open a remote shell
- TCP Proxy
    - proxy.py
    - tcp proxy can be used for forwarding traffic to bounce from host to host or when assessing network-based software
    - python proxies to help understand unknown protocols, modify traffic being sent to an application, create test cases for fuzzers.
- SSH with Paramiko
    - 
- SSH Tunneling

### Sniffing Tool

- UDP Host Discovery Tool
- Packet Sniffing
- Decoding IP Layer
- IP Decoder
- Decoding ICMP

### Network with Scapy

- Stealing Email Credentials
- ARP Cache Poisoning 
- pcap Processing

### Web Hackery

- Mapping WordPress Framework
- Brute-Forcing Directories and File Locations
- Brute-Forcing HTML Form Authentication

### Github Command and Control

- Setting up Github account and repository
- Creating modules
- Configuring Trojan
- Building GitHub-Aware Trojan
- Python's import Functionality

## Directory Structure

- basic-networking-tools
    - tcp-client.py
    - udp-client.py
    - tcp-server.py
    - netcat.py
    - proxy.py
    - ssh-paramiko
        - ssh_cmd.py
        - ssh_rcmd.py
        - ssh_server.py
    - ssh-tunneling
        - rforward.py
        - test_rsa.key

- writing-sniffer
    - scanner.py
    - sniffer.py
    - sniffer_ip_header_decode.py
    - sniffer_with_icmp.py

- using-scapy
    - Scapy & ARP Poisoning (with an extra flavour of image reco)
    - arper.py
    - mail_sniffer.py
    - pic_carver.py

- web-hackery
    - mapper.py
    - bruter.py
    - wordpress-killer.py

- github command and control
    - bhptrojan
        - config
            - abc.json
        - data
        - modules
            - dirlister.py
            - environment.py
    - git-trojan.py