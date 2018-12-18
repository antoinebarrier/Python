from logging import getLogger, ERROR
getLogger("scapy.runtime").setLevel(ERROR)
from scapy.all import *
import sys
from datetime import datetime
from time import strftime
import os
os.system('cls')
from colorama import Fore, Back, Style

print"""

  ____   ____    _    ______   __  ____   ____    _    _   _ 
 / ___| / ___|  / \  |  _ \ \ / / / ___| / ___|  / \  | \ | |
 \___ \| |     / _ \ | |_) \ V /  \___ \| |     / _ \ |  \| |
  ___) | |___ / ___ \|  __/ | |    ___) | |___ / ___ \| |\  |
 |____/ \____/_/   \_\_|    |_|   |____/ \____/_/   \_\_| \_|
                                                             


"""
#DEBUT DU PROGRAMME
#DEMANDE UTILISATEUR
try:
        target = raw_input("[*] Entrer l'IP cible : ")
        min_port = raw_input("[*] Entrer le port mini : ")
        max_port = raw_input("[*] Entrer le port max : ")
        try:
                if int(min_port) >= 0 and int(max_port) >= 0 and int(max_port) >= int(min_port):
                    pass
#GESTION DES ERREURS DE SAISIE
                else:
                    print "\n[!] Entree Invalide"
                    print "[!] Exiting..."
                    sys.exit(1)

        except Exception:
                print "\n[!] Entre Invalide"
                print "[!] Exiting..."
                sys.exit(1)
except KeyboardInterrupt:
    print "\n[*] User Requested Shutdown..."
    print "[*] Exiting..."
    sys.exit(1)

#DECLARATION DES VARIABLES
ports = range(int(min_port), int(max_port)+1)
start_clock = datetime.now()
SYNACK = 0x12
RSTACK = 0x14

#CHECK HOST
def checkhost(ip):
    conf.verb = 0
    try:
            ping = sr1(IP(dst =ip)/ICMP())
            print "\n[*] Cible Up, debut du scan..."
    except Exception:
            print "\n[!] Cible down, arret du scan..."
            print "[!] Exiting..."
            sys.exit(1)


#PROG SCAN DE PORT            
def scanport(port):
    srcport = RandShort()
    conf.verb = 0
    SYNACKpkt = sr1(IP(dst = target)/TCP(sport = srcport, dport = port, flags = "S"))
    pktflags = SYNACKpkt.getlayer(TCP).flags
    if pktflags == SYNACK:
        return True
    else:
        return False
    RSTpkt = IP(dst = target)/TCP(sport = srcport, dport = port, flages = "R")
    send(RSTpkt)

checkhost(target)
#DEBUT DU SCAN + HEURE DE DEBUT
print "[*] Debut du scan a " + strftime("%H:%M:%S") + " ! \n"

for port in ports:
    status = scanport(port)
    if status == True:
        print "Port : " + str(port) + Fore.GREEN + " est ouvert" + Fore.WHITE
    else:
        print "Port : " + str(port) + Fore.RED + " est pas ouuuuvert GROS" + Fore.WHITE

stop_clock = datetime.now()
total_time = stop_clock - start_clock
print "\n[*] Scan terminee avec succes"
print "[*] Duree total du scan : " + str(total_time)
print "[*] Fin du scan a : " + strftime("%H:%M:%S") + " ! \n"
