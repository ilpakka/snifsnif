import socket
import threading
import csv
import argparse

def print_banner():
    print("""
    _____       _  __           _  __ 
   /  ___|     (_)/ _|         (_)/ _|
   \ `--. _ __  _| |_ ___ _ __  _| |_ 
    `--. \ '_ \| |  _/ __| '_ \| |  _|
    /\__/ / | | | | | \__ \ | | | | |  
    \____/|_| |_|_|_| |___/_| |_|_|_|  
                                   
   Snifsnif by ilpakka
   """)

def scan_port(target, port, results, verbose, ipv6):
    family = socket.AF_INET6 if ipv6 else socket.AF_INET
    try:
        with socket.socket(family, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                service = get_service_name(port)
                results.append((port, service))
                print(f"[+] Port {port} ({service}) is open")
            elif verbose:
                print(f"[-] Port {port} is closed")
    except Exception as e:
        if verbose:
            print(f"[!] Error scanning port {port}: {e}")

def scan_target(target, ports, save, filename, verbose, ipv6):
    print(f"\nScanning target: {target} (IPv6: {ipv6})\n")
    results = []
    threads = []
    
    for port in ports:
        thread = threading.Thread(target=scan_port, args=(target, port, results, verbose, ipv6))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

    if save:
        save_results(target, results, filename)

def get_service_name(port):
    try:
        return socket.getservbyport(port)
    except OSError:
        return "Unknown"

def save_results(target, results, filename):
    filename = filename or f"Snifsnif_results_{target}.csv"
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Port", "Service"])
            writer.writerows(results)
        print(f"Results saved to {filename}")
    except IOError as e:
        print(f"[!] Failed to save results: {e}")

def main():
    print_banner()
    parser = argparse.ArgumentParser(description="Snifsnif by ilpakka")
    parser.add_argument("target", help="Target IP address")
    parser.add_argument("ports", help="Port range (e.g., 20-100)")
    parser.add_argument("--save", action="store_true", help="Save results to a file")
    parser.add_argument("--filename", type=str, help="Specify filename (default: Snifsnif_results_TARGET.csv)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("--ipv6", action="store_true", help="Enable IPv6 scanning")
    
    args = parser.parse_args()
    
    try:
        start_port, end_port = map(int, args.ports.split('-'))
    except ValueError:
        print("[!] Bro your port is invalid.")
        return

    ports = range(start_port, end_port + 1)
    scan_target(args.target, ports, args.save, args.filename, args.verbose, args.ipv6)

if __name__ == "__main__":
    main()
