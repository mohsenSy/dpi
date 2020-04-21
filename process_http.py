import pyshark
import sys
from dpi.models import HTTPrequest

def main():
    file_name = "smallFlows.pcap"
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    capture = pyshark.FileCapture(file_name)
    num_http_request = 0
    for packet in capture:
        if "tcp" in packet:
            tcp = packet.tcp
            dstport = int(tcp.dstport)
            if dstport == 80:
                num_http_request += 1
                if "http" in packet:
                    http = packet.http
                    HTTPrequest.add(http.request_method, http.request_full_uri, http.request_version)

if __name__ == '__main__':
    main()
