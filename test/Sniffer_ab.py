import time
import sys
import os
from scapy.all import *

#Clean Console
os.system('cls')


#Premiere ligne d'animation
animation1 = "Demarrage en cours..."
for i in range(21):
    time.sleep(0.01)
    sys.stdout.write(animation1[i % len(animation1)])
    sys.stdout.flush()

#Deuxieme ligne d'animation
animation2 = "\n \nChuuuut !   Sniffing en cours..."
for i in range(38):
    time.sleep(0.01)
    sys.stdout.write(animation2[i % len(animation2)])
    sys.stdout.flush()


#Obtenir le GET
def packet_callback(packet):
    if packet[TCP].payload:
        if packet[IP].dport == 80:
            print("\n == IP SOURCE == {} ----HTTP----> == IP TARGET == {}:{}:\n{}".format(packet[IP].src,
                                                         packet[IP].dst,
                                                         packet[IP].dport, 
                                                         str(bytes(packet[TCP].payload))))


sniff(filter='tcp', prn=packet_callback, store=0, count=0)
