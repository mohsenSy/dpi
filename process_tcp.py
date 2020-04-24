import pyshark
import sys
from dpi.models import TCPPacket

def main():
    file_name = "smallFlows.pcap"
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    capture = pyshark.FileCapture(file_name)
    num_http_request = 0
    for packet in capture:
        if "tcp" in packet:
            tcp = packet.tcp
            ip = packet.ip
            srcPort = int(tcp.srcPort)
            dstPort = int(tcp.dstPort)
            srcIP = ip.src
            dstIP = ip.dst
            print(f"Adding TCP packet ({srcIP}:{srcPort}) --> ({dstIP}:{dstPort})")
            TCPPacket.add(srcPort, dstPort, srcIP, dstIP)

if __name__ == '__main__':
    main()
