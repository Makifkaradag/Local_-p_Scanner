

# -*- coding: utf-8 -*-
import os
import time

from subprocess import Popen

devnull = open(os.devnull, 'wb')

ips = (input(" Enter the IP Range you want  ( example: 192.168.1.54 ) ====> "))

print(" Scanned thread range",ips)


if ips == "":

 print( "Try a valid ip !")

import sys

p = []
active = 0
no_answer = 0
passive = 0

for aralik in range(0,255):
    ip = ips + ".%d" % aralik
    p.append((ip, Popen(['ping', '-c', '3', ip], stdout=devnull)))
while p:
    for i, (ip, proc) in enumerate(p[:]):
        if proc.poll() is not None:
            p.remove((ip, proc))
            if proc.returncode == 0:
                print('%s active' % ip)
                active = active + 1
            elif proc.returncode == 2:
                print('%s no_answer' % ip)
                active = no_answer + 1
            else:
                print('%s Pasif' % ip)
                pasif = passive + 1
    time.sleep(.04)
devnull.close()

import os

print("current operating system",os.name)
print("Ağ Durumu")
print("Active Ip  [ ",active," ]")
print("Passive Ip [ ",passive," ]")
print("no answer  [ ",no_answer," ]")
##aid recipients : github:ismail taşdelen



