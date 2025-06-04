import subprocess

subprocess.run(["sudo", "apt", "install", "-y", "whois"])
subprocess.run(["sudo", "apt", "install", "-y", "nikto"])
subprocess.run(["sudo", "apt", "install", "-y", "whatweb"])
subprocess.run(["sudo", "apt", "install", "-y", "dnsenum"])
subprocess.run(["sudo", "apt", "install", "-y", "assetfinder"])
subprocess.run(["sudo", "apt", "install", "-y", "wafw00f"])
subprocess.run(["sudo", "apt", "install", "-y", "theharvester"])
subprocess.run(["go", "install", "-v", "github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest"])
subprocess.run(["sudo", "apt", "install", "-y", "dirsearch"])
