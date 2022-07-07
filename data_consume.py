from scapy.all import *
import numpy as np
from threading import Thread


def trans_bytes2int(raw_data, data_len=64):
    data = np.zeros(data_len)
    for i in range(data_len):
        data[i] = raw_data[i]
    return data


class Consumer(Thread):
    def __init__(self,que):
        super().__init__()
        self.que = que
        self.channel_num = 32
        self.channels = np.empty([self.channel_num,0])


    def run(self):
        while True:
            msg = self.que.get()
            signals = trans_bytes2int(msg[Raw].load)
            signals2show = signals[1::2].reshape(32,1)
            self.channels = np.append(self.channels,signals2show,axis=1)
            # print(channels.shape)
