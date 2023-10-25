from scapy.all import IP, TCP, UDP

def ip(packet):
    if IP in IP(packet):
        return IP(packet).fields

def tcp(packet):
    if TCP in TCP(packet):
        return TCP(packet).fields

def udp(packet):
    if UDP in UDP(packet):
        return UDP(packet).fields

def parse(packet):
    packet = IP(bytes(packet))
    print(packet.fields)


