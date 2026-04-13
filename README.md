# SSH Brute Force Detector

## Description
A Python-based security tool that monitors SSH authentication logs, detects brute force login attempts, and automatically blocks malicious IP addresses using Linux firewall rules.

## Skills Demonstrated
- Python scripting
- Linux log analysis
- Firewall automation with iptables
- Threat detection and incident response
- Security tool development

## How It Works
1. Reads SSH authentication logs from /var/log/auth.log
2. Parses each log entry using Regular Expressions to extract IP addresses
3. Counts failed login attempts per IP address using a Counter
4. Flags any IP address that exceeds the threshold of 5 failed attempts
5. Automatically blocks flagged IP addresses using iptables firewall rules
6. Prints real time alerts and confirmations to the terminal

## Example Output
[ALERT] 192.168.1.105 has 7 failed login attempts - BLOCKING
[BLOCKED] 192.168.1.105 has been blocked successfully

## Technologies Used
- Python 3
- Linux
- iptables
- Regular Expressions
- Kali Linux

## Author
Al-amin Awe
Morgan State University - Cybersecurity
https://www.linkedin.com/in/al-amin-awe-50aa12348/
