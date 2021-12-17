#!/usr/bin/python3

import os
import subprocess

class Ports(object):
    blacklist = [20,21,22,23,25,53,67,68,110,123,139,143,445,546,547]
    known_protcols = ["http", "https"]
    web_protocols = ["http", "https"] # HTTP/S for now

class Exploit(object):
    # Testing Exploitability
    def test(remote_host, local_host, port_proto):
        if port_proto[1] in Ports.web_protocols:
            return Exploit.test_web(remote_host, local_host, port_proto)
        else:
            return Exploit.test_unkown(remote_host, local_host, port_proto)
    # Need function to blast Log4j exploit string at a host and wait for a response request
    def test_unkown(remote_host, local_host, port_proto):
        # returns true if the call back occurs
        return
    # Need function to send HTTP/s requests with Log4j exploit strings at a host and 
    # wait for a response request
    def test_web(remote_host, local_host, port_proto):
        #returns true if the call back occurs
        return
    
    # Raining shells
    def exploit(remote_host, local_host, port_proto):
        return


class Host(object):
    def __init__(self, address):
        self.address = address
        self.open_ports = list() # [(port, proto), ...]
        self.targeted_ports = list() # [(port, proto), ...]
        self.vulnerable_ports = list() # [(port, proto), ...]
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
            if entry.find("open") != -1:
                protocol = entry.split(" ")[-1]
                port = entry.split("/")[0]
                self.open_ports.append((int(port), protocol))
        return
    def determineTargets(self):
        for port in self.open_ports:
            if port[0] not in Ports.blacklist:
                self.targeted_ports.append(port)
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
    if len(host.open_ports) == 0:
        print("[!] No open ports found, exiting")
        exit()
    host.determineTargets()
    print("[*] The following ports were found: ")
    for port in host.targeted_ports:
        print("[-] {} {}".format(port[0],port[1]))
    if input("[?] Attempt to exploit listed ports? [y/n]: ") != "y":
        exit()
    local_host = input("[?] Please enter the address of the local host: ")
    for port in host.targeted_ports:
        Exploit.test(host.address, local_host, port)