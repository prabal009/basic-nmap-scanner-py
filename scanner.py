#!/usr/bin/python3
import nmap

scanner = nmap.PortScanner()

print("This is a simple nmap automation tool")
ip_addr = input("Please enter the ip address you want to scan: ")
print("The ip address you entered is", ip_addr)

resp = input("""\nPlease enter the type of scan you want to run
                1) SYN ACK Scan
                2) UDP Scan
                3) Comprehensive Scan \n""")

print("You have selected option: ", resp)

try:
    if resp == '1':
        print("Nmap Version: ", scanner.nmap_version())
        # -v (verbose), -sS (SYN ACK scan)
        scanner.scan(ip_addr, '1-1024', '-v -sS')
        print(scanner.scaninfo())
        print("IP Status: ", scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())

        if 'tcp' in scanner[ip_addr]:
            print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
        else:
            print("No open TCP ports found.")

    elif resp == '2':
        print("Nmap Version: ", scanner.nmap_version())
        # -v (verbose), -sU (UDP scan)
        scanner.scan(ip_addr, '1-1024', '-v -sU')
        print(scanner.scaninfo())
        print("IP Status: ", scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())

        if 'udp' in scanner[ip_addr]:
            print("Open Ports: ", scanner[ip_addr]['udp'].keys())
        else:
            print("No open UDP ports found.")

    elif resp == '3':
        print("Nmap Version: ", scanner.nmap_version())
        # -sS (SYN), -sV (Version), -sC (Default Scripts), -A (Aggressive), -O (OS)
        scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
        print(scanner.scaninfo())
        print("IP Status: ", scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())

        if 'tcp' in scanner[ip_addr]:
            print("Open ports:", scanner[ip_addr]['tcp'].keys())
        else:
            print("No open TCP ports found.")

    else:
        print("Please enter a valid option (1, 2, or 3)")

except Exception as e:
    print("\n[!] An error occurred!")
    print("[!] Make sure the IP is valid, the host is online, and you ran the script with 'sudo'.")
    print("Error details:", e)
