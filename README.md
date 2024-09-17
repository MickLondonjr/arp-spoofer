# ARP Spoofer

This Python script performs ARP spoofing, which allows an attacker to intercept traffic between two devices on a local network. The script uses Scapy to send ARP replies that trick the target machine and the gateway into thinking your machine's MAC address is associated with the other device's IP address.

**Warning: ARP spoofing is illegal without permission. Use this tool only in authorized environments, such as for penetration testing on networks you own or have permission to test.**

## Features

- Spoofs ARP responses to redirect traffic between a target machine and the gateway.
- Continuously sends spoofed packets to maintain the attack.
- Restores the network when the script is stopped (by sending legitimate ARP responses to both the target and gateway).

## Requirements

- Python 3.x
- `scapy` library (can be installed using `pip`)

## Usage

To run the ARP spoofing script, use the following syntax:

```bash
python arp_spoofer.py <target_ip> <gateway_ip>
```

For example:

```bash
python arp_spoofer.py 192.168.1.10 192.168.1.1
```

- `<target_ip>`: The IP address of the machine you want to spoof.
- `<gateway_ip>`: The IP address of the network gateway (usually your router).

### Example

```bash
python arp_spoofer.py 192.168.0.105 192.168.0.1
```

This example will trick the target machine (192.168.0.105) into thinking your machine is the gateway (192.168.0.1), and vice versa.

## Installation

1. Clone the repository or download the script.
2. Install the `scapy` library:

    ```bash
    pip install scapy
    ```

3. Run the script using Python 3:

    ```bash
    python arp_spoofer.py <target_ip> <gateway_ip>
    ```

## How it Works

1. The script sends forged ARP replies to both the target and the gateway:
   - The target machine receives a fake ARP reply associating your machine's MAC address with the IP of the gateway.
   - The gateway receives a fake ARP reply associating your machine's MAC address with the IP of the target machine.
   
2. This results in your machine being in the middle of the communication between the two devices, allowing you to intercept or modify their traffic.

3. When the script is interrupted (Ctrl + C), it sends legitimate ARP replies to both the target and the gateway to restore normal network communication.

## Legal Disclaimer

This script is intended for educational purposes only. Use it responsibly and only in environments where you have permission to test network security. Unauthorized use of this script on networks you do not own or have permission to test may violate laws and could result in criminal charges.
```
