# E4ldosint
Osint Tool
# E4ldOSINT - Powerful Domain Reconnaissance Tool 🔎

**E4ldOSINT** is a lightweight yet powerful OSINT (Open Source Intelligence) toolkit for gathering domain information using both aggressive and quiet scanning modes. It combines several well-known tools to give you fast, flexible, and firewall-aware recon power — all in a simple Python CLI.

## 💡 Features

- Aggressive and Quiet scanning modes
- Automated integration of tools like:
  - `nmap`, `nikto`, `dirsearch`, `theHarvester`, `wafw00f`, `whatweb`
  - `dnsenum`, `assetfinder`, `subfinder`, `whois`
- English-based terminal interface
- Lightweight and terminal-based
- Ideal for bug bounty, recon, CTF, and red teaming

---

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/e4ldosint.git
cd e4ldosint
sudo python3 setup.py
python3 e4ldosint.py
This will install:
whois, nikto, whatweb, dnsenum, assetfinder,
wafw00f, theharvester, subfinder, dirsearch
🔥 Mode Descriptions
🔹 Aggressive Mode (a)
Performs deep scans using fast and detailed parameters. Best used in environments where detection is not an issue.

Tools & Parameters used:

nmap with OS detection, full port scan

dirsearch with recursive crawling

nikto, theHarvester, dnsenum, assetfinder, subfinder, etc.

🔹 Quiet Mode (q)
Performs minimal, stealthy scans to avoid triggering firewalls or IPS.

Tools run in low-noise mode with slower timing:

nmap with stealth SYN scan

dirsearch with low timeout & delay

Passive DNS/email recon via theHarvester, etc.

⚠️ Legal Disclaimer
This tool is intended for educational and authorized testing purposes only.
Do not use against systems you do not have permission to test.
The developer is not responsible for any misuse or illegal activity.
