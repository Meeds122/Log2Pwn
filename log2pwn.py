#!/usr/bin/python3

import os

class Ports(object):
    blacklist = [20,21,22,23,25,53,67,68,110,123,137,143,445,546,547]
    known_protocols = [80,443] # HTTP/S for now

class Host(object):
    def __init__(self, address):
        self.address = address
        self.open_ports = list()
        self.vulnerable_ports = list()
        return
    def isOnline(self):
        if os.system("ping -c 1 {}".format(self.address)) == 0:
            self.online = True
        else:
            self.online = False
        return self.online


if __name__=="__main__":
    print("[*] This software is licensed under the GPLv3 License.")
    print("[*] It is also only meant for legal testing purposes.")
    print("[*] Illegal use of this product is strictly prohibited")
    print("[*] Authored by: Tristan Henning")
    address = input("[?] Host to attack: ")
    host = Host(address)
    if not host.isOnline():
        print("[!] Host not responding to ping probe, exiting")
        exit()
    print("[*] Host is online, initiating port scan")