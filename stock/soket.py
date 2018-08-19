# __author__:"Adolphus"
# project:'stock'
import socket
s=socket.socket()
s.connect(('111.202.43.166',80))
rev=s.recv(4096)
print(rev)