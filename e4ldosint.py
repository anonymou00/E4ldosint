import subprocess

# Input
target = input("Enter the target site (e.g., example.com): ")
choice = input("Mode info: Aggressive mode: Stronger and deeper scan | Quiet mode: Stealthier, bypasses firewalls like Nginx. Choose mode (Aggressive = a | Quiet = q): ").lower()

# Aggressive Mode
if choice == "a":
    print("\n[+] Aggressive mode started...\n")
    subprocess.run(["dirsearch", "-u", target, "--timeout=30", "--random-agent", "--crawl", "3"])
    subprocess.run(["wafw00f", target, "-v"])
    subprocess.run(["nmap", "-O", "-T4", "-sV", "-sS", "-p-", target])
    subprocess.run(["theharvester", "-d", target, "-b", "all"])
    subprocess.run(["whois", "--verbose", target])
    subprocess.run(["nikto", "-h", f"https://{target}", "--check6", "--Display", "2", "--useragent", "Mozilla/5.0", "--timeout", "10"])
    subprocess.run(["whatweb", "-v", "-a", "4", "-l", target])
    subprocess.run(["assetfinder", target])
    subprocess.run(["dnsenum", "-w", "-v", "-t", "10", "--enum", "--threads", "5", "-s", "15", "-w", target])
    subprocess.run(["subfinder", target])

# Quiet Mode
elif choice == "q":
    print("\n[+] Quiet mode started...\n")
    subprocess.run(["dirsearch", "-u", target, "--timeout=10", "--crawl", "1", "--random-agent", "--delay", "2"])
    subprocess.run(["wafw00f", target])
    subprocess.run(["nmap", "-sS", "-T1", "-Pn", target])
    subprocess.run(["theharvester", "-d", target, "-b", "bing"])
    subprocess.run(["whois", target])
    subprocess.run(["nikto", "-h", f"https://{target}", "--Display", "0", "--timeout", "5", "--useragent", "Mozilla/5.0"])
    subprocess.run(["whatweb", "--no-errors", target])
    subprocess.run(["assetfinder", "--subs-only", target])
    subprocess.run(["dnsenum", "-t", "3", "--noreverse", "--nocolor", target])
    subprocess.run(["subfinder", "-d", target, "-silent"])

# Invalid Input
else:
    print("Invalid choice! Please choose 'q' for Quiet or 'a' for Aggressive mode.")
)




