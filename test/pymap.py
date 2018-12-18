import socket
import os
os.system('cls')
print """
 _   _ ___  ___  ___  ______  
| \ | ||  \/  | / _ \ | ___ \ 
|  \| || .  . |/ /_\ \| |_/ / 
| . ` || |\/| ||  _  ||  __/  
| |\  || |  | || | | || |     
\_| \_/\_|  |_/\_| |_/\_| 


"""
target = raw_input('What target to scan?: ')
x = raw_input('Port Min : ')
y = raw_input('Port Max : ')
def pscan(port):
    try:
        con = s.connect((target,port))
        return True
    except:
        return False


while int(x) <= int(y):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if pscan(x):
        print'Port',x,'is open'
    else:
        print'Port',x,'is close'
    x = int(x) + 1
    s.close

pscan
