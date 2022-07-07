from scapy.all import *
from threading import Thread


class Sniffer(Thread):
    def __init__(self, que):
        super().__init__()
        self.que = que
        self.iface = "Intel(R) Ethernet Connection (14) I219-V"
        self.mac_filter = "ether src 66:44:33:22:11:01"

    def run(self):
        print('starting sniffing...')
        while True:
            # sniff(prn=self.que.put, iface=self.iface, filter=self.mac_filter)
            packets = sniff(prn=self.que.put, iface=self.iface, filter=self.mac_filter,count=500)
            for packet in packets:
                self.que.put(packet)
            # self.que.put(pkts)