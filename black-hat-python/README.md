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

- To perform tasks and report its findings back to 
- Trojan framework that will appear innocuous on the remote machine
- nefarious task

- Setting up Github account and repository
    - setup a github account with with repo "bhptrojan"
    - generate a token for authentication
    - copy token into file "mytoken.txt"
    - mytoken.txt and git-trojan.py should be in same folder 
    - bhptrojan
        - config
            - abc.json
        - data
        - modules
            - dirlister.py
            - environment.py
- Creating modules
    - dirlister.py
        - list all files in the current directory of trojan and returns that list as string
    - enviornment.py
        - retrieves any environment variables that are set on the remote machine on which the trojan is executing
- Configuring Trojan
    - abc.json
    - way to tell trojan what actions to perform and what modules are responsible for performing them.
    - also enables to effectively put a trojan to sleep (by not giving it any task)
    - configure the trojan to look in the config directory for TROJANID.json, which will return a simple JSON document that we can parse out, convert to a python dictionary, and then use to inform our trojan of which tasks to perform
    - The JSON format makes it easy to change configuration oprions as well
- Building GitHub-Aware Trojan
- Python's import Functionality
    - Python's import functionality is used to copy external libraries into programs to use their code
    - we are controlling remote machine, we may want to use a package not available on that machine
    - we also want to make sure that if we pull in a dependancy
    - Python allows us to customize how it imports modules; if it can't find a module locally, it will call an import class we define, which will allow us to remotely retrieve the library from out repo

### trojaning task on windows

- Common tasks for trojan after deployment
    - performing tasks on windows systems
    - grabing keystrokes
    - take screenshots
    - execute shellcode to provide interactive session
    - Keyogging and Keystrokes
        - The use of concealed program to record consecutive keystrokes
        - extremely effective at capturing sensitive information such as credentials or conversations.
        - PyWinHook library in python


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

- trojan-windows (trojaning-task-on-windows)
    - keylogger.py
    - screenshotter.py
    - shell_exec.py
    - sandbox_detect.py