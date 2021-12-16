#!/usr/bin/python3

import os
import subprocess

class Ports(object):
    blacklist = [20,21,22,23,25,53,67,68,110,123,137,143,445,546,547]
    known_protcols = ["http", "https"]
    web_protocols = ["http", "https"] # HTTP/S for now

class Host(object):
    def __init__(self, address):
        self.address = address
        self.open_ports = list()
        self.vulnerable_ports = list()
        return
    def isOnline(self):
        if os.system("ping -c 1 {} 1> /dev/null".format(self.address)) == 0:
            self.online = True
        else:
            self.online = False
        return self.online
    def scanPorts(self):
        # sets self.open_ports to a list of tuples with (port, "protocol") as entries
        scan_results = subprocess.check_output(['nmap', '--open', '-p1-65535', '-Pn', self.address]).decode('utf-8')
        results_list = scan_results.split("\n")
        for entry in results_list:
            if(entry.find("open") != -1):
                protocol = entry.split(" ")[-1]
                port = entry.split("/")[0]
                self.open_ports.append((int(port), protocol))
        return


if __name__=="__main__":
    print("[*] This software is licensed under the GPLv3 License.")
    print("[*] It is also only meant for legal testing purposes.")
    print("[*] Illegal use of this product is strictly prohibited!")
    print("[*] Authored by: Tristan Henning")
    address = input("[?] Host to attack: ")
    host = Host(address)
    if not host.isOnline():
        print("[!] Host not responding to ping probe, exiting")
        exit()
    print("[*] Host is online, initiating port scan")
    host.scanPorts()
    if(len(host.open_ports) == 0):
        print("[!] No open ports found, exiting")
        exit()
    print("[*] Open ports found, analyzing")
