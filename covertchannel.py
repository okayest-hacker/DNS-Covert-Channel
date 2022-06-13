#! /usr/bin/env python3

from scapy.all import DNS, DNSQR, IP, sr1, UDP

#data sent in octal

covert = [125, 120, 114, 117, 101, 104]



for i in covert:
    dns_req = IP(dst='8.8.8.8')/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname='www.thepacketgeek.com/?'+str(i)))
    answer = sr1(dns_req, verbose=0)

print(payload sent)
